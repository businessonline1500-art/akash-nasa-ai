import streamlit as st
import random
import datetime
import os
import time

# ১. ইমমর্টাল ডাটাবেস ও ডিভাইস ট্র্যাকার ফাইল
DB_FILE = "akash_secure_cloud.txt"
TRACKER_FILE = "device_spy_logs.txt"

def save_to_cloud(entry):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def log_device_info(name, ip, device):
    now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    log_entry = f"📱 [DEVICE DETECTED] Time: {now} | Name: {name} | IP: {ip} | Device: {device}"
    with open(TRACKER_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")
    save_to_cloud(log_entry)

# ২. ডিজাইন ও নিয়ন ইন্টারফেস
st.set_page_config(page_title="NASA AI | DEVICE TRACKER V23", page_icon="📡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');
    .stApp { background: radial-gradient(circle at center, #000510 0%, #000000 100%) !important; color: #ffffff; font-family: 'Share Tech Mono', monospace; }
    .main-title { color: #00f2ff; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 40px; text-shadow: 0 0 40px #00f2ff; }
    .spy-panel { border: 1px solid #00f2ff; padding: 15px; border-radius: 10px; background: rgba(0, 242, 255, 0.05); }
    .hacker-warning { background: #ff0000; color: #fff; padding: 20px; border-radius: 10px; text-align: center; font-size: 25px; animation: shake 0.5s infinite; }
    @keyframes shake { 0% { transform: translate(1px, 1px); } 50% { transform: translate(-2px, -1px); } 100% { transform: translate(1px, 1px); } }
</style>
""", unsafe_allow_html=True)

# ৩. সেশন ম্যানেজমেন্ট
if 'generated_ip' not in st.session_state: st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'payment_verified' not in st.session_state: st.session_state.payment_verified = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'hacker_detected' not in st.session_state: st.session_state.hacker_detected = False

GOD_MODE_KEY = "Akash@God#71"    
FREE_CODE = "Akash@Free#2026"

# ৪. হ্যাকার ট্র্যাপ (ভয় দেখানো)
if st.session_state.hacker_detected:
    st.markdown('<div class="hacker-warning">⚠️ SYSTEM BREACH DETECTED!<br>POLICE TRACKING IN PROGRESS...</div>', unsafe_allow_html=True)
    st.error("🚨 আপনার আইপি এবং ডিভাইস আইডি সদর দপ্তরে পাঠানো হয়েছে।")
    if st.button("EXIT NOW"):
        st.session_state.hacker_detected = False
        st.rerun()
    st.stop()

# ৫. এন্ট্রি গেটওয়ে ও অটো ট্র্যাকিং
if not st.session_state.authenticated:
    st.markdown('<div style="text-align: center;"><h1 class="main-title">NASA SUPREME SPY SERVER</h1></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="spy-panel">', unsafe_allow_html=True)
        
        if not st.session_state.payment_verified:
            ip_input = st.text_input("🛡️ Security IP Code:", placeholder="AKASH-XXXX")
            is_discounted = ip_input.strip().upper() == st.session_state.generated_ip
            min_v, max_v = (1000, 3000) if is_discounted else (3000, 10000)
            
            amount = st.slider("Select Energy Power:", min_v, max_v, min_v, step=500)
            st.markdown(f"<h2 style='text-align:center; color:#00f2ff;'>৳ {amount}</h2>", unsafe_allow_html=True)

            with st.form("entry_gate"):
                u_name = st.text_input("Your Name / ID")
                u_key = st.text_input("Encryption Key", type="password")
                if st.form_submit_button("CONNECT"):
                    # হ্যাকার চেক
                    if any(x in u_key.lower() for x in ["hack", "bypass", "sql"]):
                        st.session_state.hacker_detected = True
                        st.rerun()
                    
                    # ডিভাইস অটো ট্র্যাকিং লজিক (সিমুলেটেড ফর ওয়েব)
                    dummy_ip = f"103.{random.randint(10,99)}.{random.randint(100,255)}.{random.randint(1,255)}"
                    devices = ["iPhone 15 Pro", "Samsung S24 Ultra", "Pixel 8", "Desktop Windows", "Xiaomi 14"]
                    detected_device = random.choice(devices)

                    if u_key == GOD_MODE_KEY:
                        st.session_state.payment_verified, st.session_state.authenticated, st.session_state.is_admin = True, True, True
                        st.session_state.user_name = "Akash Master"
                        st.rerun()
                    elif u_key == FREE_CODE or len(u_key) >= 8:
                        st.session_state.payment_verified = True
                        st.session_state.temp_name = u_name if u_name else "Anonymous"
                        # ইউজারের তথ্য সেভ করা
                        log_device_info(st.session_state.temp_name, dummy_ip, detected_device)
                        st.rerun()
        else:
            with st.form("gmail_gate"):
                st.info("Identity Confirmed! Link your Gmail.")
                u_email = st.text_input("Gmail Address")
                if st.form_submit_button("START SERVER"):
                    if "@gmail.com" in u_email:
                        st.session_state.authenticated = True
                        st.session_state.user_name = st.session_state.temp_name
                        st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # ৫. আকাশ এর স্পেশাল কন্ট্রোল সেন্টার (১৮ কোটি পাওয়ার)
    st.markdown(f"<h1 class='main-title'>MASTER HUB: {st.session_state.user_name}</h1>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        st.success("Welcome back Akash! System running at 180,000,000x Speed.")
        tab1, tab2, tab3 = st.tabs(["🕵️‍♂️ DEVICE SPY LOGS", "🔑 CONTROL CODES", "📱 UNIVERSAL WORK"])
        
        with tab1:
            st.subheader("📡 ইউজারদের মোবাইলের তথ্য (Live Tracking)")
            if os.path.exists(TRACKER_FILE):
                with open(TRACKER_FILE, "r", encoding="utf-8") as f:
                    logs = f.readlines()
                st.markdown(f'<div style="background:#000; padding:15px; color:#00ff88; border:1px solid #00f2ff; height:400px; overflow-y:scroll;">{"<br>".join(logs[::-1])}</div>', unsafe_allow_html=True)
            else:
                st.write("No device logs found yet.")
        
        with tab2:
            st.info(f"Current IP Code: {st.session_state.generated_ip}")
            st.success(f"Master God Key: {GOD_MODE_KEY}")
            if st.button("CLEAR ALL SPY LOGS"):
                if os.path.exists(TRACKER_FILE): os.remove(TRACKER_FILE)
                st.rerun()
        
        with tab3:
            st.markdown("### 🚀 Admin Master Tools")
            st.button("Sync Mobile Apps")
            st.button("Gmail Marketing Bot")
            if st.button("EXIT SERVER"):
                st.session_state.authenticated = False
                st.rerun()
    else:
        st.success(f"Verified {st.session_state.user_name}: Secure Connection Active.")
        st.chat_input("Enter your command...")

st.markdown("<p style='text-align: center; color: #333; margin-top: 50px;'>NASA Spy-Shield v23.0 | Total Device Intelligence by Akash</p>", unsafe_allow_html=True)
