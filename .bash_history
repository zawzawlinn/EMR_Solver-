sudo apt update
wget http://raw.githubusercontent.com/angristan/wiregurad-install/master/wireguard-install.sh -0 wireguard-install.sh
wget http://raw.githubusercontent.com/angristan/wiregurad-install/master/wireguard-install.sh -O wireguard-install.sh
[200~wget https://raw.githubusercontent.com/angristan/wireguard-install/master/wireguard-install.sh -O wireguard-install.sh~
wget https://raw.githubusercontent.com/angristan/wireguard-install/master/wireguard-install.sh -O wireguard-install.sh
chmod +x wirdguard-install.sh
chmod +x wireguard-install.sh
sudo ./wireguard-install.sh 
sudo fallocate -l 2G/swapfile
# 2GB အရွယ်အစားရှိတဲ့ Swap file တစ်ခု ဆောက်မယ်
sudo fallocate -l 2G /swapfile
# File ရဲ့ permission ကို ပြင်မယ်
sudo chmod 600 /swapfile
# Swap file အဖြစ် သတ်မှတ်မယ်
sudo mkswap /swapfile
# Swap ကို စတင်အသုံးပြုမယ်
sudo swapon /swapfile
# Backup ယူထားမယ်
sudo cp /etc/fstab /etc/fstab.bak
# Config ထဲကို ထည့်မယ်
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
free -h
exit
pip install stramlit pandas
sudo yum update -y
sudo apt update -y
sudo apt update && sudo apt upgrade
sudo apt install python3-pip -y
pip3 install streamlit pandas
nano app.py
sudo nano app.py
[200~ubuntu@ip-172-31-36-218:~$
~# ဖိုင်အဟောင်းဖျက်မယ်
rm app.py
# ဖိုင်အသစ်ပြန်ဆောက်ပြီး Code ထည့်မယ်
cat <<EOF > app.py
import streamlit as st
import pandas as pd
import os

DATA_FILE = "emr_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Error Message", "Solution", "Category"]).to_csv(DATA_FILE, index=False)

st.title("🏥 EMR Issue Solver")
menu = st.sidebar.radio("Menu", ["🔍 Search", "➕ Add/Edit"])
df = pd.read_csv(DATA_FILE)

if menu == "🔍 Search":
    query = st.text_input("Error Message ရှာရန်:")
    if query:
        st.write(df[df["Error Message"].str.contains(query, case=False, na=False)])

elif menu == "➕ Add/Edit":
    with st.form("add_form"):
        err = st.text_input("Error Message")
        sol = st.text_area("Solution")
        cat = st.text_input("Category")
        if st.form_submit_button("Save"):
            new_data = pd.DataFrame({"Error Message": [err], "Solution": [sol], "Category": [cat]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("Data Saved!")

st.write("---")
st.dataframe(df)
EOF

sudo rm -f app.py
# ဖိုင်အဟောင်းဖျက်မယ်
rm app.py
# ဖိုင်အသစ်ပြန်ဆောက်ပြီး Code ထည့်မယ်
cat <<EOF > app.py
import streamlit as st
import pandas as pd
import os

DATA_FILE = "emr_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Error Message", "Solution", "Category"]).to_csv(DATA_FILE, index=False)

st.title("🏥 EMR Issue Solver")
menu = st.sidebar.radio("Menu", ["🔍 Search", "➕ Add/Edit"])
df = pd.read_csv(DATA_FILE)

if menu == "🔍 Search":
    query = st.text_input("Error Message ရှာရန်:")
    if query:
        st.write(df[df["Error Message"].str.contains(query, case=False, na=False)])

elif menu == "➕ Add/Edit":
    with st.form("add_form"):
        err = st.text_input("Error Message")
        sol = st.text_area("Solution")
        cat = st.text_input("Category")
        if st.form_submit_button("Save"):
            new_data = pd.DataFrame({"Error Message": [err], "Solution": [sol], "Category": [cat]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("Data Saved!")

st.write("---")
st.dataframe(df)
EOF

streamlit run app.py --server.port 8501
pip install streamlit
pip3 streamlit
pip3 install streamlit
sudo rm -f app.py
python3 -mvenv venv source venv/bin/activate
sudo apt  update
sudo apt install python3-venv -y
python3 -m venv venv
soruce venv/bin/activate
source venv/bin/activate
pip install streamlit pandas
cat <<EOF > app.py
import streamlit as st
import pandas as pd
import os

DATA_FILE = "emr_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Error Message", "Solution", "Category"]).to_csv(DATA_FILE, index=False)

st.title("🏥 EMR Issue Solver")
menu = st.sidebar.radio("Menu", ["🔍 Search", "➕ Add/Edit"])
df = pd.read_csv(DATA_FILE)

if menu == "🔍 Search":
    query = st.text_input("Error Message ရှာရန်:")
    if query:
        st.write(df[df["Error Message"].str.contains(query, case=False, na=False)])

elif menu == "➕ Add/Edit":
    with st.form("add_form"):
        err = st.text_input("Error Message")
        sol = st.text_area("Solution")
        cat = st.text_input("Category")
        if st.form_submit_button("Save"):
            new_data = pd.DataFrame({"Error Message": [err], "Solution": [sol], "Category": [cat]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("Data Saved!")

st.write("---")
st.dataframe(df)
EOF

streamlit run app.py --server.port 8501
nano app.py
streamlit run app.py --server.port 8501
nano app.py
streamlit run app.py --server.port 8501
nano app.py
streamlit run app.py --server.port 8501
source venv/bin/activate
streamlit run app.py --server.port 8501
nano app.py
streamlit run app.py --server.port 8501
nano app.py
streamlit run app.py --server.port 8501
source venv/bin/acitivate
source venv/bin/activate
sudo nano /etc/systemd/system/emr_app.service
sudo systemctl daemon-reload
sudo systemctl enable emr_app
sudo systemctl start emr_app
sudo systemctl status emr_app
streamlit run app.py
nano app.py
sudo systemctl restart emr_app
streamlit run app.py
nano app.py
sudo systemctl restart emr_app
nano app.py
sudo systemctl restart emr_app
nano app.py
sudo systemctl restart emr_app
nano app.py
sudo systemctl restart emr_app
sudo nano/etc/systemd/system/emr_app.service
sudo nano /etc/systemd/system/emr_app.servic
source venv/bin/activate
sudo nano /etc/systemd/system/emr_app.servic
sudo systemctl deamon-reload
sudo systemctl daemon-reload
sudo systemctl enable emr-app
sudo systemctl enable emr_app
sudo systemctl daemon-reload
sudo systemctl enable emr_app
sudo systemctl start emr_app
nano app.py
sudo systemctl restart emr_app
nano app.py
sudo systemctl restart emr_app
exit
nano app.py
sudo chmod 777/home/ubuntu/images
sudo chmod 777 /home/ubuntu/images
mkdir -p/home/ubuntu/images
mkdir -p /home/ubuntu/images
sudo chmod 777 /home/ubuntu/images
sudo systemctl restart emr_app
rm emr_data.csv
cat emr_data.csv
nano app.py
rm emr_data.csv
nano app.py
sudo systemctl restart emr_app
# ၁။ မူရင်း Python code ကို backup သိမ်းခြင်း (မင်းရဲ့ file နာမည်က app.py မဟုတ်ရင် ပြောင်းပေးပါ)
cp app.py app_backup.py
# ၂။ မူရင်း CSV Data တွေကို backup သိမ်းခြင်း
cp emr_data.csv emr_data_backup.csv
# ၃။ ပုံတွေ သိမ်းဖို့ 'images' ဆိုတဲ့ folder ဆောက်ခြင်း
mkdir -p images
# ၄။ Folder ကို Permission ပေးခြင်း (Error မတက်အောင်)
sudo chmod -R 755 images
sudo chown -R ubuntu:ubuntu images
nano app.py
sudo systemctl restart emr_app service
sudo chmod -R 777 images
sudo systemctl restart emr_app
nano app.py
exit
