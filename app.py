import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.set_page_config(page_title="Mandalar Hospital EMR Solver", layout="wide")

# Mandalar Hospital ပုံကို Background နှင့် Sidebar နောက်ခံပုံအဖြစ် ထည့်သွင်းခြင်း
st.markdown(
    """
    <style>
    /* Main Background Dark Theme */
    .stApp {
        background-color: #0d233a;
    }
    
    /* Sidebar Background ပုံနှင့် အရောင်ထည့်ခြင်း */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(rgba(13, 35, 58, 0.9), rgba(13, 35, 58, 0.9)), 
                          url('https://www.mandalarhealthcaregroup.com/images/business-units/hospital-1-up.png');
        background-size: cover;
        background-position: center;
    }

    /* Sidebar ထဲက စာသားများ အားလုံး ဖြူစင်ထင်ရှားစေရန် */
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* Main Page စာသားများ ဖြူစင်စေရန် */
    h1, h2, h3, p, label, .stMarkdown {
        color: #ffffff !important;
    }

    /* Text Input များနှင့် Box များကို ပိုမိုပေါ်လွင်စေရန် */
    .stTextInput input, .stTextArea textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if not os.path.exists("images"):
  os.makedirs("images")

CSV_FILE = "emr_data.csv"


def load_data():
  if os.path.exists(CSV_FILE):
    return pd.read_csv(CSV_FILE)
  else:
    return pd.DataFrame(
        columns=["Error Message", "Solution", "Category", "Images"]
    )


def save_data(df):
  df.to_csv(CSV_FILE, index=False)


df = load_data()

st.sidebar.markdown(
    "### 🏥 Mandalar Hospital\n*The first and only JCI accredited hospital in"
    " Upper Myanmar*"
)

app_mode = st.sidebar.selectbox(
    "Select Mode", ["🔍 User Search (Chatbot)", "🛠 Admin Management"]
)

if app_mode == "🔍 User Search (Chatbot)":
  st.title("🔍 သိလိုသည်ကိုရှာနိုင်သည် ကျေးဇူးပါဗျာ")
  query = st.text_input("🔍 ရှာလိုသည့် Error သို့မဟုတ် အကြောင်းအရာကို ရိုက်ပါ:")

  if query:
    if not df.empty and "Error Message" in df.columns:
      exact_res = df[
          df["Error Message"].str.contains(query, case=False, na=False)
      ]
      corpus = df["Error Message"].dropna().astype(str).tolist()

      if corpus:
        vectorizer = TfidfVectorizer()
        full_corpus = corpus + [query]
        tfidf_matrix = vectorizer.fit_transform(full_corpus)

        cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        best_match_idx = cosine_sim.argmax()
        highest_score = cosine_sim[0][best_match_idx]

        if exact_res.empty and highest_score > 0.15:
          similar_row = df.iloc[best_match_idx]
          res = pd.DataFrame([similar_row])
          st.success(
              f"💡 အနီးစပ်ဆုံး တွေ့ရှိချက် (Match Score: {highest_score:.2f})"
          )
        else:
          res = exact_res
      else:
        res = exact_res

    if not res.empty:
        for _, row in res.iterrows():
          st.markdown("---")
          st.subheader(f"⚠️ {row['Error Message']}")

          col1, col2 = st.columns([1, 2])
          with col1:
            if pd.notna(row["Images"]) and str(row["Images"]).strip() != "":
              for i, img_path in enumerate(str(row["Images"]).split(",")):
                if os.path.exists(img_path.strip()):
                  st.image(
                      img_path.strip(),
                      caption=f"ပုံ ({i+1})",
                      use_container_width=True,
                  )
            else:
              st.write("📸 No Image")
          with col2:
            st.write(f"**Solution:** {row['Solution']}")
            st.write(f"**Category:** {row['Category']}")
    else:
        st.warning("တောင်းပန်ပါတယ်လူကြီးမင်းရှာလိုသည့် အကြောင်းအရာကို မရှိပါသဖြင့်admin သို့တင်ပြထားပါမည့်ဗျ")
else:
  st.title("Admin Panel")
  action = st.radio(
      "လုပ်ဆောင်ချက်",
      ["➕ Add New Error", "✏️ Edit Existing Error", "🗑 Delete Error"],
  )

  if action == "➕ Add New Error":
    with st.form("add_form"):
      new_error = st.text_input("Error Message")
      new_sol = st.text_area("Solution")
      new_cat = st.text_input("Category")
      new_imgs = st.file_uploader(
          "Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True
      )
      if st.form_submit_button("Save & Add"):
        if new_error and new_sol:
          img_paths = (
              [os.path.join("images", img.name) for img in new_imgs]
              if new_imgs
              else []
          )
          if new_imgs:
            for img, p in zip(new_imgs, img_paths):
              with open(p, "wb") as f:
                f.write(img.getbuffer())
          new_row = pd.DataFrame([{
              "Error Message": new_error,
              "Solution": new_sol,
              "Category": new_cat,
              "Images": ",".join(img_paths),
          }])
          df = pd.concat([df, new_row], ignore_index=True)
          save_data(df)
          st.success("Successfully Added!")
          st.rerun()
        else:
          st.error("Fill required fields!")

  elif action == "✏️ Edit Existing Error":
    if not df.empty:
      sel = st.selectbox("Select Error to Edit", df["Error Message"].tolist())
      idx = df[df["Error Message"] == sel].index[0]
      curr = df.loc[idx]
      with st.form("edit_form"):
        e_err = st.text_input("Error Message", value=curr["Error Message"])
        e_sol = st.text_area("Solution", value=curr["Solution"])
        e_cat = st.text_input(
            "Category",
            value=str(curr["Category"]) if pd.notna(curr["Category"]) else "",
        )
        e_imgs = st.file_uploader(
            "New Images (Optional)",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
        )
        if st.form_submit_button("Update"):
          img_str = curr["Images"]
          if e_imgs:
            img_paths = [os.path.join("images", img.name) for img in e_imgs]
            for img, p in zip(e_imgs, img_paths):
              with open(p, "wb") as f:
                f.write(img.getbuffer())
            img_str = ",".join(img_paths)
          df.at[idx, "Error Message"] = e_err
          df.at[idx, "Solution"] = e_sol
          df.at[idx, "Category"] = e_cat
          df.at[idx, "Images"] = img_str
          save_data(df)
          st.success("Updated!")
          st.rerun()

  elif action == "🗑 Delete Error":
    if not df.empty:
      sel_del = st.selectbox("Delete Error", df["Error Message"].tolist())
      if st.button("Confirm Delete"):
        df = df[df["Error Message"] != sel_del]
        save_data(df)
        st.success("Deleted!")
        st.rerun()