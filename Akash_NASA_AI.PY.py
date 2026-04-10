import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. হাই-টেক মিলিটারি গ্রেড ইন্টারফেস ---
st.set_page_config(page_title="NASA SUPREME MASTER V33 - ULTIMATE", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; }
    .nasa-logo { display: block; margin: auto; width: 120px; filter: drop-shadow(0 0 15px #00eaff); }
    
    /* 🚨 আল্টিমেট সিকিউরিটি প্যানেল (সেনাবাহিনী, পুলিশ, সিআইডি) 🚨 */
    .emergency-panel { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 8px solid #ff0000; padding: 35px; background: #010101; 
        box-shadow: 0 0 100px red; border-radius: 20px; margin: 20px 0;
    }
    .alert-msg { font-size: 20px; color: #ffd700; margin: 10px 0; }
    .blink { animation: blinker 0.6s linear infinite; font-weight: 900; color: #ff0000; font-size: 40px; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    .status-box { background: rgba(255, 0, 0, 0.2); border: 1px solid red; padding: 15px; border-radius: 10px; margin-top: 15px;}
    .status-text { color: #00ff00; font-family: 'Courier New', monospace; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- ২. মাস্টার সিকিউরিটি সেটিংস ---
OWNER_PASS = "Akash@Owner#2026"         
VIP_FREE_PASS = "NASA-ADMIN-FREE-2026"  
AKASH_NUMBER = "01967840830"           

if 'access' not in st.session_state: st.session_state.access = False
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0
if 'logs' not in st.session_state: st.session_state.logs = []
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "SUCCESS100", "AKASH786"]

# --- ৩. মেইন হেডার ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA SUPREME MASTER V33</h1><p>Military & Intelligence Secure Network | Dev: Akash</p></div>", unsafe_allow_html=True)

# --- ৪. হাই-অ্যালার্ট গেটওয়ে (সেনাবাহিনী + পুলিশ + সিআইডি) ---
if not st.session_state.access:
    
    if st.session_state.failed_attempts >= 3:
        st.markdown(f"""
            <div class='emergency-panel'>
                <h1 class='blink'>🛑 ACCESS DENIED - SYSTEM LOCKED 🛑</h1>
                <p class='alert-msg'>বারবার ভুল তথ্যের কারণে আপনার ডিভাইসটি রাষ্ট্রীয় নজরদারিতে নেওয়া হয়েছে।</p>
                <div class='status-box'>
                    <div class='status-text'>🛡️ <b>সেনাবাহিনী:</b> কমান্ড সেন্টারকে সতর্ক করা হয়েছে।</div>
                    <div class='status-text'>🚓 <b>পুলিশ:</b> আপনার বর্তমান আইপি (IP) নিকটস্থ থানায় পাঠানো হয়েছে।</div>
                    <div class='status-text'>🕵️ <b>CID:</b> আপনার ডাটা এবং লোকেশন ট্র্যাক করা শুরু হয়েছে।</div>
                    <div class='status-text'>🛰️ <b>GPS:</b> COORDINATES SENT TO NATIONAL SURVEILLANCE</div>
                </div>
                <p style='color: white; margin-top: 15px;'>অবিলম্বে আপনার নিকটস্থ প্রশাসনিক কেন্দ্রে যোগাযোগ করুন।</p>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/V4NSRTs3h9XfG/giphy.gif")
        
        # শুধুমাত্র আকাশ জান (অ্যাডমিন) এটা আনলক করতে পারবে
        unlock = st.text_input("সিস্টেম রিসেট করতে অ্যাডমিন পাসওয়ার্ড দিন:", type="password", key="admin_lock_res")
        if st.button("Emergency Override"):
            if unlock == OWNER_PASS:
                st.session_state.failed_attempts = 0
                st.success("সিস্টেম আনলক হয়েছে।")
                time.sleep(1); st.rerun()
        st.stop()

    # মেইন লগইন প্যানেল
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("💳 পেমেন্ট গেটওয়ে")
        st.info(f"বিকাশ/নগদ (Personal): {AKASH_NUMBER}")
        trx_input = st.text_input("আপনার TrxID কোডটি দিন:", key="trx_main").strip()
        if st.button("ভেরিফাই করুন 🔓"):
            if trx_input in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "TrxID", "Status": "Verified"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error(f"ভুল TrxID! চেষ্টা বাকি: {3-st.session_state.failed_attempts}/3")

    with col_right:
        st.subheader("👑 ভিআইপি গেটওয়ে")
        vip_code = st.text_input("গোপন VIP পাসওয়ার্ড দিন:", type="password", key="vip_main").strip()
        if st.button("VIP প্রবেশ 🚀"):
            if vip_code == VIP_FREE_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now().strftime("%I:%M %p"), "Type": "VIP Pass", "Status": "Success"})
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error("অবৈধ পাসওয়ার্ড!")
    st.stop()

# --- ৫. মেইন ড্যাশবোর্ড (লগইন করার পর) ---
st.success("অভিনন্দন আকাশ! নাসা মিলিটারি নেটওয়ার্কে আপনাকে স্বাগতম।")
tab1, tab2, tab3 = st.tabs(["📡 COMMAND HQ", "📝 PRIVATE NOTES", "⚙️ MONITORING"])

with tab1:
    st.info("আপনার লাইসেন্স এবং সিকিউরিটি শিল্ড বর্তমানে ১০০০% সক্রিয়।")
    st.metric("সার্ভার হেলথ", "Secure", delta="Army Guarded")
    st.balloons()

with tab2:
    st.markdown("### 📝 আকাশ জান-এর গোপন ডায়েরি")
    st.session_state.my_notes = st.text_area("আপনার প্রজেক্টের নোট এখানে সেভ থাকবে:", value=st.session_state.my_notes, height=250)
    if st.button("সেভ করুন ✅"): st.success("আপনার গোপন ডাটা এনক্রিপ্ট করে সেভ করা হয়েছে।")

with tab3:
    st.subheader("⚙️ সুপার অ্যাডমিন কন্ট্রোল")
    master_key = st.text_input("মনিটর সেন্টার দেখতে ওনার পাসওয়ার্ড দিন:", type="password", key="admin_audit")
    if master_key == OWNER_PASS:
        st.markdown("✅ **ইউজার অ্যাক্টিভিটি লগস:**")
        if st.session_state.logs:
            st.table(pd.DataFrame(st.session_state.logs))
        else:
            st.write("কোনো লগ রেকর্ড নেই।")
            
        if st.button("সব লগ ক্লিয়ার করুন"):
            st.session_state.logs = []
            st.rerun()
    
    if st.button("সিস্টেম লগ আউট 🔒"):
        st.session_state.access = False; st.rerun()

st.markdown("---")
st.caption("© 2026 AKASH NASA AI SYSTEM | ARMY-POLICE-CID PROTECTED | VERSION 33.5")
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
