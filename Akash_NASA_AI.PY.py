import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. হাই-টেক নাসা থিম সেটআপ ---
st.set_page_config(page_title="NASA SUPREME MASTER PRO V33", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; }
    .nasa-logo { display: block; margin: auto; width: 140px; filter: drop-shadow(0 0 15px #00eaff); padding: 10px;}
    
    /* বাটন ও ইনপুট ডিজাইন */
    .stButton>button { background: linear-gradient(90deg, #00eaff, #0080ff); color: black; border-radius: 8px; font-weight: bold; width: 100%; border: none;}
    .stButton>button:hover { box-shadow: 0 0 15px #00eaff; background: linear-gradient(90deg, #0080ff, #00eaff);}
    
    /* ট্র্যাকিং প্যানেল এনিমেশন */
    .tracker-panel { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 4px solid red; padding: 25px; background: #000; 
        box-shadow: 0 0 50px red; border-radius: 15px; margin: 20px 0;
    }
    .alert-blink { color: red; font-size: 28px; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- ২. সিকিউরিটি কনফিগারেশন ---
OWNER_PASS = "Akash@Owner#2026"         
VIP_FREE_PASS = "NASA-ADMIN-FREE-2026"  
AKASH_NUMBER = "01967840830"           

if 'access' not in st.session_state: st.session_state.access = False
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0
if 'logs' not in st.session_state: st.session_state.logs = []
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786"]

# --- ৩. মেইন ইন্টারফেস ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA COMMAND CENTER V33</h1><p>Developer: Akash | Secure Access Layer</p></div>", unsafe_allow_html=True)

# --- ৪. এক্সেস কন্ট্রোল ---
if not st.session_state.access:
    # ৩ বার ভুল করলে ট্র্যাকিং সিস্টেম
    if st.session_state.failed_attempts >= 3:
        st.markdown("""
            <div class='tracker-panel'>
                <h1 class='alert-blink'>🛑 SYSTEM BREACH DETECTED 🛑</h1>
                <p>আপনার লোকেশন এবং আইপি অ্যাড্রেস নাসা সার্ভারে ট্র্যাক করা হচ্ছে।</p>
                <p>Status: <span style='color:lime'>GPS LOCKING...</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/V4NSRTs3h9XfG/giphy.gif")
        
        unlock_key = st.text_input("সিস্টেম আনলক করতে অ্যাডমিন কোড দিন:", type="password")
        if st.button("Emergency Unlock"):
            if unlock_key == OWNER_PASS:
                st.session_state.failed_attempts = 0
                st.rerun()
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💳 TrxID ভেরিফিকেশন")
        st.write(f"বিকাশ/নগদ: {AKASH_NUMBER}")
        trx = st.text_input("TrxID দিন:").strip()
        if st.button("TrxID দিয়ে প্রবেশ 🔓"):
            if trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M"), "Type": "TrxID", "Status": "Success"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error("ভুল TrxID! চেষ্টা বাকি: " + str(3-st.session_state.failed_attempts))

    with col2:
        st.subheader("👑 VIP এক্সেস")
        vip = st.text_input("VIP পাসওয়ার্ড দিন:", type="password").strip()
        if st.button("VIP প্রবেশ 🚀"):
            if vip == VIP_FREE_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M"), "Type": "VIP", "Status": "Success"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error("অবৈধ পাসওয়ার্ড!")
    st.stop()

# --- ৫. সাকসেস ড্যাশবোর্ড ---
st.success("স্বাগতম আকাশ! আপনার সিস্টেম এখন অনলাইন।")
tabs = st.tabs(["📡 নাসা ডাটা", "📝 ওয়ার্কস্পেস", "⚙️ সেটিংস"])

with tabs[0]:
    st.info("আপনার লাইসেন্স ২০২৬ সাল পর্যন্ত বৈধ।")
    st.metric("সার্ভার স্ট্যাটাস", "Running", delta="High Speed")

with tabs[1]:
    notes = st.text_area("আপনার গোপন নোটস লিখুন:", height=200)
    if st.button("Save Notes"): st.success("নোট সেভ হয়েছে!")

with tabs[2]:
    st.write("অ্যাডমিন প্যানেল")
    if st.text_input("মাস্টার পাসওয়ার্ড দিন:", type="password") == OWNER_PASS:
        st.table(pd.DataFrame(st.session_state.logs))
    
    if st.button("লগ আউট 🔒"):
        st.session_state.access = False
        st.rerun()

st.markdown("---")
st.caption("© 2026 AKASH NASA SYSTEM | SECURE ENCRYPTED")
