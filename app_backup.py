import streamlit as st
import pandas as pd
import os

DATA_FILE = "emr_data.csv"
# ပုံတွေနဲ့ပတ်သက်တာတွေကို ဖယ်ထုတ်လိုက်ပါပြီ

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Error Message", "Solution", "Category"]).to_csv(DATA_FILE, index=False)

st.set_page_config(layout="wide")

# CSS: စာသားများ အပြည့်ပေါ်ရန်နှင့် Table အကျဉ်းမဖြစ်စေရန်
st.markdown("""
    <style>
    .stApp { width: 100%; }
    .css-1r6slb0 { width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

st.title("🏥 EMR Issue Solver")

# Login Section
st.sidebar.title("🔐 Access Control")
role = st.sidebar.radio("Select Role", ["Other User", "Admin"])

if role == "Admin":
    pwd = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if pwd == "admin123":
            st.session_state.logged_in = True
            st.rerun()
    if st.sidebar.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
else:
    st.session_state.logged_in = False

df = pd.read_csv(DATA_FILE)
# Category ကို Text အဖြစ်ပြောင်းပေးထားတယ် (Error မတက်အောင်)
df['Category'] = df['Category'].astype(str)

# Admin (Edit/Delete)
if st.session_state.logged_in:
    st.subheader("🛠 Admin Panel: Edit/Delete")
    edited_df = st.data_editor(
        df, 
        use_container_width=True, 
        num_rows="dynamic",
        column_config={
            "Error Message": st.column_config.TextColumn(width="medium"),
            "Solution": st.column_config.TextColumn(width="large"),
            "Category": st.column_config.TextColumn(width="small"),
        }
    )
    if st.button("Save Changes"):
        edited_df.to_csv(DATA_FILE, index=False)
        st.success("Database Saved!")
        st.rerun()

# Other User (Search Only - List View)
else:
    st.info("🔍 Search Only")
    query = st.text_input("🔍 Error Message ကို ရိုက်ရှာပါ:")
    
    if query:
        res = df[df["Error Message"].str.contains(query, case=False, na=False)]
        if not res.empty:
            for _, row in res.iterrows():
                st.markdown("---")
                st.subheader(f"⚠️ {row['Error Message']}")
                st.write(f"**Solution:** {row['Solution']}")
                st.write(f"**Category:** {row['Category']}")
        else:
            st.warning("မတွေ့ရှိပါ။")
    else:
        st.write("ရှာဖွေရန် စာရိုက်ပါ...")
