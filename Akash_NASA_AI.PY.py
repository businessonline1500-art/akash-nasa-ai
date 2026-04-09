import streamlit as st
import time

# ১. পেজ সেটআপ (AKASH NASA AI SERVER PRO v6.0)
st.set_page_config(page_title="AKASH NASA AI SERVER | SOLAR", page_icon="☀️", layout="wide")

# ২. মহাকাশ ও সৌর ডিজাইন (Deep Space & Solar Nebula Color)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    /* মহাকাশের ব্যাকগ্রাউন্ড */
    .stApp { 
        background: radial-gradient(circle at center, #001220 0%, #000000 100%), 
                    url('https://www.transparenttextures.com/patterns/black-linen.png') !important; 
        color: #ffffff;
    }
    
    /* গ্যালাক্সি টাইটেল */
    .main-title { 
        color: #ff3c00;
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
        font-size: 50px; 
        font-weight: 900; 
        text-shadow: 0 0 20px #ff3c00;
        margin-bottom: 5px;
    }

    /* রোবট এনিমেশন */
    @keyframes robot-float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    
    /* পেমেন্ট গ্লাস কার্ড (সবচেয়ে সুন্দর অংশ) */
    .solar-glass-box { 
        background: rgba(255, 255, 255, 0.02); 
        backdrop-filter: blur(20px);
        padding: 40px; 
        border-radius: 30px; 
        border: 2px solid rgba(255, 60, 0, 0.4); 
        text-align: center; 
        box-shadow: 0 0 50px rgba(255, 60, 0, 0.3);
        margin-top: 20px;
    }

    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #ff3c00, #ff8000) !important;
    }

    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #ff3c00 0%, #ff8000 100%) !important; 
        color: white !important; 
        border-radius: 20px; 
        height: 65px; 
        font-weight: bold; 
        font-size: 22px;
        border: none;
        box-shadow: 0 0 25px rgba(255, 60, 0, 0.5);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 50px rgba(255, 128, 0, 0.7);
    }

    .amount-display {
        font-size: 45px;
        color: #ffcc00;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(255, 204, 0, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# ৩. স্মার্ট ভয়েস ফাংশন
def speak_text(text):
    if text:
        js_code = f"<script>var msg = new SpeechSynthesisUtterance('{text}'); msg.lang = 'bn-BD'; window.speechSynthesis.speak(msg);</script>"
        st.components.v1.html(js_code, height=0)

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# ৪. মহাকাশ ও সৌর পেমেন্ট গেটওয়ে
if not st.session_state.authenticated:
    # সৌর টাইটেল ও লোগো
    st.markdown("""
    <div style="text-align: center; margin-top: -30px;">
        <h1 style="color: #ff8000; font-family: 'Orbitron', sans-serif; font-size: 30px; text-shadow: 0 0 10px #ff8000; margin-bottom: 5px;">☀️ SOLAR SYSTEM ☀️</h1>
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
        <p style="color: #ffcc00; font-size: 20px; letter-spacing: 5px;">EXPEDITION v6.0 POWER</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # এআই রোবটের ছবি এবং পেমেন্ট গেটওয়ে
        col_img, col_pay = st.columns([1, 3])
        
        with col_img:
            # এআই রোবটের ছবি (স্ট্যাটিক)
            st.markdown("""
            <div style="animation: robot-float 4s infinite ease-in-out;">
                <img src="https://i.ibb.co/N2L4b3P/robot.png" width="100%">
            </div>
            """, unsafe_allow_html=True)
            
        with col_pay:
            # পেমেন্ট কার্ড (সবচেয়ে সুন্দর অংশ)
            st.markdown('<div class="solar-glass-box">', unsafe_allow_html=True)
            st.markdown("<h3 style='color: #ffcc00; text-shadow: 0 0 10px #ffcc00;'>💳 পেমেন্ট গেটওয়ে</h3>", unsafe_allow_html=True)
            st.markdown("<h1 style='color: #ffffff; font-size: 40px; text-shadow: 0 0 10px #ff3c00; margin-bottom: 5px;'>01967840830</h1>", unsafe_allow_html=True)
            st.write("বিকাশ বা নগদ (পার্সোনাল)")
            
            st.markdown("---")
            st.write("আপনার আপডেট অ্যামাউন্ট নির্বাচন করুন:")
            amount = st.slider("", 3000, 10000, 5000, step=500)
            st.markdown(f'<p class="amount-display">৳ {amount}</p>', unsafe_allow_html=True)
            
            with st.form("space_activation"):
                u_name = st.text_input("Candidate Name", placeholder="আপনার নাম")
                u_trxid = st.text_input("TrxID / Master Key", type="password", placeholder="পেমেন্ট আইডি")
                
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
                        st.error("ভুল TrxID! দয়া করে সঠিক আইডি দিন।")
            st.markdown('</div>', unsafe_allow_html=True)

# ৫. মেইন স্পেস ড্যাশবোর্ড
else:
    st.markdown("""
    <div style="text-align: center; margin-top: -30px;">
        <h1 style="color: #ff8000; font-family: 'Orbitron', sans-serif; font-size: 30px; text-shadow: 0 0 10px #ff8000; margin-bottom: 5px;">☀️ SOLAR SYSTEM COMMAND ☀️</h1>
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
    </div>
    """, unsafe_allow_html=True)
    
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

st.markdown("<p style='text-align: center; color: #444;'>Deep Space Engine v6.0 | Developed by Akash</p>", unsafe_allow_html=True)
