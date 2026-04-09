import streamlit as st
import time

# ১. পেজ সেটআপ (AKASH NASA AI SERVER - MASTER UPDATE)
st.set_page_config(page_title="AKASH NASA AI SERVER | MASTER", page_icon="🚀", layout="wide")

# ২. প্রিমিয়াম ডীপ স্পেস ও নিওন ডিজাইন (Color & Logo Update)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    /* মহাকাশের ব্যাকগ্রাউন্ড */
    .stApp { 
        background: radial-gradient(circle at center, #001d3d 0%, #000000 100%) !important; 
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* লোগো ও টাইটেল কন্টেইনার */
    .header-container {
        text-align: center;
        margin-top: -50px;
        margin-bottom: 20px;
    }
    
    /* নাসার কক্ষপথ লোগো স্টাইল */
    .nasa-logo {
        filter: drop-shadow(0 0 15px rgba(0, 242, 255, 0.5));
        margin-bottom: 10px;
    }
    
    .main-title { 
        color: #ff3c00; 
        font-family: 'Orbitron', sans-serif;
        font-size: 50px; 
        font-weight: 900; 
        text-shadow: 0 0 25px rgba(255, 60, 0, 0.7);
        margin-top: 0;
    }

    /* গ্লাস-মরফিজম কার্ড ডিজাইন */
    .glass-card { 
        background: rgba(255, 255, 255, 0.05); 
        backdrop-filter: blur(15px);
        padding: 30px; 
        border-radius: 25px; 
        border: 1px solid rgba(255, 60, 0, 0.3); 
        text-align: center; 
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
        margin-bottom: 15px;
    }
    
    /* স্লাইডার অ্যামাউন্ট ডিসপ্লে */
    .price-tag { 
        font-size: 35px; 
        color: #00f2ff; 
        font-weight: bold; 
        text-shadow: 0 0 15px #00f2ff;
    }

    /* প্রিমিয়াম বাটন */
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #ff3c00 0%, #7b0000 100%) !important; 
        color: white !important; 
        border-radius: 15px; 
        height: 60px; 
        font-weight: bold; 
        font-size: 20px;
        border: none;
        box-shadow: 0 5px 20px rgba(255, 60, 0, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(255, 60, 0, 0.8);
    }
    
    /* ইনপুট বক্স সুন্দর করা */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 60, 0, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# ৩. স্মার্ট ভয়েস ফাংশন (বাংলা)
def speak_text(text):
    if text:
        js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'bn-BD';
        window.speechSynthesis.speak(msg);
        </script>
        """
        st.components.v1.html(js_code, height=0)

# সেশন স্টেট (লগইন হ্যান্ডলিং)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# ৪. পেমেন্ট গেটওয়ে ইন্টারফেস (লগইন এর আগে)
if not st.session_state.authenticated:
    # মাঝখানে নাসার অরিজিনাল লোগো ও টাইটেল
    st.markdown("""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" width="180">
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
        <p style="text-align: center; color: #00f2ff; font-size: 18px; letter-spacing: 2px;">মিশন আনলক করতে আপডেট কিনুন</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: white; margin-bottom: 10px;'>💳 পেমেন্ট গেটওয়ে</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px; margin-bottom: 5px;'>বিকাশ ও নগদ (পার্সোনাল):</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #ff3c00; font-size: 45px; letter-spacing: 2px;'>01967840830</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        # কাস্টম পেমেন্ট স্লাইডার
        st.write("আপনার আপডেট অ্যামাউন্ট নির্বাচন করুন:")
        amount = st.slider("", 3000, 10000, 5000, step=500)
        st.markdown(f'<p class="price-tag">৳ {amount}</p>', unsafe_allow_html=True)
        
        with st.form("activation_form"):
            u_name = st.text_input("Candidate Name", placeholder="আপনার নাম")
            u_trxid = st.text_input("TrxID / Master Key", type="password", placeholder="পেমেন্ট আইডি")
            if st.form_submit_button("ভেরিফাই এবং সার্ভার কানেক্ট করুন 🚀"):
                # মাস্টার কি চেক
                if u_trxid == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "Akash"
                    speak_text(f"স্বাগতম {st.session_state.user_name}. আকাশ নাসা সার্ভার আনলক করা হয়েছে.")
                    st.rerun()
                elif len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "User"
                    speak_text(f"ধন্যবাদ {st.session_state.user_name}. পেমেন্ট সফল হয়েছে.")
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে সঠিক পেমেন্ট নিশ্চিত করুন।")
        st.markdown('</div>', unsafe_allow_html=True)

# ৫. মেইন কমান্ড সেন্টার (লগইন করার পর)
else:
    # ড্যাশবোর্ডের মাঝখানেও লোগো থাকবে
    st.markdown("""
    <div class="header-container" style="margin-top: -30px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" width="100">
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
        <p style="text-align: center; color: #00f2ff;">MISSION COMMAND CENTER</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💬 AI Voice Assistant", "📡 App Automation", "🔐 Logout"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}, বলুন কী কাজ করতে হবে?")
        user_input = st.chat_input("সিস্টেমকে কমান্ড দিন...")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            reply = f"ঠিক আছে {st.session_state.user_name}, আকাশ নাসা সার্ভার কাজটি সম্পন্ন করছে।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ অটোমেশন")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Messenger Bot Active"):
                st.success("Messenger Online")
                speak_text("মেসেঞ্জার অটোমেশন একটিভ হয়েছে।")
        with col_b:
            if st.button("WhatsApp API Sync"):
                st.info("WhatsApp Syncing")
                speak_text("হোয়াটসঅ্যাপ সিঙ্ক সম্পন্ন হয়েছে।")

    with tab3:
        if st.button("Logout From Server"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #444;'>Developer: Akash | AKASH NASA AI SERVER v5.0 Master Update</p>", unsafe_allow_html=True)
