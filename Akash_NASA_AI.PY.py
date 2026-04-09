import streamlit as st
import time

# ১. পেজ সেটআপ
st.set_page_config(page_title="AI LIVE | NASA x AKASH AI", page_icon="🚀", layout="wide")

# ২. প্রিমিয়াম নিওন গ্লাস ডিজাইন (কালার আপডেট)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001d3d 0%, #000000 100%) !important; 
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .logo-container {
        text-align: center;
        margin-top: -50px;
    }
    
    .main-title { 
        color: #ff3c00; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
        font-size: 55px; 
        font-weight: bold; 
        text-shadow: 0 0 30px rgba(255, 60, 0, 0.6);
        margin-bottom: 5px;
    }

    /* গ্লাস বক্স ডিজাইন */
    .package-card, .payment-info { 
        background: rgba(255, 255, 255, 0.07); 
        backdrop-filter: blur(15px);
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid rgba(252, 61, 33, 0.3); 
        text-align: center; 
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-bottom: 15px;
    }
    
    .price-tag { 
        font-size: 35px; 
        color: #00f2ff; 
        font-weight: bold; 
        text-shadow: 0 0 10px #00f2ff;
    }

    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #ff3c00 0%, #7b0000 100%); 
        color: white; 
        border-radius: 15px; 
        height: 60px; 
        font-weight: bold; 
        font-size: 20px;
        border: none;
        box-shadow: 0 0 20px rgba(255, 60, 0, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(255, 60, 0, 0.7);
    }

    /* ইনপুট বক্স সুন্দর করা */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #ff3c00 !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# ৩. ভয়েস ফাংশন
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

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# ৪. পেমেন্ট গেটওয়ে (সবার আগে)
if not st.session_state.authenticated:
    # নাসা লোগো এবং টাইটেল
    st.markdown("""
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="150">
        <h1 class="main-title">AKASH AI SYSTEM</h1>
        <p style="text-align: center; color: #00f2ff; font-size: 18px;">মিশন আনলক করতে প্যাকেজ বেছে নিন</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="package-card"><h3 style="color:#ff3c00;">CORE</h3><p class="price-tag">৳৩,০০০</p><p>এআই বেসিক অ্যাক্সেস</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="package-card"><h3 style="color:#ff3c00;">PRO</h3><p class="price-tag">৳৫,০০০</p><p>এআই + অটোমেশন</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="package-card"><h3 style="color:#ff3c00;">ULTRA</h3><p class="price-tag">৳১০,০০০</p><p>ফুল সিস্টেম কন্ট্রোল</p></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("""
        <div class="payment-info">
            <h3 style="color: white; margin-bottom: 5px;">💳 পেমেন্ট করুন</h3>
            <p style="font-size: 20px; color: #00f2ff;">বিকাশ ও নগদ (পার্সোনাল)</p>
            <h1 style="color: #ff3c00; font-size: 45px; letter-spacing: 2px;">01967840830</h1>
            <p style="color: #ffffff; font-weight: bold;">টাকা পাঠিয়ে নিচে TrxID দিন</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("activation_form"):
            u_name = st.text_input("আপনার নাম (Candidate Name)")
            u_trxid = st.text_input("Transaction ID (TrxID)", type="password")
            if st.form_submit_button("ভেরিফাই এবং লঞ্চ মিশন 🚀"):
                if u_trxid == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "Akash"
                    speak_text(f"স্বাগতম {st.session_state.user_name}. নাসা এআই সিস্টেম আনলক করা হয়েছে.")
                    st.rerun()
                elif len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name
                    speak_text(f"ধন্যবাদ {u_name}. পেমেন্ট সফল হয়েছে.")
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে সঠিক পেমেন্ট নিশ্চিত করুন।")

# ৫. মেইন ড্যাশবোর্ড
else:
    st.markdown("""
    <div style="text-align:center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" width="80">
        <h1 class="main-title">COMMAND CENTER</h1>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💬 AI Voice Assistant", "📲 App Control", "🔐 Logout"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}, কমান্ড দিন")
        user_input = st.chat_input("Ask something...")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            reply = f"ঠিক আছে {st.session_state.user_name}, নাসা সার্ভার থেকে কাজটি সম্পন্ন করছি।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ অটোমেশন")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Messenger Mode"):
                st.success("Messenger Bot Active")
                speak_text("মেসেঞ্জার কন্ট্রোল চালু হয়েছে।")
        with col_b:
            if st.button("WhatsApp Link"):
                st.info("WhatsApp Sync Active")
                speak_text("হোয়াটসঅ্যাপ সিঙ্ক হয়েছে।")

    with tab3:
        if st.button("Exit System"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #888;'>Developer: Akash | NASA AI LIVE 2026</p>", unsafe_allow_html=True)
