import streamlit as st
import time

# পেজ সেটআপ - NASA x AKASH AI
st.set_page_config(page_title="AI LIVE | NASA x AKASH AI", page_icon="🚀", layout="wide")

# --- প্রিমিয়াম নিওন ডিজাইন ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #0b3d91 0%, #000000 100%) !important; color: white; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #fc3d21, #b92b27); color: white; border-radius: 12px; height: 50px; font-weight: bold; border: none; box-shadow: 0 4px 15px rgba(252, 61, 33, 0.4); }
    .package-card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #fc3d21; text-align: center; margin-bottom: 10px; transition: 0.3s; }
    .package-card:hover { transform: translateY(-5px); border-color: #00f2ff; box-shadow: 0 0 20px rgba(0, 242, 255, 0.2); }
    .price-tag { font-size: 26px; color: #fc3d21; font-weight: bold; }
    .payment-info { background: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px; border: 1px dashed #00f2ff; text-align: center; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# ভয়েস ফাংশন
def speak_text(text):
    js_code = f"<script>var msg = new SpeechSynthesisUtterance('{text}'); msg.lang = 'bn-BD'; window.speechSynthesis.speak(msg);</script>"
    st.components.v1.html(js_code, height=0)

if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- ১. পেমেন্ট ও প্যাকেজ সিস্টেম ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #fc3d21;'>NASA x AKASH AI SYSTEM</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>সিস্টেমটি আনলক করতে নিচের প্যাকেজগুলো থেকে একটি বেছে নিন</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="package-card"><h3>Basic</h3><p class="price-tag">৩,০০০ টাকা</p><p>AI Chat Access</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="package-card"><h3>Pro</h3><p class="price-tag">৫,০০০ টাকা</p><p>AI + Automation</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="package-card"><h3>Ultra</h3><p class="price-tag">১০,০০০ টাকা</p><p>Full System Access</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    col_f1, col_f2, col_f3 = st.columns([1, 1.5, 1])
    with col_f2:
        # পেমেন্ট ইনফো সেকশন
        st.markdown("""
        <div class="payment-info">
            <h4 style="color: #00f2ff; margin-bottom: 10px;">💳 পেমেন্ট গেটওয়ে</h4>
            <p style="font-size: 20px; margin: 5px 0;">বিকাশ ও নগদ (পার্সোনাল):</p>
            <h2 style="color: #fc3d21; letter-spacing: 2px;">01967840830</h2>
            <p style="color: #aaa; font-size: 14px;">টাকা পাঠিয়ে TrxID নিচে দিন</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("activation_form"):
            u_name = st.text_input("Candidate Name")
            u_package = st.selectbox("আপনার পছন্দের প্যাকেজ", ["Basic (3000)", "Pro (5000)", "Ultra (10000)"])
            u_trxid = st.text_input("TrxID / Master Key দিন", type="password")
            
            if st.form_submit_button("ভেরিফাই এবং লঞ্চ মিশন"):
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
                    st.success("Payment Verified!")
                    speak_text(f"ধন্যবাদ {u_name}. আপনার পেমেন্ট সফল হয়েছে.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("ভুল TrxID! দয়া করে পেমেন্ট সম্পন্ন করে সঠিক আইডি দিন।")

# --- ২. মেইন কমান্ড সেন্টার (লগইন করার পর) ---
else:
    st.markdown(f"<h2 style='text-align: center; color: #fc3d21;'>AI LIVE MISSION CONTROL</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💬 AI Voice Assistant", "🛰️ App Control", "⚙️ Admin Settings"])

    with tab1:
        st.subheader(f"🤖 কমান্ড দিন {st.session_state.user_name}")
        user_input = st.chat_input("Ask anything...")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            reply = f"বুঝেছি {st.session_state.user_name}, আপনার কমান্ডটি প্রসেস করা হচ্ছে।"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            speak_text(reply)

        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])

    with tab2:
        st.subheader("📲 অ্যাপ অটোমেশন")
        if st.button("Messenger Auto-Reply Active"):
            st.success("Active")
            speak_text("মেসেঞ্জার অটোমেশন চালু হয়েছে।")

    with tab3:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

st.markdown("<p style='text-align: center; color: #555;'>Developer: Akash | NASA AI Live v2.0</p>", unsafe_allow_html=True)
