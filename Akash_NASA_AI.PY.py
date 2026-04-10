import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. নাসা SUPREME ডিজাইন ও হাই-টেক ইন্টারফেস ---
st.set_page_config(page_title="NASA SUPREME MASTER PRO V33", layout="wide")

st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    
    /* হেডার ও লোগো */
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; }
    .nasa-logo { display: block; margin: auto; width: 140px; filter: drop-shadow(0 0 15px #00eaff); }
    
    /* প্রাইসিং কার্ড */
    .pricing-table { display: flex; justify-content: space-around; flex-wrap: wrap; margin: 20px 0; }
    .price-card { background: rgba(0, 234, 255, 0.1); border: 2px solid #00eaff; padding: 20px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 15px #00eaff; }
    .vip-card { background: rgba(255, 215, 0, 0.1); border: 2px solid #ffd700; padding: 20px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 15px #ffd700; }
    
    /* বাটন */
    .stButton>button { background: linear-gradient(90deg, #00eaff, #0080ff); color: black; border-radius: 8px; font-weight: bold; width: 100%; height: 3.5em; }
    
    /* 🚨 হাই-টেক গোয়েন্দা ট্র্যাকিং প্যানেল 🚨 */
    .tracker-panel { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 5px solid red; padding: 30px; background: #010101; 
        box-shadow: 0 0 50px red; border-radius: 20px; 
        font-family: 'Courier New', monospace; margin: 20px 0;
    }
    .track-metrics { 
        display: flex; justify-content: space-around; margin-top: 15px;
        background: rgba(255, 0, 0, 0.1); padding: 10px; border-radius: 10px;
    }
    .metric-text { color: lime; text-shadow: 0 0 5px lime; }
    .alert-blink { color: red; font-size: 30px; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    /* অ্যাডমিন মনিটর স্টাইল */
    .admin-stats { background: rgba(0, 255, 0, 0.1); border: 1px solid lime; border-radius: 10px; padding: 15px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ২. সিকিউরিটি ও ডাটা সেটিংস ---
OWNER_PASS = "Akash@Owner#2026"         
VIP_FREE_PASS = "NASA-ADMIN-FREE-2026"  
AKASH_NUMBER = "01967840830"           
LICENSE_PRICE = "৫০০০ টাকা"              
CHARGE_FEE = "৫০ টাকা"                 

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786", "SUCCESS100"]

# --- ৩. মেইন হেডার ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA SUPREME MASTER COMMAND CENTER</h1><p>Global Intelligence Network | Dev: Akash</p></div>", unsafe_allow_html=True)

# --- ৪. গেটওয়ে সেকশন (পেমেন্ট ও ট্র্যাকিং গেটওয়ে) ---
if not st.session_state.access:
    
    # 🚨 হাই-টেক গোয়েন্দা ট্র্যাকিং (৩ বার ভুল করলে) 🚨
    if st.session_state.failed_attempts >= 3:
        st.markdown(f"""
            <div class='tracker-panel'>
                <h1 class='alert-blink'>🛑 LOCATION LOCKED! 🛑</h1>
                <p>বারবার ভুল তথ্য দেওয়ায় আপনার সিস্টেমটি গোয়েন্দা জালে আটকা পড়েছে।</p>
                <p>নাসা স্যাটেলাইট এবং গোয়েন্দা পুলিশ আপনার মোবাইল/পিসি ট্র্যাকিং করছে।</p>
                <div class='track-metrics'>
                    <div style='text-align: left;'>
                        🛰️ Status: <b class='metric-text'>LIVE TRACKING</b><br>
                        🕵️ Agency: <b class='metric-text'>BD Army + CID</b>
                    </div>
                    <div style='text-align: right;'>
                        座標 Location: <b class='metric-text'>FETCHING COORDINATES...</b><br>
                        📡 Device ID: <b class='metric-text'>LOCKED ON DEVICE</b>
                    </div>
                </div>
                <p style='color: yellow; margin-top: 15px;'>আপনার বর্তমান ডাটা এবং লোকেশন নিকটস্থ থানায় পাঠানো হচ্ছে।</p>
            </div>
        """, unsafe_allow_html=True)
        # একটি হ্যাকিং ম্যাপের GIF যোগ করা হয়েছে
        st.image("https://media.giphy.com/media/V4NSRTs3h9XfG/giphy.gif", use_column_width=True)
        
        # অ্যাডমিন পাসওয়ার্ড দিয়ে ইউজারকে বাঁচানো
        admin_unlock = st.text_input("সিস্টেম আনলক করতে অ্যাডমিন পাসওয়ার্ড দিন (শুধুমাত্র অ্যাডমিন):", type="password", key="admin_save")
        if st.button("ইউজারকে আনলক করুন"):
            if admin_unlock == OWNER_PASS:
                st.session_state.failed_attempts = 0
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "Admin Reset", "Val": "User Saved", "IP": "Admin Reset"})
                st.rerun()
            else:
                st.error("ভুল অ্যাডমিন পাসওয়ার্ড!")
        st.stop() # আনলক না হওয়া পর্যন্ত নিচে যাবে না

    # লাকি ড্র
    st.markdown("### 🎁 NASA PRIZE POOL")
    if st.button("🔥 SPIN TO WIN 10,000 TK"):
        st.balloons(); st.success("🎉 ১০,০০০ টাকা জিতেছেন! পুরস্কার ক্লেইম করতে নিচে আনলক করুন।")
    
    st.markdown("---")
    st.markdown(f"""<div class='pricing-table'><div class='price-card'><h3>STANDARD</h3><p>{LICENSE_PRICE}</p><p>ফি: {CHARGE_FEE}</p></div><div class='vip-card'><h3>VIP</h3><p>৫০০-২০০০ টাকা</p><p>Invitation Only</p></div></div>""", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("💳 পেমেন্ট গেটওয়ে")
        st.info(f"বিকাশ/নগদ: {AKASH_NUMBER}")
        user_trx = st.text_input("TrxID কোডটি দিন:", key="trx_gate", placeholder="Ex: 8M29X7PQ").strip()
        if st.button("TrxID দিয়ে আনলক 🔓"):
            if user_trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "TrxID", "Val": user_trx, "IP": "User IP Tracked"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1; st.error("❌ ভুল TrxID!")

    with col_b:
        st.subheader("👑 ভিআইপি গেটওয়ে")
        dash_pass = st.text_input("VIP ড্যাশবোর্ড পাস দিন:", type="password", placeholder="গোপন পাসওয়ার্ড")
        if st.button("পাস দিয়ে সরাসরি প্রবেশ 🚀"):
            if dash_pass == VIP_FREE_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "VIP Pass", "Val": "FREE_ACCESS", "IP": "Admin IP Tracked"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1; st.error("❌ অবৈধ ভিআইপি পাসওয়ার্ড!")

    st.stop()

# --- ৫. মূল ড্যাশবোর্ড (আনলক হওয়ার পর) ---
tab1, tab2, tab3, tab4 = st.tabs(["📡 NASA COMMAND", "📝 WORKSPACE", "🌍 DATA", "⚙️ MONITOR"])

with tab1:
    st.markdown("### 🛰️ নাসা কমান্ড সেন্টার সক্রিয়")
    st.success(f"অভিনন্দন আকাশ জান! আপনার {LICENSE_PRICE} মূল্যের লাইসেন্স attivo।")

with tab2:
    st.markdown("### 📝 আকাশের গোপন ওয়ার্কস্পেস")
    st.session_state.my_notes = st.text_area("আপনার নোটস:", value=st.session_state.my_notes, height=300)
    if st.button("সেভ করুন ✅"): st.success("সংরক্ষিত হয়েছে!")

with tab3:
    st.markdown("### 🌍 গ্লোবাল ইউজার ডাটা")
    with st.form("u_form"):
        st.text_input("নাম:"); st.text_area("বার্তা:"); submit = st.form_submit_button("সার্ভারে পাঠান")
        if submit: st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "User Message", "Val": "Received", "IP": "Message Sent"})

with tab4:
    # --- আকাশের জন্য বিশেষ মনিটরিং সেন্টার ---
    st.subheader("⚙️ SUPER ADMIN MONITORING CENTER")
    admin_key = st.text_input("আপনার গোপন মালিকানা পাসওয়ার্ড দিন (Akash@Owner#2026):", type="password")
    
    if admin_key == OWNER_PASS:
        st.markdown("<div class='admin-stats'>✅ স্বাগতম আকাশ জান! আপনার সার্ভারের বর্তমান অবস্থা নিচে দেওয়া হলো।</div>", unsafe_allow_html=True)
        
        # ডাটাবেজ সামারি
        col1, col2, col3 = st.columns(3)
        col1.metric("মোট লগ (Log Entries)", len(st.session_state.logs))
        col2.metric("ভুল চেষ্টা (Failed)", st.session_state.failed_attempts)
        col3.metric("TrxID ডাটাবেজ", len(st.session_state.valid_ids))

        st.markdown("### 📊 বিস্তারিত ইউজার অ্যাক্টিভিটি")
        if st.session_state.logs:
            df = pd.DataFrame(st.session_state.logs)
            st.table(df) # এখানে সব ডিটেইলস দেখা যাবে
        else:
            st.info("এখনো কোনো অ্যাক্টিভিটি রেকর্ড হয়নি।")

        st.markdown("---")
        st.subheader("🛠️ সার্ভার কন্ট্রোল")
        new_id = st.text_input("নতুন পেমেন্ট কোড (TrxID) যোগ করুন:")
        if st.button("কোড সেভ করুন"):
            st.session_state.valid_ids.append(new_id)
            st.success("আইডি যোগ হয়েছে।")
    elif admin_key != "":
        st.error("🚨 ভুল পাসওয়ার্ড! এই জায়গাটি শুধুমাত্র আকাশের জন্য।")

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SYSTEM | VERSION 33 PRO | ENCRYPTED | DEVELOPED BY AKASH")
