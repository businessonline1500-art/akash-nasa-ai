import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. হাই-টেক নাসার ডিজাইন ও রেসপন্সিভ সেটিংস ---
st.set_page_config(page_title="NASA SUPREME MASTER PRO", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron', sans-serif; }
    .nasa-logo { display: block; margin: auto; width: 140px; filter: drop-shadow(0 0 15px #00eaff); }
    
    /* ভিআইপি ও জেনারেল প্রাইস ট্যাগ */
    .pricing-table {
        display: flex; justify-content: space-around; flex-wrap: wrap; margin: 20px 0;
    }
    .price-card {
        background: rgba(0, 234, 255, 0.1); border: 2px solid #00eaff;
        padding: 20px; border-radius: 15px; width: 45%; text-align: center;
        box-shadow: 0 0 15px #00eaff;
    }
    .vip-card {
        background: rgba(255, 215, 0, 0.1); border: 2px solid #ffd700;
        padding: 20px; border-radius: 15px; width: 45%; text-align: center;
        box-shadow: 0 0 15px #ffd700;
    }

    .stButton>button { 
        background: linear-gradient(90deg, #00eaff, #0080ff); 
        color: black; border-radius: 8px; font-weight: bold; width: 100%; height: 3.5em; 
    }
    .security-alert { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 4px solid red; padding: 20px; background: rgba(255,0,0,0.2); 
        box-shadow: 0 0 30px red; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ২. সিকিউরিটি ও সেটিংস ---
OWNER_PASS = "Akash@Owner#2026"  
DASHBOARD_PASS = "NASA-ADMIN-FREE-2026" # এই পাসওয়ার্ডটি দিলে টাকা ছাড়াই ঢোকা যাবে
AKASH_NUMBER = "01967840830"    

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed' not in st.session_state: st.session_state.failed = 0
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786"]

# --- ৩. মেইন হেডার ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA SUPREME MASTER COMMAND CENTER</h1><p>Global Security Layer | Dev: Akash</p></div>", unsafe_allow_html=True)

# --- ৪. গেটওয়ে সেকশন ---
if not st.session_state.access:
    # প্রাইসিং টেবিল
    st.markdown("""
    <div class='pricing-table'>
        <div class='price-card'>
            <h3 style='color:#00eaff;'>STANDARD ACCESS</h3>
            <p>লাইসেন্স ফি: <b>৫০০০ টাকা</b></p>
            <p>ভেরিফিকেশন: ৫০ টাকা</p>
        </div>
        <div class='vip-card'>
            <h3 style='color:#ffd700;'>VIP MEMBERSHIP</h3>
            <p>লাইসেন্স ফি: <b>৫০০ - ২০০০ টাকা</b></p>
            <p>(শুধুমাত্র আমন্ত্রিতদের জন্য)</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # লাকি ড্র
    st.markdown("### 🎁 NASA PRIZE POOL")
    if st.button("🔥 SPIN TO WIN 10,000 TK"):
        st.balloons()
        st.success("🎉 অভিনন্দন! আপনি ১০,০০০ টাকা জিতেছেন।")
        st.info("পুরস্কারটি আপনার অ্যাকাউন্টে নিতে সিস্টেমটি আনলক করুন।")

    st.markdown("---")

    # আনলক সিস্টেম
    st.subheader("🔑 এক্সেস গেটওয়ে")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.write("**পেমেন্ট গেটওয়ে (TrxID)**")
        st.info(f"বিকাশ/নগদ: {AKASH_NUMBER}")
        user_trx = st.text_input("TrxID কোড দিন:", key="trx_input").strip()
        if st.button("TrxID দিয়ে আনলক"):
            if user_trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now(), "Type": "TrxID", "Val": user_trx})
                st.rerun()
            else:
                st.session_state.failed += 1
                st.error("ভুল কোড!")

    with col_b:
        st.write("**ড্যাশবোর্ড পাস (Admin Pass)**")
        dash_pass = st.text_input("গোপন ড্যাশবোর্ড পাস দিন:", type="password", help="এই পাসওয়ার্ড থাকলে টাকা লাগবে না।")
        if st.button("পাস দিয়ে সরাসরি প্রবেশ"):
            if dash_pass == DASHBOARD_PASS:
                st.session_state.access = True
                st.session_state.logs.append({"Time": datetime.now(), "Type": "DashPass", "Val": "FREE_ACCESS"})
                st.success("ফ্রি এক্সেস গ্র্যান্টেড!")
                time.sleep(1); st.rerun()
            else:
                st.session_state.failed += 1
                st.error("অবৈধ পাসওয়ার্ড!")

    # সিকিউরিটি অ্যালার্ট
    if st.session_state.failed >= 3:
        st.markdown("<div class='security-alert'>🚨 SECURITY BREACH! বাংলাদেশ সেনাবাহিনী ও পুলিশ আপনার লোকেশন ট্র্যাক করছে।</div>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
    
    st.stop()

# --- ৫. মূল ড্যাশবোর্ড ---
t1, t2, t3, t4 = st.tabs(["📡 NASA CONTROL", "📝 AKASH WORKSPACE", "🌍 GLOBAL DATA", "⚙️ MASTER ADMIN"])

with t1:
    st.markdown("### 🛰️ লাইভ স্যাটেলাইট ফিড")
    st.success("আপনার প্রিমিয়াম এক্সেস সক্রিয় আছে।")
    st.write("পুরস্কারের টাকা ক্লেইম করতে আপনার বিকাশ নাম্বারটি অ্যাডমিন প্যানেলে জমা দিন।")

with t2:
    st.markdown("### 📝 আকাশের গোপন ওয়ার্কস্পেস")
    st.session_state.my_notes = st.text_area("আপনার নোটস:", value=st.session_state.my_notes, height=300)
    if st.button("সেভ করুন"): st.success("সংরক্ষিত হয়েছে!")

with t3:
    st.markdown("### 🌍 গ্লোবাল ইউজার ডাটা")
    st.text_input("আপনার নাম:")
    st.text_area("বার্তা:")
    st.button("সার্ভারে পাঠান")

with t4:
    st.subheader("⚙️ অ্যাডমিন কন্ট্রোল")
    if st.text_input("মাস্টার কি:", type="password") == OWNER_PASS:
        st.write("### এক্সেস লগ:")
        st.write(pd.DataFrame(st.session_state.logs))
        new_id = st.text_input("নতুন বৈধ TrxID যোগ করুন:")
        if st.button("সেভ আইডি"):
            st.session_state.valid_ids.append(new_id)
            st.success("আইডি যুক্ত হয়েছে।")
    elif st.button("লগ আউট"):
        st.session_state.access = False
        st.rerun()

st.markdown("---")
st.caption(f"© 2026 AKASH NASA SYSTEM | V33 PRO | ENCRYPTED BY NASA-CORE")
