import streamlit as st
import time

# ১. পেজ সেটআপ - AKASH NASA AI SERVER (SPACE EDITION)
st.set_page_config(page_title="AKASH NASA AI SERVER | SPACE", page_icon="🌌", layout="wide")

# ২. মহাকাশ থিম ডিজাইন (Deep Space & Nebula Color)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    /* মহাকাশের ব্যাকগ্রাউন্ড */
    .stApp { 
        background: radial-gradient(circle at bottom, #000c18 0%, #000000 100%), 
                    url('https://www.transparenttextures.com/patterns/stardust.png') !important; 
        color: #ffffff;
    }
    
    /* গ্যালাক্সি টাইটেল এনিমেশন */
    .main-title { 
        background: linear-gradient(90deg, #00f2ff, #7b2ff7, #ff00d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
        font-size: 60px; 
        font-weight: 900; 
        filter: drop-shadow(0 0 15px rgba(123, 47, 247, 0.8));
        margin-bottom: 10px;
        animation: space-glow 3s linear infinite;
    }
    
    @keyframes space-glow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }

    /* নেবুলা গ্লাস কার্ড */
    .glass-card { 
        background: rgba(255, 255, 255, 0.03); 
        backdrop-filter: blur(25px);
        padding: 35px; 
        border-radius: 30px; 
        border: 1px solid rgba(0, 242, 255, 0.2); 
        text-align: center; 
        box-shadow: 0 0 40px rgba(123, 47, 247, 0.2);
    }

    /* কাস্টম স্লাইডার কালার (আকাশী/বেগুনি আভা) */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #00f2ff, #7b2ff7) !important;
    }

    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #7b2ff7 0%, #00f2ff 100%) !important; 
        color: white !important; 
        border-radius: 20px; 
        height: 65px; 
        font-weight: bold; 
        font-size: 22px;
        border: none;
        box-shadow: 0 0 25px rgba(123, 47, 247, 0.5);
    }
    
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.7);
    }

    .amount-display {
        font-size: 45px;
        color: #00f2ff;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# ৩. ভয়েস ফাংশন
def speak_text(text):
    if text:
        js_code = f"<script>var msg = new SpeechSynthesisUtterance('{text}'); msg.lang = 'bn-BD'; window.speechSynthesis.speak(msg);</script>"
        st.components.v1.html(js_code, height=0)

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# ৪. মহাকাশ পেমেন্ট গেটওয়ে
if not st.session_state.authenticated:
    st.markdown("""
    <div style="text-align: center; margin-top: -30px;">
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
        <p style="color: #7b2ff7; font-size: 20px; letter-spacing: 5px; font-weight: bold;">SPACE EXPEDITION v5.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00f2ff;'>💳 মহাকাশ পেমেন্ট গেটওয়ে</h3>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #ffffff; font-size: 40px; text-shadow: 0 0 10px #7b2ff7;'>01967840830</h1>", unsafe_allow_html=True)
        st.write("বিকাশ বা নগদ (পার্সোনাল)")
        
        st.markdown("---")
        st.write("আপনার আপডেট অ্যামাউন্ট নির্বাচন করুন:")
        amount = st.slider("", 3000, 10000, 5000, step=500)
        st.markdown(f'<p class="amount-display">৳ {amount}</p>', unsafe_allow_html=True)
        
        with st.form("space_activation"):
            u_name = st.text_input("Candidate Name", placeholder="আপনার নাম")
            u_trxid = st.text_input("TrxID / Master Key", type="password", placeholder="পেমেন্ট ট্রানজেকশন আইডি")
            
            if st.form_submit_button("ভেরিফাই এবং সার্ভারে প্রবেশ করুন 🛸"):
                if u_trxid == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "Akash"
                    speak_text(f"স্বাগতম {st.session_state.user_name}. মহাকাশ সার্ভারে আপনার সংযোগ সফল।")
                    st.rerun()
                elif len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name
                    speak_text(f"পেমেন্ট সফল। {u_name}, আকাশ নাসা সার্ভার এখন আপনার নিয়ন্ত্রণে।")
                    st.rerun()
                else:
                    st.error("ভুল TrxID! মহাকাশ সার্ভারে প্রবেশাধিকারের জন্য সঠিক আইডি দিন।")
        st.markdown('</div>', unsafe_allow_html=True)

# ৫. মেইন স্পেস ড্যাশবোর্ড
else:
    st.markdown("<h1 class='main-title'>SPACE COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["💬 Galaxy AI Chat", "🛰️ Satellite Control", "📊 Live Stats", "🔐 Logout"])

    with tabs[0]:
        st.subheader(f"🚀 মিশন কমান্ড: {st.session_state.user_name}")
        u_input = st.chat_input("মহাকাশ কমান্ড দিন...")
        if u_input:
            st.session_state.chat_history.append({"role": "user", "content": u_input})
            reply = f"ঠিক আছে {st.session_state.user_name}, মহাকাশ সার্ভার আপনার ডেটা প্রসেস করছে।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)
        
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tabs[1]:
        col_x, col_y = st.columns(2)
        with col_x:
            if st.button("Activate Messenger Bot"):
                st.success("Bot Connected via Satellite")
                speak_text("মেসেঞ্জার অটোমেশন এখন মহাকাশ লিঙ্কে সক্রিয়।")
        with col_y:
            if st.button("Sync Global API"):
                st.info("Syncing with Global Server")
                speak_text("গ্লোবাল ডাটা সিঙ্ক হচ্ছে।")

    with tabs[2]:
        st.subheader("📡 সার্ভার স্ট্যাটাস")
        st.write("কানেকশন: আল্ট্রা স্টেবল")
        st.progress(100)

    with tabs[3]:
        if st.button("Logout From Orbit"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #444;'>Deep Space Engine v5.0 | Developed by Akash</p>", unsafe_allow_html=True)
