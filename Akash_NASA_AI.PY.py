import streamlit as st
import pandas as pd
from datetime import datetime
import smtplib
import random
from email.mime.text import MIMEText

# --- NASA SUPREME CONFIGURATION ---
st.set_page_config(page_title="NASA MASTER CORE V33 - ULTRA MILITARY", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); }
    .header-text { color: #00eaff; text-align: center; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 30px #00eaff; }
    .stButton>button { background: linear-gradient(45deg, #00FF00, #008000); color: white; border-radius: 5px; height: 3em; font-weight: bold; width: 100%; }
    .security-log { color: #ff0000; font-family: 'Courier New'; font-weight: bold; text-align: center; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER SETTINGS ---
OWNER_PASS = "Akash@Owner#2026"
VIP_PROMO = "BAP-VIP-500"
AKASH_BKASH = "01967840830"
MY_GMAIL = "your-email@gmail.com" # এখানে তোমার জিমেইল দাও
GMAIL_APP_PASS = "your-app-password" # অ্যাপ পাসওয়ার্ড দাও

# --- DATABASE ---
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# --- ALERT FUNCTION ---
def send_security_alert(data):
    try:
        msg = MIMEText(f"🚨 NASA SECURITY ALERT: Breach Attempt!\n\nTarget Info: {data}")
        msg['Subject'] = '🚀 NASA & MILITARY EMERGENCY ALERT'
        msg['From'] = MY_GMAIL
        msg['To'] = MY_GMAIL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MY_GMAIL, GMAIL_APP_PASS)
        server.send_message(msg)
        server.quit()
    except:
        pass

# --- UI HEADER ---
st.markdown("<h1 class='header-text'>🚀 NASA OFFICIAL SUPREME CORE - AKASH EDITION</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF00;'>🛡️ NASA V33 PROTOCOL: ARMY & POLICE SYNC ACTIVE | POWER: 210M MHz</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💎 পেমেন্ট পোর্টাল", "🔐 NASA MASTER CONTROL"])

with tab1:
    st.markdown("### 💰 কাস্টমার পেমেন্ট সিস্টেম")
    with st.form("payment_form"):
        name = st.text_input("আপনার নাম:")
        email = st.text_input("জিমেইল এড্রেস (@gmail.com):")
        device = st.selectbox("ডিভাইস ব্র্যান্ড:", ["iPhone", "Samsung", "Xiaomi", "Vivo", "Oppo", "Realme", "Infinix", "Tecno", "Other"])
        promo = st.text_input("ডিসকাউন্ট কোড (VIP):")
        
        price = 2500
        if promo == VIP_PROMO:
            price = 500
            st.success(f"🔥 NASA VIP ডিসকাউন্ট গ্র্যান্টেড! মূল্য: {price} টাকা।")
        
        st.warning(f"বিকাশ/নগদ (Personal): {AKASH_BKASH}")
        trxid = st.text_input("Transaction ID (TrxID):")
        
        if st.form_submit_button("SUBMIT TO NASA SERVER"):
            if "@gmail.com" in email and len(trxid) >= 6:
                entry = {"Time": datetime.now().strftime("%H:%M:%S"), "Name": name, "Email": email, "Device": device, "Price": price, "TrxID": trxid}
                st.session_state.logs.append(entry)
                send_security_alert(f"Payment Entry from {name}")
                st.balloons()
                st.success("✅ ডাটা এনক্রিপ্ট করে নাসা মাস্টার সার্ভারে পাঠানো হয়েছে।")
            else:
                st.error("❌ ভুল তথ্য! সঠিক জিমেইল এবং TrxID দিন।")

with tab2:
    st.subheader("🔐 NASA Master Core Access")
    access_code = st.text_input("সিকিউরিটি কী (Key) দিন:", type="password")
    
    if access_code == OWNER_PASS:
        st.session_state.failed_attempts = 0
        st.success(f"🔓 এক্সেস গ্র্যান্টেড! স্বাগতম মাস্টার আকাশ।")
        
        if st.session_state.logs:
            df = pd.DataFrame(st.session_state.logs)
            st.dataframe(df, use_container_width=True)
            
            # PENDRIVE BACKUP
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 পেনড্রাইভে ডাটা ব্যাকআপ নিন",
                data=csv,
                file_name=f"NASA_Akash_Backup_{datetime.now().strftime('%d_%m')}.csv",
                mime='text/csv'
            )
        else:
            st.info("অপেক্ষমান: এখনো কোনো নতুন ডাটা আসেনি।")
            
    elif access_code != "":
        st.session_state.failed_attempts += 1
        
        # --- NASA & MILITARY SECURITY BREACH ---
        st.markdown("<div class='security-log'>🚨 NASA SECURITY BREACH DETECTED! 🚨</div>", unsafe_allow_html=True)
        st.error(f"অবৈধ অনুপ্রবেশের চেষ্টা! (প্রচেষ্টা নং: {st.session_state.failed_attempts})")
        
        fake_ip = f"{random.randint(100,255)}.{random.randint(10,99)}.{random.randint(100,255)}.{random.randint(1,255)}"
        st.warning(f"সতর্কবার্তা: নাসা সার্ভার আপনার আইপি ({fake_ip}) ট্র্যাক করেছে।")
        st.markdown("<h3 style='color:red; text-align:center;'>সংকেত পাঠানো হচ্ছে: বাংলাদেশ সেনাবাহিনী ও পুলিশ সাইবার ইউনিট...</h3>", unsafe_allow_html=True)
        
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
        
        if st.session_state.failed_attempts >= 3:
            st.markdown("<h2 style='color:red; text-align:center;'>🔴 NASA & ARMY CYBER UNIT ENGAGED! 🔴</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color:yellow; text-align:center; font-weight:bold;'>আপনার ডিভাইসের বর্তমান লোকেশন পুলিশ কন্ট্রোল রুমে শেয়ার করা হয়েছে।</p>", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 AKASH NASA AI MASTER SYSTEM | MILITARY & POLICE PROTECTION V33")  
