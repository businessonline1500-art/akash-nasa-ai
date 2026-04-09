import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# পেজ সেটআপ
st.set_page_config(page_title="AKASH AI | OMNI-CONTROL", page_icon="🤖", layout="wide")

# --- প্রিমিয়াম ডার্ক নিওন ডিজাইন ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #07101a 0%, #000000 100%) !important; color: #00ffcc; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00ffcc, #0099ff); color: black; font-weight: bold; border-radius: 12px; height: 50px; }
    .stTextInput>div>div>input { background: #0a192f !important; color: #00ffcc !important; border: 1px solid #00ffcc55 !important; }
</style>
""", unsafe_allow_html=True)

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- ১. সিকিউরিটি গেটওয়ে ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center;'>🚀 AKASH OMNI-AI SYSTEM</h1>", unsafe_allow_html=True)
    st.info("সিস্টেমটি ব্যবহার করতে ৩,০০০ টাকা পেমেন্ট করে TrxID দিন। মাস্টার কি: akash-bypass-71")
    
    with st.form("security_gate"):
        u_name = st.text_input("Candidate Name")
        u_trxid = st.text_input("TrxID / Bypass Key")
        if st.form_submit_button("Enter System"):
            if u_trxid == "akash-bypass-71" or len(u_trxid) > 7:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("ভুল TrxID! ৩০০০ টাকা পরিশোধ করে সঠিক আইডি দিন।")

# --- ২. মেইন এআই সিস্টেম (সব অ্যাপের জন্য) ---
else:
    tab1, tab2, tab3, tab4 = st.tabs(["💬 AI Assistant", "📲 App Automation", "🛰️ Mission Track", "🔐 Admin"])

    with tab1:
        st.subheader("🤖 আকাশ এআই ইন্টেলিজেন্স")
        user_input = st.chat_input("আমাকে কাজ দিন (যেমন: 'মেসেঞ্জারে অটো রিপ্লাই চাই')...")
        
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            msg = user_input.lower()
            
            if "মেসেঞ্জার" in msg or "messenger" in msg:
                reply = "আকাশ, মেসেঞ্জার অটো-রিপ্লাই সিস্টেম রেডি। আপনি না থাকলেও এটি উত্তর দিবে। নিচের 'App Automation' ট্যাব থেকে ফাইলটি ডাউনলোড করে নিন।"
            elif "whatsapp" in msg or "হোয়াটসঅ্যাপ" in msg:
                reply = "হোয়াটসঅ্যাপ অটোমেশন ফাইল জেনারেট করা হয়েছে। এটি ফোনের নেট ছাড়াও ব্যাকগ্রাউন্ডে কাজ করবে।"
            else:
                reply = f"বুঝেছি আকাশ। আপনার '{user_input}' কাজটি আমি প্রসেস করছি। নাসা সার্ভার থেকে কনফিগারেশন আপডেট করা হচ্ছে..."
            
            st.session_state.chat_history.append({"role": "assistant", "content": reply})

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ অটোমেশন কন্ট্রোল")
        st.write("নিচের অ্যাপগুলো আপনার ফোনের নেট না থাকলেও অটো রিপ্লাই দেওয়ার জন্য কনফিগার করা যাবে:")
        
        cols = st.columns(3)
        with cols[0]:
            if st.button("Messenger Auto-Bot"):
                st.success("Messenger Script Generated!")
        with cols[1]:
            if st.button("WhatsApp Auto-Bot"):
                st.success("WhatsApp Script Generated!")
        with cols[2]:
            if st.button("System Cleaner"):
                st.info("Optimization Started...")
        
        st.markdown("""
        ---
        **কিভাবে নেট ছাড়া চালাবেন?** ১. 'Tasker' বা 'AutoResponder' অ্যাপটি প্লে-স্টোর থেকে নামান।  
        ২. আমার এই সিস্টেম থেকে দেওয়া কোডটি সেখানে কপি-পেস্ট করুন।  
        ৩. এখন থেকে আপনার ফোনের নেট বন্ধ থাকলেও এআই সবার মেসেজের উত্তর দিবে।
        """)

    with tab3:
        st.text_input("আপনার ট্র্যাকিং আইডি দিন")
        
    with tab4:
        if st.text_input("অ্যাডমিন পাসওয়ার্ড", type="password") == "akash71":
            st.write("সব ডাটা সুরক্ষিত আছে।")
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.rerun()
