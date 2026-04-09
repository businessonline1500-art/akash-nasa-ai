n   import streamlit as st
import pandas as pd
from datetime import datetime

# পেজ কনফিগারেশন
st.set_page_config(
    page_title="NASA x AKASH AI | Internal Control", 
    page_icon="🚀", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- প্রিমিয়াম রেসপনসিভ ডিজাইন (NASA Red & Blue) ---
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #0b3d91 0%, #000000 100%) !important;
        color: #ffffff !important;
    }
    .header-box { text-align: center; margin-bottom: 20px; padding: 10px; }
    .nasa-logo { 
        font-size: clamp(40px, 10vw, 60px); font-weight: 900; 
        color: #fc3d21; text-shadow: 0 0 15px #fc3d21; letter-spacing: 5px;
    }
    .akash-ai { 
        font-size: clamp(16px, 4vw, 25px); font-weight: 300; 
        color: #ffffff; text-transform: uppercase; letter-spacing: 5px;
    }
    .price-box {
        background: rgba(255, 255, 255, 0.05); border: 2px solid #fc3d2133;
        border-radius: 15px; padding: 15px; text-align: center; margin-bottom: 10px;
    }
    .stButton>button {
        width: 100% !important; background: linear-gradient(90deg, #fc3d21, #b92b27) !important;
        color: white !important; font-weight: bold !important; font-size: 18px !important;
        border-radius: 12px !important; height: 60px !important; 
        box-shadow: 0 5px 15px rgba(252, 61, 33, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

if 'database' not in st.session_state:
    st.session_state.database = []

# --- হেডার ---
st.markdown("""
<div class="header-box">
    <div class="nasa-logo">NASA</div>
    <div class="akash-ai">AKASH AI SYSTEM</div>
    <div style='color:#81d4fa; font-size:11px; margin-top:5px;'>MISSION CONTROL: BYPASS ENABLED v5.0</div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 Mission", "🛰️ Track", "🔐 Admin"])

with tab1:
    st.markdown("### 💠 Protocol Selection")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='price-box' style='border-left: 5px solid #fc3d21;'>New: <b>৳ ৩,০০০</b></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='price-box' style='border-left: 5px solid #0b3d91;'>Update: <b>৳ ৩,০০০-১০,০০০</b></div>", unsafe_allow_html=True)

    with st.form("main_form"):
        u_name = st.text_input("Full Name")
        u_phone = st.text_input("Mobile Number")
        u_type = st.selectbox("Mission Type", ["New Launch (3000 BDT)", "System Upgrade"])
        u_amount = 3000 if "New" in u_type else st.slider("Select Budget (BDT)", 3000, 10000, 5000, step=500)
        
        st.write(f"**Total Allocation: {u_amount} BDT**")
        u_method = st.selectbox("Gateway", ["bKash (01967840830)", "Nagad (01967840830)"])
        u_trxid = st.text_input("TrxID (Transaction ID)")
        
        if st.form_submit_button("Launch Mission"):
            # --- VIP MASTER BYPASS SYSTEM ---
            if u_trxid == "akash-bypass-71": # এটি আপনার গোপন কোড
                st.balloons()
                st.success(f"Welcome Akash! System unlocked via Master Key. No payment required.")
            elif u_name and u_phone and u_trxid:
                st.session_state.database.append({
                    "Date": datetime.now().strftime("%I:%M %p"),
                    "Name": u_name, "Phone": u_phone, "Amount": u_amount, "TrxID": u_trxid, "Status": "VERIFYING"
                })
                st.balloons()
                st.success("Mission Initialized! Thank you.")
            else:
                st.error("Fill all fields!")

with tab2:
    st.markdown("### 🛰️ Live Tracking")
    check_id = st.text_input("Enter TrxID")
    if st.button("Query Status"):
        if check_id == "akash-bypass-71":
            st.warning("Master Key used. Access: UNLIMITED.")
        else:
            found = False
            for entry in st.session_state.database:
                if entry['TrxID'] == check_id:
                    st.info(f"**Status:** {entry['Status']}")
                    found = True
            if not found and check_id:
                st.error("Not found.")

with tab3:
    st.markdown("### 🔐 Admin Terminal")
    access = st.text_input("Access Key", type="password")
    if access == "akash71":
        if st.session_state.database:
            st.dataframe(pd.DataFrame(st.session_state.database))
            total = sum(d['Amount'] for d in st.session_state.database)
            st.metric("Total Collected", f"৳ {total}")
        else:
            st.write("No missions logged.")
