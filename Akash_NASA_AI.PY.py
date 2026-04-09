import streamlit as st

# পেজ সেটআপ এবং নাম
st.set_page_config(page_title="Akash NASA AI", page_icon="🚀", layout="centered")

# উন্নত ডার্ক নিওন সিএসএস (ডিজাইন সুন্দর করার জন্য)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1a1c23; color: #00ffcc; border: 1px solid #00ffcc;
    }
    h1 { color: #00ffcc; text-align: center; text-shadow: 0 0 10px #00ffcc; font-family: 'Arial'; }
    .stButton>button {
        width: 100%; background: linear-gradient(45deg, #00ffcc, #0080ff);
        color: white; font-weight: bold; border-radius: 10px; border: none; height: 50px;
    }
    .payment-card {
        background-color: #161b22; padding: 20px; border-radius: 15px;
        border: 1px solid #30363d; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Akash NASA AI - Payment Dashboard")
st.write("<p style='text-align: center; color: #8b949e;'>স্বাগতম! আপনার পেমেন্ট এবং অর্ডার ফরমটি নির্ভুলভাবে পূরণ করুন।</p>", unsafe_allow_html=True)

# পেমেন্ট মেথড সেকশন (বিকাশ ও নগদ প্রদর্শন)
st.markdown("### 💳 পেমেন্ট করার মাধ্যম")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='background-color: #d12053; padding: 15px; border-radius: 10px; color: white; text-align: center;'>
        <b>bKash (Personal)</b><br>01967840830
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color: #f7941d; padding: 15px; border-radius: 10px; color: white; text-align: center;'>
        <b>Nagad (Personal)</b><br>01967840830
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# অর্ডার ফরম
st.markdown("### 📝 অর্ডারের তথ্য পূরণ করুন")
with st.container():
    name = st.text_input("আপনার পুরো নাম")
    phone = st.text_input("আপনার মোবাইল নম্বর")
    amount = st.number_input("টাকার পরিমাণ (৫,০০০ টাকা)", min_value=0, value=5000)
    method = st.selectbox("পেমেন্ট মাধ্যম সিলেক্ট করুন", ["bKash", "Nagad"])
    trx_id = st.text_input("ট্রানজেকশন আইডি (TrxID)")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Confirm Order"):
    if name and phone and trx_id:
        st.balloons()
        st.success(f"ধন্যবাদ {name}! আপনার পেমেন্ট রিকোয়েস্টটি সফলভাবে আকাশের কাছে পাঠানো হয়েছে।")
        
        # সামারি বক্স
        st.info(f"""
        **অর্ডার সামারি:**
        - গ্রাহক: {name}
        - মাধ্যম: {method}
        - পরিমাণ: {amount} টাকা
        - TrxID: {trx_id}
        """)
    else:
        st.error("দয়া করে ফরমের সবগুলো তথ্য সঠিকভাবে পূরণ করুন।")
