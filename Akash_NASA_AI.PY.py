import streamlit as st
import random
import string
import datetime
import os

# ১. ইমমর্টাল ক্লাউড ডাটাবেস
DB_FILE = "akash_cloud_db.txt"

def save_to_cloud(entry):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def load_cloud_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

# ২. পেজ সেটআপ ও আল্টিমেট ডিজাইন
st.set_page_config(page_title="NASA AI SERVER | GOD MODE ACTIVE", page_icon="📡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #000814 0%, #000000 100%) !important; color: #ffffff; font-family: 'Rajdhani', sans-serif; }
    .main-title { color: #ff3c00; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 55px; text-shadow: 0 0 30px #ff3c00; margin-top: -50px; }
    .glass-card { background: rgba(255, 60, 0, 0.05); backdrop-filter: blur(25px); padding: 35px; border-radius: 30px; border: 1px solid #ff3c00; box-shadow: 0 0 50px rgba(255, 60, 0, 0.2); }
    .spy-box { background: #000; border: 2px solid #00f2ff; padding: 20px; border-radius: 15px; font-family: 'Courier New', monospace; color: #00f2ff; height: 400px; overflow-y: scroll; }
    .promo-box { background: linear-gradient(90deg, #ff3c00, #9d0000); color: white; padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; }
    .admin-badge { background: #ffcc00; color: #000; padding: 5px 15px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 10px;}
</style>
""", unsafe_allow_html=True)

# ৩. সেশন স্টেট ও সিক্রেট কী
if 'generated_ip' not in st.session_state:
    st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'payment_verified' not in st.session_state: st.session_state.payment_verified = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# তোমার স্পেশাল বাইপাস পাসওয়ার্ড
GOD_MODE_KEY = "Akash@God#71"

def log_activity(user, action):
    now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    entry = f"🛡️ [{now}] {user} >> {action}"
    save_to_cloud(entry)

# ৪. মেইন লজিক গেট
if not st.session_state.authenticated:
    st.markdown('<div style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="160"><h1 class="main-title">NASA AI SERVER PRO</h1></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        # পেমেন্ট ও লগইন ধাপ
        if not st.session_state.payment_verified:
            st.markdown('<div class="promo-box">🎁 আপনার কাছে কি ডিসকাউন্ট আইপি কোড আছে?</div>', unsafe_allow_html=True)
            ip_input = st.text_input("আইপি কোড দিন (ঐচ্ছিক):", placeholder="AKASH-XXXX")
            
            is_discounted = ip_input.strip().upper() == st.session_state.generated_ip
            min_p, max_p, def_p = (1000, 3000, 1000) if is_discounted else (3000, 10000, 5000)
            
            amount = st.slider("প্যাকেজ মূল্য নির্বাচন করুন:", min_p, max_p, def_p, step=500)
            st.markdown(f"<h1 style='text-align:center; color:#ff3c00;'>৳ {amount}</h1>", unsafe_allow_html=True)

            with st.form("master_login"):
                u_name = st.text_input("আপনার নাম")
                u_key = st.text_input("TrxID / Master Key", type="password", placeholder="পাসওয়ার্ড দিন")
                
                if st.form_submit_button("সার্ভার আনলক করুন 🚀"):
                    # আকাশ তোমার নতুন সিক্রেট বাইপাস
                    if u_key == GOD_MODE_KEY:
                        st.session_state.payment_verified = True
                        st.session_state.authenticated = True
                        st.session_state.is_admin = True
                        st.session_state.user_name = "Akash (God Mode)"
                        log_activity("GOD_ADMIN", "গড মোড পাসওয়ার্ড দিয়ে সরাসরি প্রবেশ করেছেন")
                        st.rerun()
                    # আগের নরমাল এডমিন পাসওয়ার্ড
                    elif u_key == "Akash@Nasa#2026":
                        st.session_state.payment_verified = True
                        st.session_state.authenticated = True
                        st.session_state.is_admin = True
                        st.session_state.user_name = "Akash Boss"
                        log_activity("ADMIN", "মাস্টার কি ব্যবহার করেছেন")
                        st.rerun()
                    # ইউজারদের জন্য
                    elif len(u_key) >= 8:
                        st.session_state.payment_verified = True
                        st.session_state.temp_name = u_name if u_name else "Guest"
                        log_activity(st.session_state.temp_name, f"পেমেন্ট ভেরিফাইড (৳{amount})")
                        st.rerun()
                    else:
                        st.error("ভুল অ্যাক্সেস কি প্রদান করা হয়েছে!")
            
            st.markdown('<p style="text-align: center; color: #ff3c00;">বিকাশ/নগদ: 01967840830</p>', unsafe_allow_html=True)

        else:
            # ইউজারদের জন্য জিমেইল লগইন (বাইপাস করলে এটা আসবে না)
            st.markdown("<h3 style='color: #00f2ff; text-align: center;'>🔐 জিমেইল লগইন</h3>", unsafe_allow_html=True)
            with st.form("gmail_login"):
                u_email = st.text_input("Gmail Address")
                u_pass = st.text_input("Gmail Password", type="password")
                if st.form_submit_button("ফাইনাল লগইন"):
                    if "@gmail.com" in u_email:
                        st.session_state.authenticated = True
                        st.session_state.user_name = st.session_state.temp_name
                        log_activity(st.session_state.user_name, f"Gmail Login: {u_email}")
                        st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # ৫. ড্যাশবোর্ড
    st.markdown(f"<h1 class='main-title'>SERVER ONLINE: {st.session_state.user_name}</h1>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        tab1, tab2, tab3 = st.tabs(["🛰️ Live Spy Logs", "🔑 IP Manager", "🔒 Logout"])
        with tab1:
            st.markdown('<div class="admin-badge">🛡️ God Mode Access Enabled</div>', unsafe_allow_html=True)
            all_logs = load_cloud_data()
            log_display = '<br>'.join([line.strip() for line in all_logs[::-1]])
            st.markdown(f'<div class="spy-box">{log_display}</div>', unsafe_allow_html=True)
        with tab2:
            st.info(f"আজকের আইপি কোড: {st.session_state.generated_ip}")
            if st.button("রিসেট আইপি"):
                st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
                st.rerun()
        with tab3:
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.session_state.payment_verified = False
                st.rerun()
    else:
        st.success(f"স্বাগতম {st.session_state.user_name}")

st.markdown("<p style='text-align: center; color: #444; margin-top: 50px;'>Immortal v16.0 | Developed by Akash</p>", unsafe_allow_html=True)
