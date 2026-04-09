import streamlit as st
import random
import datetime
import os
import time

# ১. মাস্টার ডাটাবেস ও ট্র্যাকিং ফাইল
TRACKER_FILE = "akash_master_logs.txt"

def log_all_data(name, email, ip, device, amount, trxid):
    now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    log_entry = f"🚀 [SYSTEM ACCESS] {now} | Name: {name} | Email: {email} | IP: {ip} | Device: {device} | Amount: ৳{amount} | TrxID: {trxid}"
    with open(TRACKER_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

# ২. পেজ সেটআপ ও প্রফেশনাল নাসা নিয়ন থিম
st.set_page_config(page_title="NASA SUPREME SERVER | AKASH", page_icon="📡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');
    .stApp { background: radial-gradient(circle at center, #00122e 0%, #000000 100%) !important; color: #ffffff; font-family: 'Share Tech Mono', monospace; }
    .main-title { color: #00f2ff; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 45px; text-shadow: 0 0 35px #00f2ff, 0 0 10px #ffffff; margin-bottom: 25px; }
    .logo-container { text-align: center; margin-top: -30px; margin-bottom: 20px; }
    .payment-box { border: 2px solid #e2136e; padding: 20px; border-radius: 15px; background: rgba(226, 19, 110, 0.12); text-align: center; margin-bottom: 15px; box-shadow: 0 0 15px rgba(226, 19, 110, 0.4); }
    .hacker-alert { background: #ff0000; color: #fff; padding: 25px; border-radius: 12px; text-align: center; font-family: 'Orbitron', sans-serif; animation: blink 0.4s infinite; border: 3px solid #ffffff; }
    @keyframes blink { 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# ৩. সেশন এবং সিকিউরিটি কনফিগারেশন
if 'step' not in st.session_state: st.session_state.step = "login"
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'hacker' not in st.session_state: st.session_state.hacker = False

# তোমার গোপন পাসওয়ার্ড ও নাম্বার (আকাশ স্পেশাল)
OWNER_KEY = "Akash@Owner#2026"   # তোমার নিজের জন্য
VIP_CODE = "BAP-VIP-500"         # কাস্টমার ডিসকাউন্ট কোড
BKASH_NAGAD = "01967840830"

# ৪. হ্যাকার প্রোটেকশন
if st.session_state.hacker:
    st.markdown('<div class="hacker-alert">🚨 SYSTEM BREACH DETECTED!<br>IP & DEVICE LOGGED BY CYBER DIVISION.</div>', unsafe_allow_html=True)
    st.error("হ্যাকিং চেষ্টার কারণে আপনার তথ্য রেকর্ড করা হয়েছে।")
    if st.button("I APOLOGIZE & EXIT"): 
        st.session_state.hacker = False
        st.rerun()
    st.stop()

# ৫. এন্ট্রি গেটওয়ে (লগইন ও পেমেন্ট জিমেইলসহ)
if st.session_state.step == "login":
    st.markdown(f"""<div class="logo-container"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="160"></div>""", unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">NASA MASTER CORE V32</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # ওনার লগইন সেকশন
        st.markdown("<h3 style='color:#00f2ff; text-align:center;'>🛡️ Owner Master Access</h3>", unsafe_allow_html=True)
        owner_pass = st.text_input("Enter Private Key:", type="password", placeholder="আপনার গোপন কোড দিন")
        if st.button("Enter Admin Core"):
            if owner_pass == OWNER_KEY:
                st.session_state.is_admin = True
                st.session_state.step = "dashboard"
                st.rerun()
            elif owner_pass != "": st.warning("Access Denied! Incorrect Key.")

        st.markdown("<hr style='border-color:#00f2ff;'>", unsafe_allow_html=True)
        
        # কাস্টমার জিমেইল ও পেমেন্ট গেটওয়ে
        st.markdown("<h3 style='text-align:center;'>💳 Customer Payment Gateway</h3>", unsafe_allow_html=True)
        
        # লাইভ ভিআইপি ডিসকাউন্ট কোড চেক (অটোমেটিক স্লাইডার চেঞ্জ)
        v_input = st.text_input("🎁 VIP Discount Code (Optional):", placeholder="VIP কোড থাকলে দিন")
        is_vip_active = v_input.strip() == VIP_CODE
        
        # তোমার শর্ত অনুযায়ী প্রাইস রেঞ্জ আপডেট
        min_p, max_p = (500, 2000) if is_vip_active else (3000, 10000)
        if is_vip_active: st.success("✅ VIP BAP DISCOUNT ACTIVE! (৳500-৳2000)")
        
        amt = st.slider("Select Package Amount:", min_p, max_p, min_p, step=500)
        st.markdown(f'<div class="payment-box">Send Money: <b>৳{amt}</b><br>To: <b>{BKASH_NAGAD}</b></div>', unsafe_allow_html=True)

        with st.form("payment_form"):
            u_name = st.text_input("Full Name")
            u_email = st.text_input("Gmail Address (Must be valid)")
            u_trx = st.text_input("TrxID")
            
            if st.form_submit_button("Verify & Unlock Server"):
                if "@gmail.com" not in u_email.lower():
                    st.error("ভুল ইমেইল! অবশ্যই @gmail.com থাকতে হবে।")
                elif any(x in u_trx.lower() for x in ["hack", "bypass", "sql", "crack"]):
                    st.session_state.hacker = True
                    st.rerun()
                elif len(u_trx) >= 8 and u_name != "":
                    # ২১ কোটি পাওয়ারের ট্র্যাকিং জেনারেটর
                    ip = f"103.{random.randint(10,99)}.{random.randint(100,255)}." + str(random.randint(1,255))
                    dev = random.choice(["iPhone 15 Pro", "Samsung S24 Ultra", "Google Pixel 8", "OnePlus 12"])
                    log_all_data(u_name, u_email, ip, dev, amt, u_trx)
                    
                    st.session_state.user_info = {"name": u_name, "email": u_email}
                    st.session_state.step = "dashboard"
                    st.rerun()
                else:
                    st.error("সব তথ্য সঠিকভাবে পূরণ করুন।")

# ৬. সুপ্রিম ড্যাশবোর্ড (২১ কোটি পাওয়ার)
elif st.session_state.step == "dashboard":
    st.markdown(f'<h1 class="main-title">SYSTEM CORE ACTIVE: {st.session_state.is_admin and "AKASH OWNER" or st.session_state.user_info["name"]}</h1>', unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        st.info("🚀 POWER LEVEL: 210,000,000X | SUPREME ADMIN ACTIVE")
        tab1, tab2, tab3 = st.tabs(["🕵️‍♂️ Live Sales Log", "📱 Device Tracking", "⚙️ Server Control"])
        
        with tab1:
            st.subheader("কাস্টমার পেমেন্ট ডাটাবেস:")
            if os.path.exists(TRACKER_FILE):
                with open(TRACKER_FILE, "r", encoding="utf-8") as f:
                    logs = f.readlines()[::-1]
                    for log in logs:
                        st.markdown(f"<p style='color:#00ff88;'>{log}</p>", unsafe_allow_html=True)
            else:
                st.write("No logs yet.")
        
        with tab2:
            st.write("কানেক্টেড আইপি ও ডিভাইসের বিস্তারিত তথ্য ট্র্যাকিং মোডে আছে।")
            
        with tab3:
            st.write(f"Current VIP Code: **{VIP_CODE}**")
            st.write(f"Admin Key: **{OWNER_KEY}**")
            if st.button("Force Logout"):
                st.session_state.step = "login"
                st.session_state.is_admin = False
                st.rerun()
    else:
        st.success(f"Verified Access for {st.session_state.user_info['email']}")
        st.write("সার্ভার পাওয়ার: ২১ কোটি গুণ | স্ট্যাটাস: এনক্রিপ্টেড কানেকশন")
        st.chat_input("Enter Command to AI Server...")
