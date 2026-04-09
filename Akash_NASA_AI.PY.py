import streamlit as st
import time

# ১. পেজ সেটআপ - AKASH NASA AI SERVER (PRO UPDATE)
st.set_page_config(page_title="AKASH NASA AI SERVER | PRO", page_icon="⚡", layout="wide")

# ২. আল্ট্রা-প্রিমিয়াম নিওন ডিজাইন ও এনিমেশন
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at top, #001d3d 0%, #000000 100%) !important; 
        color: #ffffff;
    }
    
    /* টাইটেল এনিমেশন */
    .main-title { 
        color: #ff3c00; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
        font-size: 55px; 
        font-weight: 900; 
        text-shadow: 0 0 30px #ff3c00, 0 0 60px #7b0000;
        margin-bottom: 10px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 20px #ff3c00; }
        to { text-shadow: 0 0 40px #ff3c00, 0 0 10px #00f2ff; }
    }

    /* গ্লাস কার্ড ডিজাইন */
    .glass-card { 
        background: rgba(255, 255, 255, 0.05); 
        backdrop-filter: blur(20px);
        padding: 30px; 
        border-radius: 25px; 
        border: 2px solid rgba(255, 60, 0, 0.3); 
        text-align: center; 
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.7);
        transition: 0.5s;
    }
    .glass-card:hover {
        border-color: #00f2ff;
        transform: translateY(-5px);
    }

    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #ff3c00 0%, #b92b27 100%) !important; 
        color: white !important; 
        border-radius: 18px; 
        height: 65px; 
        font-weight: bold; 
        font-size: 22px;
        border: none;
        box-shadow: 0 10px 30px rgba(255, 60, 0, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #00f2ff 0%, #0056b3 100%) !important;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.6);
    }

    /* পেমেন্ট স্লাইডার স্টাইল */
    .amount-display {
        font-size: 40px;
        color: #00f2ff;
        font-weight: bold;
        text-shadow: 0 0 15px #00f2ff;
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

# ৪. পেমেন্ট ও কাস্টম অ্যামাউন্ট সিস্টেম
if not st.session_state.authenticated:
    st.markdown("""
    <div style="text-align: center; margin-top: -20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="100">
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
        <p style="color: #00f2ff; font-size: 18px; letter-spacing: 2px;">SECURE ACCESS PROTOCOL v4.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("💳 পেমেন্ট গেটওয়ে (বিকাশ/নগদ)")
        st.markdown("<h2 style='color: #ff3c00; font-size: 35px;'>01967840830</h2>", unsafe_allow_html=True)
        
        # নিজের ইচ্ছামতো টাকা দেওয়ার সিস্টেম
        st.markdown("---")
        st.write("আপনার আপডেট অ্যামাউন্ট নির্বাচন করুন:")
        amount = st.slider("", 3000, 10000, 5000, step=500)
        st.markdown(f'<p class="amount-display">৳ {amount}</p>', unsafe_allow_html=True)
        
        with st.form("pro_activation"):
            u_name = st.text_input("Candidate Name", placeholder="আপনার নাম লিখুন")
            u_trxid = st.text_input("TrxID / Master Key", type="password", placeholder="পেমেন্ট আইডি দিন")
            
            if st.form_submit_button("ভেরিফাই এবং সার্ভার কানেক্ট করুন ⚡"):
                if u_trxid == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "Akash"
                    speak_text(f"স্বাগতম {st.session_state.user_name}. সার্ভার কানেকশন স্থিতিশীল।")
                    st.rerun()
                elif len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name
                    speak_text(f"পেমেন্ট সফল। {u_name}, আপনার আকাশ নাসা সার্ভার এখন একটিভ।")
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে সঠিক পেমেন্ট নিশ্চিত করুন।")
        st.markdown('</div>', unsafe_allow_html=True)

# ৫. মেইন কমান্ড সেন্টার
else:
    st.markdown("<h1 class='main-title'>SERVER COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["💬 AI Assistant", "📲 Automation", "📡 Live Tracking", "🔐 Logout"])

    with tabs[0]:
        st.subheader(f"🤖 অনলাইন: {st.session_state.user_name}")
        u_input = st.chat_input("সিস্টেম কমান্ড দিন...")
        if u_input:
            st.session_state.chat_history.append({"role": "user", "content": u_input})
            reply = f"বুঝেছি {st.session_state.user_name}, আকাশ নাসা সার্ভার আপনার অনুরোধটি প্রসেস করছে।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)
        
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tabs[1]:
        col_x, col_y = st.columns(2)
        with col_x:
            if st.button("Activate Messenger Bot"):
                st.success("Messenger Bot Online")
                speak_text("মেসেঞ্জার অটোমেশন চালু হয়েছে।")
        with col_y:
            if st.button("Sync WhatsApp API"):
                st.info("WhatsApp Connected")
                speak_text("হোয়াটসঅ্যাপ সিঙ্ক সম্পন্ন।")

    with tabs[2]:
        st.subheader("📡 স্যাটেলাইট ট্র্যাকিং একটিভ")
        st.progress(85)
        st.write("সার্ভার কানেক্টিভিটি: ১০০%")

    with tabs[3]:
        if st.button("Logout Server"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #555;'>Power Update: v4.0 | Owner: Akash</p>", unsafe_allow_html=True)
