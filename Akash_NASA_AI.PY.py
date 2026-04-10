import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. হাই-টেক গোয়েন্দা ও নাসা ডিজাইন ---
st.set_page_config(page_title="NASA SUPREME MASTER PRO V33", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; }
    .nasa-logo { display: block; margin: auto; width: 140px; filter: drop-shadow(0 0 15px #00eaff); }
    
    .pricing-table { display: flex; justify-content: space-around; flex-wrap: wrap; margin: 20px 0; }
    .price-card { background: rgba(0, 234, 255, 0.1); border: 2px solid #00eaff; padding: 20px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 15px #00eaff; }
    .vip-card { background: rgba(255, 215, 0, 0.1); border: 2px solid #ffd700; padding: 20px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 15px #ffd700; }
    
    .stButton>button { background: linear-gradient(90deg, #00eaff, #0080ff); color: black; border-radius: 8px; font-weight: bold; width: 100%; height: 3.5em; }
    
    /* 🚨 গোয়েন্দা ও সেনাবাহিনী ট্র্যাকিং অ্যালার্ট 🚨 */
    .gov-tracking { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 5px solid red; padding: 30px; background: #0b0000; 
        box-shadow: 0 0 50px red; border-radius: 15px; 
        font-family: 'Courier New', monospace; margin-top: 20px;
    }
    .tracking-status { color: #00ff00; font-size: 18px; text-align: left; margin-left: 20%; }
    .alert-blink { color: red; font-size: 28px; animation: blinker 0.8s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- ২. সিকিউরিটি সেটিংস (আগের ডাটা) ---
OWNER_PASS = "Akash@Owner#2026"         
VIP_FREE_PASS = "NASA-ADMIN-FREE-2026"  
AKASH_NUMBER = "01967840830"           
LICENSE_PRICE = "৫০০০ টাকা"              
CHARGE_FEE = "৫০ টাকা"                 

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed' not in st.session_state: st.session_state.failed = 0
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786", "SUCCESS100"]

# --- ৩. মেইন হেডার ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA SUPREME MASTER COMMAND CENTER</h1><p>National Security Level | Dev: Akash</p></div>", unsafe_allow_html=True)

# --- ৪. গেটওয়ে সেকশন ---
if not st.session_state.access:
    # লাকি ড্র
    st.markdown("### 🎁 NASA PRIZE POOL")
    if st.button("🔥 SPIN TO WIN 10,000 TK"):
        st.balloons(); st.success("🎉 অভিনন্দন! আপনি ১০,০০০ টাকা জিতেছেন।")

    st.markdown("---")
    st.markdown(f"""<div class='pricing-table'><div class='price-card'><h3>STANDARD</h3><p>{LICENSE_PRICE}</p><p>ফি: {CHARGE_FEE}</p></div><div class='vip-card'><h3>VIP</h3><p>৫০০-২০০০ টাকা</p><p>Invitation Only</p></div></div>""", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("💳 পেমেন্ট গেটওয়ে")
        st.info(f"বিকাশ/নগদ: {AKASH_NUMBER}")
        user_trx = st.text_input("TrxID দিন:", key="trx_gate").strip()
        if st.button("TrxID দিয়ে আনলক 🔓"):
            if user_trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now(), "Type": "TrxID", "Val": user_trx})
                st.rerun()
            else:
                st.session_state.failed += 1; st.error("ভুল TrxID!")

    with col_b:
        st.subheader("👑 ভিআইপি গেটওয়ে")
        dash_pass = st.text_input("VIP পাসওয়ার্ড দিন:", type="password")
        if st.button("পাস দিয়ে সরাসরি প্রবেশ 🚀"):
            if dash_pass == VIP_FREE_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now(), "Type": "VIP_PASS", "Val": "FREE"})
                st.rerun()
            else:
                st.session_state.failed += 1; st.error("অবৈধ পাসওয়ার্ড!")

    # --- ৫. 🚨 গোয়েন্দা ও সেনাবাহিনী ট্র্যাকিং (৩ বার ভুল করলে) 🚨 ---
    if st.session_state.failed >= 3:
        st.markdown(f"""
            <div class='gov-tracking'>
                <h2 class='alert-blink'>🛑 ACCESS DENIED! 🛑</h2>
                <p>সন্দেহজনক কার্যক্রমের জন্য আপনার অ্যাকাউন্টটি লক করা হয়েছে।</p>
                <div class='tracking-status'>
                    🛰️ <b>বাংলাদেশ সেনাবাহিনী স্যাটেলাইট:</b> ট্র্যাকিং শুরু...<br>
                    🕵️ <b>গোয়েন্দা পুলিশ (DB):</b> লোকেশন আইডেন্টিফাইড!<br>
                    📡 <b>নাসা সিকিউরিটি:</b> আইপি (IP) ব্লক করা হয়েছে।
                </div>
                <p style='color: yellow; margin-top: 15px;'>আপনার বর্তমান লোকেশন নিকটস্থ থানায় পাঠানো হচ্ছে।</p>
            </div>
        """, unsafe_allow_html=True)
        # গোয়েন্দা ম্যাপ GIF
        st.image("https://media.giphy.com/media/V4NSRTs3h9XfG/giphy.gif", use_column_width=True)
    
    st.stop()

# --- ৬. মূল ড্যাশবোর্ড (আনলক হওয়ার পর) ---
tab1, tab2, tab3, tab4 = st.tabs(["📡 NASA CONTROL", "📝 AKASH WORKSPACE", "🌍 GLOBAL DATA", "⚙️ SUPER ADMIN MONITOR"])

with tab1:
    st.markdown("### 🛰️ নাসা প্রিমিয়াম কমান্ড সেন্টার (V33)")
    st.success(f"অভিনন্দন! আপনি {LICENSE_PRICE} মূল্যের লাইসেন্স ব্যবহার করছেন।")

with tab2:
    st.markdown("### 📝 আকাশের গোপন ওয়ার্কস্পেস")
    st.session_state.my_notes = st.text_area("নোটস:", value=st.session_state.my_notes, height=300)
    if st.button("সেভ করুন ✅"): st.success("সেভ হয়েছে!")

with tab3:
    st.markdown("### 🌍 গ্লোবাল ইউজার ডাটা")
    with st.form("u_form"):
        st.text_input("নাম:"); st.text_area("বার্তা:"); submit = st.form_submit_button("সার্ভারে পাঠান")

with tab4:
    # আকাশের অ্যাডমিন মনিটর
    st.subheader("⚙️ SUPER ADMIN MONITORING CENTER")
    if st.text_input("মাস্টার পাসওয়ার্ড দিন (Akash@Owner#2026):", type="password") == OWNER_PASS:
        st.write("### 📊 বিস্তারিত পেমেন্ট ও ইউজার লগ:")
        st.write(pd.DataFrame(st.session_state.logs))
        new_id = st.text_input("নতুন TrxID যোগ করুন:")
        if st.button("অ্যাড করুন"):
            st.session_state.valid_ids.append(new_id); st.success("আইডি যোগ হয়েছে।")
    elif st.button("লগ আউট"):
        st.session_state.access = False; st.rerun()

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SYSTEM | VERSION 33 PRO | DEVELOPED BY AKASH")
