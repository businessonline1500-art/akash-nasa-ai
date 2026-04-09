import streamlit as st
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# --- CONFIGURATION & NASA UI ---
st.set_page_config(page_title="NASA MASTER CORE - V33", layout="wide")

# Custom CSS for Dark Neon NASA Look
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; }
    .stButton>button { background-color: #00FF00; color: black; border-radius: 10px; font-weight: bold; }
    .header { color: #00eaff; text-align: center; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>🚀 NASA OFFICIAL GATEWAY - SUPREME V33</h1>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg", width=100)

# --- SYSTEM SETTINGS ---
OWNER_PASS = "Akash@Owner#2026"
VIP_PROMO = "BAP-VIP-500"
AKASH_BKASH = "01967840830"
MY_GMAIL = "your-email@gmail.com" # এখানে তোমার জিমেইল দিও
GMAIL_APP_PASS = "your-app-password" # জিমেইলের অ্যাপ পাসওয়ার্ড

# --- SESSION STATE FOR DATABASE ---
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- FUNCTIONS ---
def send_email_alert(data):
    try:
        msg = MIMEText(f"নতুন পেমেন্ট এসেছে!\n\nতথ্য: {data}")
        msg['Subject'] = 'Akash NASA Server - New Payment Alert'
        msg['From'] = MY_GMAIL
        msg['To'] = MY_GMAIL
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MY_GMAIL, GMAIL_APP_PASS)
        server.send_message(msg)
        server.quit()
    except:
        pass # ইমেইল সেটআপ না থাকলেও যেন ক্র্যাশ না করে

# --- MAIN APP INTERFACE ---
tab1, tab2 = st.tabs(["💎 CUSTOMER GATEWAY", "🔐 AKASH ADMIN PANEL"])

with tab1:
    st.info("⚡ ১৮ কোটি পাওয়ারের মাস্টার সার্ভারে স্বাগতম")
    
    with st.form("payment_form"):
        name = st.text_input("আপনার নাম:")
        email = st.text_input("জিমেইল এড্রেস (অবশ্যই @gmail.com হতে হবে):")
        device = st.selectbox("আপনার ডিভাইসের ব্র্যান্ড:", ["iPhone/Samsung", "Xiaomi", "Vivo", "Oppo", "Realme", "Infinix", "Tecno", "Other"])
        promo = st.text_input("ডিসকাউন্ট প্রমো কোড (থাকলে দিন):")
        
        price = 2500
        if promo == VIP_PROMO:
            price = 500
            st.success(f"VIP কোড অ্যাক্টিভ! মূল্য এখন মাত্র {price} টাকা।")
        
        st.write(f"💵 পেমেন্ট করুন: **{AKASH_BKASH}** (বিকাশ/নগদ)")
        trxid = st.text_input("Transaction ID (TrxID) দিন:")
        
        submit = st.form_submit_button("SUBMIT PAYMENT")
        
        if submit:
            if "@gmail.com" in email and len(trxid) > 5:
                entry = {
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Name": name,
                    "Email": email,
                    "Device": device,
                    "Price": price,
                    "TrxID": trxid,
                    "IP": "Verified"
                }
                st.session_state.logs.append(entry)
                send_email_alert(entry) # ইমেইলে ব্যাকআপ পাঠানো
                st.success("পেমেন্ট সফলভাবে জমা হয়েছে! আকাশ আপনার সাথে যোগাযোগ করবে।")
            else:
                st.error("ভুল তথ্য দিয়েছেন! জিমেইল এবং TrxID চেক করুন।")

with tab2:
    st.subheader("ADMIN LOGIN")
    access_code = st.text_input("Enter Owner Key:", type="password")
    
    if access_code == OWNER_PASS:
        st.success("✅ SYSTEM CORE ACTIVE: AKASH OWNER")
        
        if st.session_state.logs:
            df = pd.DataFrame(st.session_state.logs)
            st.table(df)
            
            # --- PENDRIVE BACKUP SECTION ---
            st.markdown("### 📥 PENDRIVE BACKUP SECTION")
            csv = df.to_csv(index=False).encode('utf-8')
            
            st.download_button(
                label="কাস্টমার ডাটা ডাউনলোড করুন (পেনড্রাইভে রাখার জন্য)",
                data=csv,
                file_name=f"akash_backup_{datetime.now().strftime('%d_%m')}.csv",
                mime='text/csv',
            )
            st.info("উপরে ডাউনলোড বাটনে ক্লিক করে ফাইলটি সরাসরি তোমার পেনড্রাইভে সেভ করে রাখো।")
        else:
            st.warning("এখনো কোনো পেমেন্ট ডাটা আসেনি।")
    elif access_code != "":
        st.error("❌ ভুল পাসওয়ার্ড! হ্যাকিং অ্যালার্ট চালু হচ্ছে...")

# --- FOOTER ---
st.markdown("---")
st.caption("Powered by Akash NASA AI Master Core © 2026")
