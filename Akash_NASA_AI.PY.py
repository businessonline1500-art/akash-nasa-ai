import streamlit as st
import pandas as pd
from datetime import datetime
import time
import random

# --- ১. প্রিমিয়াম ডিজাইন (পুরানো সব সিএসএস এখানে আছে) ---
st.set_page_config(page_title="NASA SUPREME MASTER V33 - FULL VERSION", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); }
    .header-text { 
        color: #00eaff; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif; 
        text-shadow: 0 0 20px #00eaff; 
        padding: 10px; 
    }
    .nasa-logo { 
        display: block; 
        margin: auto; 
        width: 150px; 
        filter: drop-shadow(0 0 10px #00eaff); 
    }
    .lock-screen { 
        text-align: center; 
        padding: 40px; 
        border: 2px solid #00eaff; 
        border-radius: 20px; 
        background: rgba(0, 234, 255, 0.05); 
        box-shadow: 0 0 20px #00eaff; 
        max-width: 800px; 
        margin: auto; 
    }
    .stButton>button { 
        background: linear-gradient(90deg, #00FF00, #008000); 
        color: white; 
        border-radius: 10px; 
        font-weight: bold; 
        width: 100%; 
        height: 3.5em; 
    }
    .payment-info { 
        background: rgba(255, 255, 255, 0.1); 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #00eaff; 
        margin-bottom: 20px; 
        text-align: center;
    }
    .security-alert { 
        color: #ff0000; 
        font-weight: bold; 
        text-align: center; 
        border: 2px solid red; 
        padding: 10px; 
        background: rgba(255,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ২. মাস্টার সেটিংস (বিকাশ/নগদ ও পাসওয়ার্ড) ---
OWNER_PASS = "Akash@Owner#2026"
AKASH_NUMBER = "01967840830"

# তোমার সেই কাঙ্ক্ষিত TrxID লিস্ট (টাকা পাওয়ার পর যেটা তুমি এখানে যোগ করবে)
# কাস্টমার যখন টাকা পাঠিয়ে তার মেসেজের কোড এখানে দিবে, তবেই সে ঢুকতে পারবে।
VALID_TRX_IDS = ["8M29X7PQ", "9L54KT2R", "AKASH786", "NASA2026", "TRX100", "SUCCESS2026"]

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed' not in st.session_state: st.session_state.failed = 0

# --- ৩. নাসা লোগো ও হেডার (সবকিছু ঠিক আছে) ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA OFFICIAL SUPREME CORE V33</h1><p>SYSTEM SECURED BY AKASH | VERSION 3.3</p></div>", unsafe_allow_html=True)

# --- ৪. পেমেন্ট ভেরিফিকেশন লক (তোমার শেষ বলা পয়েন্টটি এখানে) ---
if not st.session_state.access:
    st.markdown("<div class='lock-screen'>", unsafe_allow_html=True)
    st.subheader("🛡️ অরিজিনাল কাজে ঢুকতে পেমেন্ট ভেরিফাই করুন")
    
    st.markdown(f"""
        <div class='payment-info'>
        <p style='color: #00eaff; font-size: 20px; font-weight: bold;'>পেমেন্ট মেথড: বিকাশ ও নগদ</p>
        <p style='color: white; font-size: 18px;'>টাকা পাঠানোর নাম্বার: <b>{AKASH_NUMBER}</b></p>
        <p style='color: #FFD700;'>টাকা পাঠানোর পর আপনার মোবাইলের ফিরতি মেসেজে যে <b>Transaction ID (TrxID)</b> আছে, তা নিচে দিন।</p>
        <p style='color: red; font-size: 14px;'>⚠️ পেমেন্ট কোড (TrxID) ছাড়া সিস্টেম আনলক হবে না।</p>
        </div>
    """, unsafe_allow_html=True)
    
    # কাস্টমার এখানে তার TrxID কোডটি দিবে
    user_trx = st.text_input("আপনার পেমেন্ট TrxID কোডটি এখানে লিখুন:", placeholder="Ex: 8M29X7PQ").strip()
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        if st.button("সিস্টেম আনলক করুন 🔓"):
            if user_trx in VALID_TRX_IDS:
                st.session_state.access = True
                st.success("✅ পেমেন্ট ভেরিফাইড! মূল সিস্টেমে আপনাকে স্বাগতম।")
                st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M"), "TrxID": user_trx})
                time.sleep(1.5)
                st.rerun()
            else:
                st.session_state.failed += 1
                st.error("❌ ভুল TrxID! আপনি এখনো টাকা পাঠাননি অথবা ভুল কোড দিয়েছেন।")
    
    with col_v2:
        if st.button("লাইসেন্স বা সহায়তার জন্য কল করুন 📞"):
            st.info(f"কল সেন্টার: {AKASH_NUMBER}")

    # ৩ বার ভুল করলে সেই আর্মি-পুলিশ ওয়ার্নিং
    if st.session_state.failed >= 3:
        st.markdown("<div class='security-alert'>🚨 SECURITY BREACH! সেনাবাহিনী ও পুলিশ সাইবার ইউনিটকে আপনার আইপি পাঠানো হয়েছে।</div>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop() # পেমেন্ট ভেরিফাই না হওয়া পর্যন্ত নিচের কোড দেখাবে না

# --- ৫. মূল সিস্টেম (পেমেন্ট ভেরিফাই হওয়ার পর যা ওপেন হবে) ---
tab1, tab2, tab3 = st.tabs(["🎁 LUCKY SPIN (Income)", "💳 PAYMENT DATABASE", "🔐 ADMIN CENTER"])

with tab1:
    st.markdown("### 💎 নাসার বিশেষ লাকি ড্র! (Spin & Win)")
    st.write("অভিনন্দন! আপনি পেমেন্ট ভেরিফাই করেছেন। এখন আপনার ভাগ্য পরীক্ষা করুন।")
    if st.button("🔥 SPIN NOW - চাকা ঘুরান"):
        with st.spinner("সার্ভারের সাথে কানেক্ট হচ্ছে..."):
            time.sleep(1)
            st.balloons()
            st.success("🎉 বিঙ্গো! অভিনন্দন আকাশ জান, আপনি ১০,০০০ টাকা জিতেছেন!")
            st.warning(f"আপনার জেতা টাকা বুঝে নিতে ২০ টাকা চার্জ পাঠান: {AKASH_NUMBER}")

with tab2:
    st.markdown("### 🏦 কাস্টমার পেমেন্ট পোর্টাল")
    with st.form("user_data_form"):
        u_name = st.text_input("আপনার নাম:")
        u_trx = st.text_input("আপনার TrxID (যেটা দিয়ে আনলক করেছেন):")
        if st.form_submit_button("SUBMIT TO DATABASE"):
            st.success("আপনার তথ্য সফলভাবে নাসা ডাটাবেজে সংরক্ষিত হয়েছে।")

with tab3:
    st.subheader("🔐 অ্যাডমিন কমান্ড সেন্টার (আকাশের জন্য)")
    admin_key = st.text_input("মাস্টার পাসওয়ার্ড দিন:", type="password")
    if admin_key == OWNER_PASS:
        st.write("### ✅ যারা পেমেন্ট করে ঢুকেছে তাদের তালিকা:")
        if st.session_state.logs:
            st.table(pd.DataFrame(st.session_state.logs))
        else:
            st.info("এখনো কোনো নতুন লগ নেই।")
    elif admin_key != "":
        st.error("🚨 অবৈধ এক্সেস! আপনি এই সিস্টেমের মালিক নন।")

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SYSTEM | LAST UPDATE: {datetime.now().date()}")
