import streamlit as st
import random
import string
import datetime

# ১. পেজ সেটআপ (AKASH NASA AI SERVER - ENCRYPTED ACCESS)
st.set_page_config(page_title="AKASH NASA AI SERVER | MASTER MONITOR", page_icon="📡", layout="wide")

# ২. প্রিমিয়াম ডিজাইন ও সাইবার স্টাইল
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #001d3d 0%, #000000 100%) !important; color: #ffffff; font-family: 'Rajdhani', sans-serif; }
    .main-title { color: #ff3c00; text-align: center; font-family: 'Orbitron', sans-serif; font-size: 50px; text-shadow: 0 0 25px rgba(255, 60, 0, 0.7); }
    .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(25px); padding: 35px; border-radius: 30px; border: 1px solid rgba(255, 60, 0, 0.3); }
    .spy-box { background: rgba(0, 0, 0, 0.7); border: 1px solid #00f2ff; padding: 20px; border-radius: 15px; font-family: 'Courier New', monospace; color: #00f2ff; height: 350px; overflow-y: scroll; box-shadow: inset 0 0 15px #00f2ff; }
    .admin-indicator { color: #ffcc00; font-weight: bold; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; text-align: center; display: block; }
</style>
""", unsafe_allow_html=True)

# ৩. ডাটাবেস ও সিকিউরিটি কনফিগারেশন
if 'generated_ip' not in st.session_state:
    st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
if 'user_logs' not in st.session_state:
    st.session_state.user_logs = [] 
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# তোমার নতুন স্পেশাল কোডড পাসওয়ার্ড
MASTER_ADMIN_KEY = "Akash@Nasa#2026"

def log_activity(user, action):
    now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    entry = f"🚀 [{now}] {user} >> {action}"
    st.session_state.user_logs.append(entry)

def speak_text(text):
    if text:
        js_code = f"<script>var msg = new SpeechSynthesisUtterance('{text}'); msg.lang = 'bn-BD'; window.speechSynthesis.speak(msg);</script>"
        st.components.v1.html(js_code, height=0)

# ৪. লগইন ইন্টারফেস
if not st.session_state.authenticated:
    st.markdown(f'<div style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="150"><h1 class="main-title">AKASH NASA AI SERVER</h1></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00f2ff; text-align: center;'>🔐 অ্যাক্সেস প্রোটোকল</h3>", unsafe_allow_html=True)
        
        ip_input = st.text_input("IP Code (ডিসকাউন্টের জন্য):", placeholder="গোপন কোড দিন")
        
        is_discounted = ip_input.strip().upper() == st.session_state.generated_ip
        min_p, max_p, def_p = (1000, 3000, 1000) if is_discounted else (3000, 10000, 5000)
        
        amount = st.slider("অ্যামাউন্ট নির্বাচন করুন:", min_p, max_p, def_p, step=500)
        st.markdown(f"<h1 style='text-align:center; color:#ff3c00;'>৳ {amount}</h1>", unsafe_allow_html=True)

        with st.form("main_login"):
            u_name = st.text_input("নাম", placeholder="আপনার নাম")
            u_trxid = st.text_input("TrxID / Master Key", type="password", placeholder="পাসওয়ার্ড বা TrxID")
            
            if st.form_submit_button("ভেরিফাই এবং এন্টার সার্ভার 🚀"):
                # নতুন কোডিং করা এডমিন পাসওয়ার্ড চেক
                if u_trxid == MASTER_ADMIN_KEY:
                    st.session_state.authenticated = True
                    st.session_state.is_admin = True
                    st.session_state.user_name = "Akash Boss"
                    log_activity("SUPER ADMIN", "এনক্রিপ্টেড কি ব্যবহার করে প্রবেশ করেছেন")
                    st.rerun()
                elif u_trxid == "akash-bypass-71" or len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "User"
                    log_activity(st.session_state.user_name, f"সার্ভারে ঢুকেছেন (৳{amount})")
                    speak_text(f"স্বাগতম {st.session_state.user_name}")
                    st.rerun()
                else:
                    st.error("ভুল সিকিউরিটি কি!")
        
        st.markdown("""<div style="background: rgba(255,60,0,0.1); padding: 10px; border-radius: 10px; border: 1px solid #ff3c00; margin-top: 15px; text-align: center;">
            <p style="margin:0; font-size: 14px;">বিকাশ ও নগদ: <b>01967840830</b></p>
        </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # ৫. মেইন ড্যাশবোর্ড
    st.markdown(f"<h1 class='main-title'>SERVER ONLINE: {st.session_state.user_name}</h1>", unsafe_allow_html=True)
    
    if st.session_state.is_admin:
        st.markdown("<span class='admin-indicator'>● SUPER ADMIN SECURE ACCESS ACTIVE</span>", unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["🕵️‍♂️ Live Spy Monitor", "🔑 IP Manager", "🛑 System Logout"])
        
        with tab1:
            st.subheader("📡 লাইভ ট্র্যাকিং ডাটাবেস")
            log_display = '<br>'.join(st.session_state.user_logs[::-1])
            st.markdown(f'<div class="spy-box">{log_display}</div>', unsafe_allow_html=True)
            if st.button("ক্লিয়ার ডাটা"):
                st.session_state.user_logs = []
                st.rerun()
        
        with tab2:
            st.info(f"আজকের সিক্রেট আইপি: {st.session_state.generated_ip}")
            if st.button("অটো-আইপি রিসেট করুন"):
                st.session_state.generated_ip = f"AKASH-{random.randint(1000, 9999)}"
                st.rerun()
                
        with tab3:
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.rerun()
    else:
        st.success(f"হ্যালো {st.session_state.user_name}, আপনি সার্ভার ব্যবহারের অনুমতি পেয়েছেন।")
        user_cmd = st.chat_input("সিস্টেম কমান্ড দিন...")
        if user_cmd:
            log_activity(st.session_state.user_name, f"কমান্ড: {user_cmd}")
            st.info("আপনার অনুরোধ প্রসেস করা হচ্ছে...")

st.markdown("<p style='text-align: center; color: #555; margin-top: 40px;'>Developer: Akash | v12.0 Encrypted Edition</p>", unsafe_allow_html=True)
