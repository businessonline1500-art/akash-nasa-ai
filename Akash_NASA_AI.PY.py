import streamlit as st
import time

# পেজ কনফিগারেশন
st.set_page_config(page_title="AI LIVE | NASA x AKASH AI", page_icon="🚀", layout="wide")

# --- প্রিমিয়াম নিওন ডিজাইন ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #0b3d91 0%, #000000 100%) !important; color: white; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #fc3d21, #b92b27); color: white; border-radius: 12px; height: 50px; font-weight: bold; border: none; box-shadow: 0 4px 15px rgba(252, 61, 33, 0.4); }
    .package-card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #fc3d21; text-align: center; margin-bottom: 10px; }
    .price-tag { font-size: 26px; color: #fc3d21; font-weight: bold; }
    .payment-info { background: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px; border: 1px dashed #00f2ff; text-align: center; }
</style>
""", unsafe_allow_html=True)

# ভয়েস ফাংশন (জাভাস্ক্রিপ্ট এরর হ্যান্ডলিং সহ)
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

# সেশন স্টেট সেটআপ
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- ১. পেমেন্ট গেটওয়ে (লগইন এর আগে এটা আসবে) ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #fc3d21;'>NASA x AKASH AI SYSTEM</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="package-card"><h3>Basic</h3><p class="price-tag">৩,০০০ টাকা</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="package-card"><h3>Pro</h3><p class="price-tag">৫,০০০ টাকা</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="package-card"><h3>Ultra</h3><p class="price-tag">১০,০০০ টাকা</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown(f"""
        <div class="payment-info">
            <p style="font-size: 18px; margin-bottom: 5px;">বিকাশ ও নগদ (পার্সোনাল)</p>
            <h2 style="color: #fc3d21;">01967840830</h2>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            name_input = st.text_input("আপনার নাম")
            trx_input = st.text_input("TrxID / Master Key", type="password")
            submit = st.form_submit_button("মিশন চালু করুন")
            
            if submit:
                if trx_input == "akash-bypass-71":
                    st.session_state.authenticated = True
                    st.session_state.user_name = name_input if name_input else "Akash"
                    st.rerun()
                elif len(trx_input) >= 8:
                    st.session_state.authenticated = True
                    st.session_state.user_name = name_input
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে পেমেন্ট করে সঠিক আইডি দিন।")

# --- ২. মেইন কমান্ড সেন্টার ---
else:
    st.markdown(f"<h2 style='text-align: center; color: #fc3d21;'>AI LIVE MISSION CONTROL</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💬 AI Voice Assistant", "🛰️ App Automation", "⚙️ Admin"])

    with tab1:
        st.subheader(f"🤖 হ্যালো {st.session_state.user_name}")
        u_cmd = st.chat_input("কমান্ড লিখুন...")
        if u_cmd:
            st.session_state.chat_history.append({"role": "user", "content": u_cmd})
            reply = f"ঠিক আছে {st.session_state.user_name}, আমি কাজটি করছি।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ কন্ট্রোল")
        if st.button("Messenger Auto-Reply Active"):
            st.success("কাজ শুরু হয়েছে!")
            speak_text("মেসেঞ্জার অটোমেশন একটিভ")

    with tab3:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #555;'>Developer: Akash | NASA AI Live</p>", unsafe_allow_html=True)
