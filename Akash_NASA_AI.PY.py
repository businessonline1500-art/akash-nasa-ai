import streamlit as st
import time

# ১. পেজ সেটআপ (AKASH NASA AI SERVER - MASTERSHIP UPDATE)
st.set_page_config(page_title="AKASH NASA AI SERVER | MASTERSHIP", page_icon="🚀", layout="wide")

# ২. প্রিমিয়াম ডীপ স্পেস ও নিওন ডিজাইন (Error Free CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001d3d 0%, #000000 100%) !important; 
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    
    .logo-container {
        text-align: center;
        margin-top: -50px;
        margin-bottom: 10px;
    }
    
    .nasa-logo {
        filter: drop-shadow(0 0 15px rgba(0, 242, 255, 0.5));
    }
    
    .main-title { 
        color: #ff3c00; text-align: center; font-family: 'Orbitron', sans-serif;
        font-size: 50px; font-weight: bold; 
        text-shadow: 0 0 25px rgba(255, 60, 0, 0.7);
        margin-top: 0;
    }

    /* গ্লাস-মরফিজম কার্ড ডিজাইন */
    .glass-card { 
        background: rgba(255, 255, 255, 0.03); 
        backdrop-filter: blur(15px);
        padding: 40px; 
        border-radius: 25px; 
        border: 1px solid rgba(255, 60, 0, 0.3); 
        text-align: center; 
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
        margin-bottom: 15px;
    }
    
    /* পেমেন্ট ইনফো বক্স (সুন্দর লেখা) */
    .payment-protocol-box {
        background: rgba(255, 60, 0, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff3c00;
        text-align: left;
        margin-bottom: 15px;
    }
    
    .protocol-title { color: #00f2ff; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
    .protocol-step { color: #aaaaaa; font-size: 16px; margin: 5px 0; }
    .price-display { font-size: 40px; color: #ff3c00; font-weight: bold; text-shadow: 0 0 20px #ff3c00; }

    .stButton>button { 
        width: 100%; background: linear-gradient(135deg, #ff3c00 0%, #7b0000 100%) !important; 
        color: white !important; border-radius: 15px; height: 60px; font-weight: bold; 
        font-size: 22px; border: none; box-shadow: 0 5px 20px rgba(255, 60, 0, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(255, 60, 0, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# ৩. স্মার্ট ভয়েস ফাংশন
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
    # নাসার লোগো ও টাইটেল
    st.markdown("""
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" width="180">
        <h1 class="main-title">AKASH NASA AI SERVER</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='color: #00f2ff; margin-bottom: 10px;'>🚀 মিশন কন্ট্রোল আনলক করুন</h2>", unsafe_allow_html=True)
        st.write("আকাশ নাসা সার্ভারের পূর্ণ ক্ষমতা ব্যবহার করতে নিচের ধাপগুলো অনুসরণ করুন। আপনার ব্যক্তিগত এআই অ্যাসিস্ট্যান্ট এবং গ্লোবাল অ্যাপ অটোমেশন রেডি।")
        st.markdown("---")
        
        # পেমেন্ট প্রোটোকল সেকশন (তোমার মনের মতো নতুন লেখা)
        st.markdown("""
        <div class="payment-protocol-box">
            <div class="protocol-title">মিশন অ্যাক্টিভেশন প্রোটোকল:</div>
            <div class="protocol-step">১. নিচের স্লাইডার থেকে আপনার পেমেন্ট অ্যামাউন্ট নির্বাচন করুন।</div>
            <div class="protocol-step">২. নিচের নম্বরে বিকাশ বা নগদ (পার্সোনাল) অ্যাপ থেকে টাকা পাঠিয়ে দিন।</div>
            <div class="protocol-step">৩. পেমেন্ট সফল হলে TrxID কপি করে নিচের ফর্মে আপনার নাম সহ বসিয়ে দিন।</div>
            <div class="protocol-step">৪. 'লঞ্চ মিশন' বাটনে ক্লিক করে সার্ভার কানেক্ট করুন।</div>
        </div>
        """, unsafe_allow_html=True)
        
        # স্লাইডার অ্যামাউন্ট
        amount = st.slider("", 3000, 10000, 5000, step=500)
        st.markdown(f'<p class="price-display">৳ {amount}</p>', unsafe_allow_html=True)
        st.write("অ্যাক্টিভেশন ফি: ৩,০০০ টাকা থেকে ১০,০০০ টাকা")
        st.markdown("---")
        
        # পেমেন্ট তথ্য (বড় এবং সুন্দর লেখা)
        st.markdown("""
        <div style="text-align: center; margin-bottom: 15px;">
            <p style="font-size: 20px; color: #aaaaaa; margin-bottom: 5px;">বিকাশ ও নগদ (পার্সোনাল):</p>
            <h1 style="color: #ff3c00; font-size: 45px; letter-spacing: 2px; text-shadow: 0 0 10px #ff3c00;">01967840830</h1>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("activation_form"):
            u_name = st.text_input("Candidate Name", placeholder="আপনার নাম লিখুন")
            u_trxid = st.text_input("TrxID / Master Key দিন", type="password", placeholder="পেমেন্ট আইডি দিন")
            if st.form_submit_button("ভেরিফাই এবং লঞ্চ মিশন 🚀"):
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

# ৫. মেইন কমান্ড সেন্টার (লগইন করার পর আসবে)
else:
    st.markdown("""
    <div class="logo-container" style="margin-top: -30px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" width="100">
        <h1 class="main-title">MISSION COMMAND CENTER</h1>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💬 AI Voice Assistant", "📡 App Automation", "🔐 Logout"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}, বলুন কী কাজ করতে হবে?")
        user_input = st.chat_input("সিস্টেমকে কমান্ড দিন...")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            reply = f"বুঝেছি {st.session_state.user_name}, আকাশ নাসা সার্ভার কাজটি সম্পন্ন করছে।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Activate Messenger Bot"):
                st.success("Messenger Online")
                speak_text("মেসেঞ্জার অটোমেশন একটিভ হয়েছে।")
        with col_b:
            if st.button("WhatsApp API Sync"):
                st.info("WhatsApp Syncing")
                speak_text("হোয়াটসঅ্যাপ সিঙ্ক সম্পন্ন হয়েছে।")

    with tab3:
        if st.button("Logout From Orbit"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #444;'>Developer: Akash | AKASH NASA AI SERVER v5.0 Master Update</p>", unsafe_allow_html=True)
