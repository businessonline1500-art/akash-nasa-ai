import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. অল-ডিভাইস হাই-টেক নাসা ডিজাইন ---
st.set_page_config(page_title="NASA SUPREME MASTER PRO V33", layout="wide")

st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    
    /* হেডার ও লোগো */
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; margin-bottom: 20px;}
    .nasa-logo { display: block; margin: auto; width: 140px; filter: drop-shadow(0 0 15px #00eaff); padding: 10px;}
    
    /* প্রাইসিং ও ভিআইপি কার্ড */
    .pricing-table { display: flex; justify-content: space-around; flex-wrap: wrap; margin: 20px 0; }
    .price-card { background: rgba(0, 234, 255, 0.1); border: 2px solid #00eaff; padding: 25px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 20px #00eaff; }
    .vip-card { background: rgba(255, 215, 0, 0.1); border: 2px solid #ffd700; padding: 25px; border-radius: 15px; width: 45%; text-align: center; box-shadow: 0 0 20px #ffd700; }
    
    /* বাটন ও ইনপুট বক্স */
    .stButton>button { background: linear-gradient(90deg, #00eaff, #0080ff); color: black; border-radius: 8px; font-weight: bold; width: 100%; height: 3.5em; border: none;}
    .stButton>button:hover { box-shadow: 0 0 15px #00eaff; background: linear-gradient(90deg, #0080ff, #00eaff);}
    
    /* পাসওয়ার্ড ইনপুট বক্সের জন্য বিশেষ স্টাইল (অটো-ফিল সমস্যা দূর করতে) */
    .pass-input { border: 2px solid #ffd700 !important; background-color: rgba(255, 215, 0, 0.1) !important; color: white !important; font-size: 18px !important; padding: 10px !important; }

    /* 🚨 হাই-টেক ট্র্যাকিং প্যানেল (ভুল ট্রাই করলে) 🚨 */
    .tracker-panel { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 5px solid red; padding: 30px; background: #010101; 
        box-shadow: 0 0 60px red; border-radius: 20px; 
        font-family: 'Courier New', monospace; margin: 20px 0;
    }
    .track-metrics { 
        display: flex; justify-content: space-around; margin-top: 20px;
        background: rgba(255, 0, 0, 0.15); padding: 15px; border-radius: 10px; border: 1px solid red;
    }
    .metric-text { color: lime; text-shadow: 0 0 5px lime; font-weight: bold; }
    .alert-blink { color: red; font-size: 32px; animation: blinker 1s linear infinite; font-weight: 900;}
    @keyframes blinker { 50% { opacity: 0; } }
    
    /* অ্যাডমিন মনিটর স্টাইল */
    .admin-monitor-card { background: rgba(0, 255, 0, 0.05); border: 1px solid lime; border-radius: 12px; padding: 20px; margin-top: 15px; box-shadow: 0 0 15px lime; }
    </style>
    """, unsafe_allow_html=True)

# --- ২. সিকিউরিটি ও ডাটা সেটিংস (তোমার সব তথ্য) ---
OWNER_PASS = "Akash@Owner#2026"         # তোমার অ্যাডমিন প্যানেল পাসওয়ার্ড
VIP_FREE_PASS = "NASA-ADMIN-FREE-2026"  # ভিআইপি বড় পাসওয়ার্ড (টাকা ছাড়া প্রবেশের জন্য)
AKASH_NUMBER = "01967840830"           # তোমার বিকাশ/নগদ নাম্বার
LICENSE_PRICE = "৫০০০ টাকা"              # সফটওয়্যার স্ট্যান্ডার্ড দাম
CHARGE_FEE = "৫০ টাকা"                 # ভেরিফিকেশন চার্জ
VIP_PRICE_RANGE = "৫০০ - ২০০০ টাকা"      # ভিআইপি রেঞ্জ

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    # ডিফল্ট কিছু বৈধ TrxID
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786", "SUCCESS100"]

# --- ৩. মেইন হেডার ও লোগো ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA SUPREME MASTER COMMAND CENTER</h1><p>Global Intelligence Network | Official Security Layer | Dev: Akash</p></div>", unsafe_allow_html=True)

# --- ৪. গেটওয়ে সেকশন (পেমেন্ট ও ৩ বার ভুলের ট্র্যাকিং সিস্টেম) ---
if not st.session_state.access:
    
    # 🚨 হাই-টেক গোয়েন্দা ট্র্যাকিং ড্যাশবোর্ড (৩ বার ভুল করলে আসবে) 🚨
    if st.session_state.failed_attempts >= 3:
        st.markdown(f"""
            <div class='tracker-panel'>
                <h1 class='alert-blink'>🛑 LOCATION LOCKED! 🛑</h1>
                <p>বারবার ভুল তথ্য দেওয়ায় আপনার সিস্টেমটি গোয়েন্দা জালে আটকা পড়েছে।</p>
                <p>নাসা স্যাটেলাইট, CID এবং গোয়েন্দা পুলিশ আপনার মোবাইল/পিসি ট্র্যাকিং শুরু করেছে।</p>
                <div class='track-metrics'>
                    <div style='text-align: left;'>
                        🛰️ Status: <b class='metric-text'>LIVE TRACKING</b><br>
                        🕵️ Agency: <b class='metric-text'>BD Army + Intelligence Agency</b>
                    </div>
                    <div style='text-align: right;'>
                        座標 Location: <b class='metric-text'>FETCHING LIVE GPS COORDINATES...</b><br>
                        📡 Device ID: <b class='metric-text'>LOCKED ON DEVICE</b>
                    </div>
                </div>
                <p style='color: yellow; margin-top: 15px;'>আপনার বর্তমান ডাটা এবং আইপি (IP) নিকটস্থ থানায় পাঠানো হচ্ছে।</p>
            </div>
        """, unsafe_allow_html=True)
        
        # ট্র্যাকিং ম্যাপের GIF (তোমার ছবি অনুযায়ী)
        st.image("https://media.giphy.com/media/V4NSRTs3h9XfG/giphy.gif", use_column_width=True)
        
        # ইউজারকে ভয় দেখিয়ে অ্যাডমিন পাসওয়ার্ড দিয়ে আনলক করার অপশন
        admin_unlock = st.text_input("সিস্টেম আনলক করতে মাস্টার পাসওয়ার্ড দিন (শুধুমাত্র অ্যাডমিন):", type="password", key="admin_save_input", placeholder="অ্যাডমিন পাসওয়ার্ড")
        col_reset_1, col_reset_2 = st.columns([1,1])
        with col_reset_1:
            if st.button("ইউজারকে আনলক করুন"):
                if admin_unlock == OWNER_PASS:
                    st.session_state.failed_attempts = 0
                    st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "Admin Reset", "Val": "User Restored", "Status": "Success"})
                    st.success("ব্যবহারকারীকে সফলভাবে আনলক করা হয়েছে।")
                    time.sleep(1); st.rerun()
                else:
                    st.error("ভুল অ্যাডমিন পাসওয়ার্ড!")
        st.stop() # আনলক না হওয়া পর্যন্ত নিচে যাবে না

    # লাকি ড্র (সবার আগে)
    st.markdown("### 🎁 NASA PRIZE POOL")
    st.info("সিস্টেমে ঢোকার আগে SPIN করে পুরস্কার জিতে নিন!")
    if st.button("🔥 SPIN TO WIN 10,000 TK"):
        st.balloons(); st.success("🎉 অভিনন্দন! আপনি ১০,০০০ টাকা জিতেছেন! পুরস্কার ক্লেইম করতে নিচে আনলক করুন।")
    
    st.markdown("---")
    
    # প্রাইসিং ও ভিআইপি কার্ড
    st.markdown(f"""
    <div class='pricing-table'>
        <div class='price-card'>
            <h3 style='color:#00eaff;'>STANDARD ACCESS</h3>
            <p>লাইসেন্স ফি: <b>{LICENSE_PRICE}</b></p>
            <p>ভেরিফিকেশন ফি: <b>{CHARGE_FEE}</b></p>
        </div>
        <div class='vip-card'>
            <h3 style='color:#ffd700;'>VIP MEMBERSHIP</h3>
            <p>লাইসেন্স ফি: <b>{VIP_PRICE_RANGE}</b></p>
            <p>(শুধুমাত্র আমন্ত্রিতদের জন্য)</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # আনলক অপশন (দুইটি আলাদা কলাম)
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("💳 পেমেন্ট গেটওয়ে")
        st.info(f"বিকাশ/নগদ (Personal): {AKASH_NUMBER}")
        user_trx = st.text_input("TrxID কোডটি দিন:", key="trx_gate_input", placeholder="Ex: 8M29X7PQ").strip()
        if st.button("TrxID দিয়ে আনলক 🔓"):
            if user_trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "TrxID", "Val": user_trx, "Status": "Success"})
                st.success("ভেরিফাইড! আনলক হচ্ছে...")
                time.sleep(1.5); st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error(f"❌ ভুল TrxID! (ভুল চেষ্টা: {st.session_state.failed_attempts}/3)")

    with col_b:
        st.subheader("👑 ভিআইপি গেটওয়ে")
        st.write("যাদের কাছে গোপন ভিআইপি পাসওয়ার্ড আছে, তারা এখানে দিন:")
        
        # এটিই সেই ভিআইপি পাসওয়ার্ড বক্স। আমি এটিকে আরও ক্লিয়ার করে দিয়েছি।
        vip_pass_input = st.text_input("গোপন VIP পাসওয়ার্ডটি দিন:", type="password", key="vip_pass_gate_input", placeholder="VIP পাসওয়ার্ড").strip()
        
        if st.button("পাস দিয়ে সরাসরি প্রবেশ 🚀"):
            if vip_pass_input == VIP_FREE_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "VIP Pass", "Val": "FREE_ACCESS", "Status": "Success"})
                st.success("✅ ভিআইপি এক্সেস গ্র্যান্টেড! স্বাগতম আকাশ।")
                time.sleep(1.5); st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error(f"❌ অবৈধ পাসওয়ার্ড! (ভুল চেষ্টা: {st.session_state.failed_attempts}/3)")

    st.stop() # আনলক না হওয়া পর্যন্ত নিচে যাবে না

# --- ৫. মূল ড্যাশবোর্ড (আনলক হওয়ার পর) ---
# আকাশের সব কটি ট্যাব একসাথে
tab1, tab2, tab3, tab4 = st.tabs(["📡 NASA COMMAND", "📝 WORKSPACE", "🌍 GLOBAL DATA", "⚙️ MONITOR CENTER"])

with tab1:
    st.markdown("### 🛰️ নাসা কমান্ড সেন্টার সক্রিয় (V33 PRO)")
    st.success(f"অভিনন্দন! আপনার {LICENSE_PRICE} মূল্যের প্রফেশনাল লাইসেন্স সক্রিয় হয়েছে।")
    st.info("আপনার ১০,০০০ টাকার পুরস্কার ক্লেইম করতে অ্যাডমিন প্যানেলে বিকাশ নাম্বার জমা দিন।")

with tab2:
    # আকাশের পার্সোনাল ওয়ার্কস্পেস
    st.markdown("### 📝 আকাশের গোপন ওয়ার্কস্পেস")
    st.info("আকাশ জান, তোমার সব প্রজেক্টের নোট এখানে সেভ থাকবে।")
    st.session_state.my_notes = st.text_area("আপনার গোপন নোটস:", value=st.session_state.my_notes, height=300)
    if st.button("সেভ করুন ✅"): st.success("আপনার ডাটা সেভ করা হয়েছে!")

with tab3:
    st.markdown("### 🌍 গ্লোবাল ইউজার ডাটা")
    with st.form("global_u_form"):
        st.text_input("নাম:"); st.text_area("বার্তা/রিপোর্ট:"); submit = st.form_submit_button("সার্ভারে পাঠান")
        if submit: st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "User Message", "Status": "Received"})

with tab4:
    # --- অ্যাডমিন মনিটরিং সেন্টার (তোমার সব ডাটা দেখার জায়গা) ---
    st.subheader("⚙️ SUPER ADMIN MONITORING CENTER")
    admin_monitor_key = st.text_input("আপনার গোপন মালিকানা পাসওয়ার্ড দিন (Akash@Owner#2026):", type="password", key="admin_audit_key", placeholder="অ্যাডমিন পাসওয়ার্ড")
    
    if admin_monitor_key == OWNER_PASS:
        st.markdown("<div class='admin-monitor-card'>✅ স্বাগতম আকাশ জান! আপনার সার্ভারের বর্তমান অবস্থা নিচে দেওয়া হলো।</div>", unsafe_allow_html=True)
        
        # ডাটাবেজ মেট্রিক্স
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("মোট লগ (Logs)", len(st.session_state.logs))
        col_m2.metric("ভুল চেষ্টা (Failed Access)", st.session_state.failed_attempts)
        col_m3.metric("TrxID ডাটাবেজ", len(st.session_state.valid_ids))

        st.markdown("### 📊 বিস্তারিত ইউজার অ্যাক্টিভিটি")
        if st.session_state.logs:
            # বিস্তারিত লগ টেবিল
            df = pd.DataFrame(st.session_state.logs)
            st.table(df) # কে TrxID দিয়েছে আর কে VIP পাস দিয়ে ঢুকেছে—সব এখানে দেখা যাবে
        else:
            st.info("এখনো কোনো অ্যাক্টিভিটি রেকর্ড হয়নি।")

        st.markdown("---")
        st.subheader("🛠️ সার্ভার কন্ট্রোল")
        # নতুন TrxID যোগ করার অপশন
        new_trx_id = st.text_input("নতুন পেমেন্ট কোড (TrxID) যোগ করুন:")
        if st.button("কোড অ্যাড করুন"):
            st.session_state.valid_ids.append(new_trx_id)
            st.success(f"কোড '{new_trx_id}' সফলভাবে ডাটাবেজে যোগ হয়েছে।")
            
        if st.button("সব লগ ক্লিয়ার করুন (Clear Logs)"):
            st.session_state.logs = []
            st.rerun()
            
    elif admin_monitor_key != "":
        st.error("🚨 ভুল অ্যাডমিন পাসওয়ার্ড! এই জায়গাটি শুধুমাত্র আকাশের জন্য।")
    
    if st.button("লগ আউট 🔒"):
        st.session_state.access = False; st.rerun()

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SYSTEM | VERSION 33 PRO | MASTER CONSOLIDATED | DEVELOPED BY AKASH")
