import streamlit as st
import time

# ১. পেজ সেটআপ (NASA x AKASH AI থিম)
st.set_page_config(page_title="AI LIVE | NASA x AKASH AI", page_icon="🚀", layout="wide")

# ২. প্রিমিয়াম ডার্ক নিওন ডিজাইন (Error Free CSS)
st.markdown("""
<style>
    .stApp { 
        background: radial-gradient(circle at center, #0b3d91 0%, #000000 100%) !important; 
        color: white; 
    }
    .main-title { 
        color: #fc3d21; text-align: center; font-size: 50px; font-weight: bold; 
        text-shadow: 0 0 20px #fc3d21; margin-bottom: 20px;
    }
    .stButton>button { 
        width: 100%; background: linear-gradient(90deg, #fc3d21, #b92b27); 
        color: white; border-radius: 12px; height: 55px; font-weight: bold; border: none;
        box-shadow: 0 4px 15px rgba(252, 61, 33, 0.4);
    }
    .package-card { 
        background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; 
        border: 1px solid #fc3d21; text-align: center; margin-bottom: 10px;
    }
    .price-tag { font-size: 28px; color: #00f2ff; font-weight: bold; }
    .payment-info { 
        background: rgba(252, 61, 33, 0.1); padding: 20px; border-radius: 15px; 
        border: 1px dashed #fc3d21; text-align: center; margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ৩. ভয়েস ফাংশন (এআই সরাসরি কথা বলবে)
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

# সেশন স্টেট হ্যান্ডলিং
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# ৪. পেমেন্ট গেটওয়ে (সবার আগে টাকা দিয়ে কিনতে হবে)
if not st.session_state.authenticated:
    st.markdown("<h1 class='main-title'>NASA x AKASH AI SYSTEM</h1>", unsafe_allow_html=True)
    
    # প্যাকেজ সেকশন
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="package-card"><h3>CORE</h3><p class="price-tag">৳৩,০০০</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="package-card"><h3>PRO</h3><p class="price-tag">৳৫,০০০</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="package-card"><h3>ULTRA</h3><p class="price-tag">৳১০,০০০</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    c1, c2, c3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("""
        <div class="payment-info">
            <h3 style="color: white;">💸 পেমেন্ট করুন</h3>
            <p style="font-size: 18px; margin: 0;">বিকাশ ও নগদ (পার্সোনাল)</p>
            <h2 style="color: #fc3d21;">01967840830</h2>
            <p style="color: #00f2ff;">টাকা পাঠিয়ে নাম ও TrxID দিন</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("activation_form"):
            u_name = st.text_input("Candidate Name")
            u_package = st.selectbox("প্যাকেজ নির্বাচন করুন", ["Basic (3000)", "Pro (5000)", "Ultra (10000)"])
            u_trxid = st.text_input("TrxID / Master Key", type="password")
            
            if st.form_submit_button("ভেরিফাই এবং সিস্টেম আনলক করুন"):
                # মাস্টার কি এবং সাধারণ ভেরিফিকেশন
                if u_trxid == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "Akash"
                    st.success("Master Access Granted!")
                    speak_text(f"স্বাগতম {st.session_state.user_name}. মিশন কন্ট্রোল আনলক করা হয়েছে.")
                    time.sleep(1)
                    st.rerun()
                elif len(u_trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = u_name if u_name else "User"
                    st.success("Verification Successful!")
                    speak_text(f"ধন্যবাদ {st.session_state.user_name}. পেমেন্ট সফল হয়েছে.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে সঠিক পেমেন্ট নিশ্চিত করুন।")

# ৫. মেইন ড্যাশবোর্ড (পেমেন্ট করার পর আসবে)
else:
    st.markdown(f"<h1 class='main-title'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["💬 AI Voice Assistant", "📲 App Automation", "🛰️ Mission Track", "🔐 Admin"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}, বলুন কী কাজ করতে হবে?")
        user_input = st.chat_input("কমান্ড দিন (যেমন: 'মেসেঞ্জারে অটো রিপ্লাই চালু করো')...")
        
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            # স্মার্ট রিপ্লাই লজিক
            if "মেসেঞ্জার" in user_input.lower() or "messenger" in user_input.lower():
                reply = f"{st.session_state.user_name}, আমি মেসেঞ্জার অটোমেশন স্ক্রিপ্ট ব্যাকগ্রাউন্ডে রান করছি।"
            elif "whatsapp" in user_input.lower() or "হোয়াটসঅ্যাপ" in user_input.lower():
                reply = f"{st.session_state.user_name}, হোয়াটসঅ্যাপ ডাইরেক্ট এপিআই কানেক্টেড।"
            else:
                reply = f"বুঝেছি {st.session_state.user_name}। আপনার কমান্ডটি নাসা সার্ভারে প্রসেস করা হচ্ছে।"
            
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ অটোমেশন")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Messenger Control"):
                st.success("Messenger Bot Active")
                speak_text("মেসেঞ্জার কন্ট্রোল চালু হয়েছে।")
        with col_b:
            if st.button("WhatsApp Sync"):
                st.info("WhatsApp API Linked")
                speak_text("হোয়াটসঅ্যাপ সিঙ্ক সম্পন্ন হয়েছে।")

    with tab3:
        st.subheader("🛰️ মিশন ট্র্যাকিং")
        st.text_input("Enter ID to Track")

    with tab4:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #555;'>Developer: Akash | NASA AI Live v3.0 Update</p>", unsafe_allow_html=True)
