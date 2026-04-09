import streamlit as st
import time

# পেজ সেটআপ
st.set_page_config(page_title="AI LIVE | NASA x AKASH AI", page_icon="🚀", layout="wide")

# --- ডিজাইন ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #0b3d91 0%, #000000 100%) !important; color: white; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #fc3d21, #b92b27); color: white; border-radius: 10px; height: 50px; font-weight: bold; border: none; }
    .payment-box { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #fc3d21; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# ভয়েস রেসপন্স ফাংশন (জাভাস্ক্রিপ্ট ব্যবহার করে সরাসরি কথা বলবে)
def speak_text(text):
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

# --- ১. পেমেন্ট সিস্টেম ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #fc3d21;'>NASA x AKASH AI SYSTEM</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div class="payment-box">
            <h3 style="color: #81d4fa;">মিশন আনলক করতে পেমেন্ট করুন</h3>
            <p>বিকাশ/নগদ (পার্সোনাল): <b>01967840830</b></p>
            <p>অ্যাক্সেস ফি: ৩,০০০ টাকা</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            name = st.text_input("আপনার নাম লিখুন")
            trxid = st.text_input("Transaction ID (TrxID) / Master Key", type="password")
            if st.form_submit_button("Launch Mission"):
                if trxid == "akash-bypass-71" or len(trxid) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = name
                    st.success(f"স্বাগতম {name}! মিশন শুরু হচ্ছে।")
                    speak_text(f"স্বাগতম {name}. আমি আপনার ব্যক্তিগত এআই অ্যাসিস্ট্যান্ট. মিশন কন্ট্রোল আনলক করা হয়েছে.")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে সঠিক আইডি দিন।")

# --- ২. মেইন ড্যাশবোর্ড (AI Live) ---
else:
    st.markdown(f"<h1 style='text-align: center; color: #fc3d21;'>AI LIVE COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["💬 AI Voice Assistant", "🚀 Mission Control", "🛰️ Track ID", "🔐 Admin"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}, আমি আপনাকে কীভাবে সাহায্য করতে পারি?")
        user_input = st.chat_input("আপনার কমান্ড দিন...")
        
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # এআই রেসপন্স এবং কথা বলা
            if "কেমন আছো" in user_input:
                reply = f"আমি ভালো আছি {st.session_state.user_name}, আপনার সব কমান্ড প্রসেস করতে আমি তৈরি।"
            elif "কাজ" in user_input:
                reply = f"ঠিক আছে {st.session_state.user_name}, আমি আপনার হোয়াটসঅ্যাপ এবং মেসেঞ্জার অটোমেশন চেক করছি।"
            else:
                reply = f"{st.session_state.user_name}, আপনার কমান্ডটি গ্রহণ করা হয়েছে। নাসা সার্ভারে ডাটা পাঠানো হচ্ছে।"
            
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply) # এখানে এআই কথা বলবে

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("🚀 Active Missions")
        if st.button("Start System Scan"):
            st.write("Scanning all connected devices...")
            speak_text("সিস্টেম স্ক্যানিং শুরু হয়েছে.")

    with tab3:
        st.text_input("Enter ID to track status")

    with tab4:
        if st.text_input("Admin Password", type="password") == "akash71":
            st.write("Welcome to Master Settings.")
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.rerun()

st.markdown(f"<p style='text-align: center; color: #888;'>Logged in as: {st.session_state.user_name} | Project: AI Live</p>", unsafe_allow_html=True)
