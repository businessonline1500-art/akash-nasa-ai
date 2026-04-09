import streamlit as st
import pandas as pd
from datetime import datetime

# পেজ সেটআপ
st.set_page_config(page_title="AKASH NASA AI | ULTIMATE", page_icon="💎", layout="centered")

# --- প্রিমিয়াম নিওন ও গ্লসি ডিজাইন (CSS) ---
st.markdown("""
<style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp {
        background: radial-gradient(circle at top, #0a192f 0%, #020c1b 100%);
        color: #e6f1ff;
        font-family: 'Inter', sans-serif;
    }
    
    /* নিওন টাইটেল */
    .header-text {
        text-align: center;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 50px;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
        margin-bottom: 0px;
    }

    /* পেমেন্ট কার্ড ডিজাইন */
    .price-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .price-card:hover {
        border-color: #00ffcc;
        transform: translateY(-5px);
    }

    /* গ্লোয়িং বাটন */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00ffcc, #0088ff) !important;
        color: #020c1b !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 12px !important;
        height: 55px !important;
        font-size: 18px !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
    }

    /* ইনপুট বক্স */
    .stTextInput>div>div>input {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid #1d2d44 !important;
        color: #00ffcc !important;
    }

    /* গোপন অ্যাডমিন সেকশন */
    .admin-secret {
        background: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
        padding: 20px;
        margin-top: 100px;
        border: 1px solid #ff4b4b33;
    }
</style>
""", unsafe_allow_html=True)

# সেশন ডাটাবেস
if 'database' not in st.session_state:
    st.session_state.database = []

# --- হেডার সেকশন ---
st.markdown('<p class="header-text">AKASH NASA AI</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8892b0; margin-bottom:40px;'>Next-Gen Intelligent Operating System</p>", unsafe_allow_html=True)

# --- প্রাইসিং মডেল (২টি অপশন) ---
st.markdown("### 💎 সিলেক্ট করুন আপনার প্যাকেজ")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="price-card">
        <h4 style='color:#00ffcc;'>NEW USER</h4>
        <h2 style='margin:0;'>৳ ৩,০০০</h2>
        <p style='font-size:12px; color:#8892b0;'>বেসিক এআই লাইসেন্স</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="price-card">
        <h4 style='color:#0088ff;'>UPDATE SYSTEM</h4>
        <h2 style='margin:0;'>৳ ৫,০০০+</h2>
        <p style='font-size:12px; color:#8892b0;'>প্রো ফিচার ও সিকিউরিটি</p>
    </div>
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- পেমেন্ট ফরম ---
with st.container():
    st.markdown("### 📝 পেমেন্ট ভেরিফিকেশন ফরম")
    
    u_name = st.text_input("আপনার পূর্ণ নাম", placeholder="উদা: আকাশ আহমেদ")
    u_phone = st.text_input("সক্রিয় মোবাইল নম্বর", placeholder="01XXXXXXXXX")
    
    u_type = st.selectbox("আপনি কি করতে চান?", ["নতুন ইউজার (৩০০০ টাকা)", "সিস্টেম আপডেট (৫০০০ টাকা)"])
    
    # ডাইনামিক প্রাইস ক্যালকুলেশন
    u_amount = 3000 if "নতুন" in u_type else 5000
    
    st.markdown(f"""
        <div style='background:rgba(0,255,204,0.1); padding:10px; border-radius:10px; border-left:5px solid #00ffcc;'>
            <span style='color:#8892b0;'>নির্ধারিত মূল্য:</span> <b style='color:#00ffcc; font-size:20px;'>{u_amount} BDT</b>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    u_method = st.selectbox("পেমেন্ট গেটওয়ে", ["bKash (01967840830)", "Nagad (01967840830)"])
    u_trx = st.text_input("Transaction ID (TrxID)", placeholder="উদা: 8N7X2W9L")

if st.button("CONFIRM SECURE PAYMENT"):
    if u_name and u_phone and u_trx:
        # ডাটাবেসে সেভ করা
        entry = {
            "সময়": datetime.now().strftime("%I:%M %p"),
            "নাম": u_name,
            "ফোন": u_phone,
            "টাইপ": u_type,
            "টাকা": u_amount,
            "ID": u_trx
        }
        st.session_state.database.append(entry)
        
        st.balloons()
        st.success(f"অর্ডার রিসিভড! ধন্যবাদ {u_name}। আমাদের টিম আপনার ট্রানজেকশনটি যাচাই করছে।")
    else:
        st.error("ভুল হয়েছে! দয়া করে সব তথ্য পূরণ করুন।")

# --- গোপন অ্যাডমিন প্যানেল (শুধুমাত্র আপনার জন্য) ---
st.markdown('<div class="admin-secret">', unsafe_allow_html=True)
st.markdown("#### 🛠️ Internal Control Unit")
pass_key = st.text_input("অ্যাক্সেস কী দিন", type="password", help="শুধুমাত্র আকাশ এটি ব্যবহার করতে পারবে")

if pass_key == "akash71": # আপনার পাসওয়ার্ড: akash71
    st.markdown("### 📊 মাস্টার ডাটাবেস")
    if len(st.session_state.database) > 0:
        df = pd.DataFrame(st.session_state.database)
        st.dataframe(df.style.set_properties(**{'background-color': '#020c1b', 'color': '#00ffcc'}))
        
        total = sum(d['টাকা'] for d in st.session_state.database)
        st.markdown(f"""
            <div style='text-align:right; font-size:25px; color:#00ffcc;'>
                মোট সংগ্রহ: ৳ {total}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("এখনো কোনো পেমেন্ট জমা পড়েনি।")
elif pass_key != "":
    st.warning("অ্যাক্সেস ডিনাইড! ভুল পাসওয়ার্ড।")

st.markdown('</div>', unsafe_allow_html=True)
