import streamlit as st

# পেজ সেটআপ (ট্যাব নাম এবং আইকন)
st.set_page_config(page_title="Akash NASA AI | Terminal", page_icon="🌌", layout="centered")

# --- ADVANCED NASA AI CSS (THEME & DESIGN) ---
st.markdown("""
<style>
    /* Background & Font */
    @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&display=swap');
    
    .stApp {
        background: #000000 url('https://www.transparenttextures.com/patterns/stardust.png');
        font-family: 'Source Code Pro', monospace;
        color: #e0f7fa;
    }

    /* Neon Title & Logo */
    .title-container {
        text-align: center;
        padding: 20px;
        margin-bottom: 30px;
    }
    .neon-logo {
        font-size: 70px;
        color: #00e676;
        text-shadow: 0 0 10px #00e676, 0 0 20px #00e676, 0 0 30px #00c853;
        margin-bottom: 10px;
    }
    .neon-text {
        font-size: 35px;
        color: #81d4fa;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 5px #81d4fa, 0 0 15px #0277bd;
    }
    .subtitle-text {
        color: #b0bec5;
        font-size: 14px;
    }

    /* Glassmorphism Cards */
    .css-1r6slb0, .css-k7v04j { /* Container and Column */
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }

    /* Input Fields Style */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: #00e676 !important;
        border: 1px solid #01579b !important;
        border-radius: 5px;
        transition: all 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00e676 !important;
        box-shadow: 0 0 10px #00e676 !important;
    }

    /* Payment Methods Buttons (Bkash/Nagad) */
    .pm-btn {
        display: block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        color: white;
        transition: transform 0.2s;
        text-decoration: none;
    }
    .pm-btn:hover { transform: scale(1.05); }
    .bkash-btn { background: linear-gradient(45deg, #d12053, #e91e63); box-shadow: 0 0 10px #d12053; }
    .nagad-btn { background: linear-gradient(45deg, #f7941d, #ff5722); box-shadow: 0 0 10px #f7941d; }

    /* NASA Confirm Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #0277bd, #00e676);
        color: white;
        font-weight: bold;
        font-size: 18px;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 30px;
        border: none;
        height: 55px;
        box-shadow: 0 0 15px rgba(0, 230, 118, 0.5);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #00e676, #0277bd);
        box-shadow: 0 0 25px rgba(0, 230, 118, 0.8);
        transform: translateY(-2px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #546e7a;
        font-size: 12px;
        margin-top: 50px;
        border-top: 1px solid #1c313a;
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
<div class="title-container">
    <div class="neon-logo">🌐</div>
    <div class="neon-text">Akash NASA AI</div>
    <div class="subtitle-text">Quantum Payment Terminal v1.0 | Bangladesh Security Protocol</div>
</div>
""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- PAYMENT METHODS ---
st.markdown("### 📡 Active Payment Channels")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="css-1r6slb0">
        <div style='text-align: center; color: #b0bec5; font-size: 12px;'>CHANNEL-01</div>
        <a href="#" class="pm-btn bkash-btn">bKash Personal<br>01967840830</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="css-1r6slb0">
        <div style='text-align: center; color: #b0bec5; font-size: 12px;'>CHANNEL-02</div>
        <a href="#" class="pm-btn nagad-btn">Nagad Personal<br>01967840830</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- ORDER FORM ---
st.markdown("### 📝 Secure Order Manifest")
with st.container():
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        name = st.text_input("Full Name / Client ID", placeholder="Ex: Akash Ahmed")
    with col_f2:
        phone = st.text_input("Contact Number", placeholder="Ex: 017xxxxxxxx")
    
    col_f3, col_f4 = st.columns(2)
    with col_f3:
        amount = st.number_input("Transaction Amount (BDT)", min_value=1, value=5000)
    with col_f4:
        method = st.selectbox("Payment Gateway", ["bKash", "Nagad"])
    
    trx_id = st.text_input("Transaction ID (TrxID)", placeholder="Ex: A1B2C3D4E5")

st.markdown("<br>", unsafe_allow_html=True)

# --- CONFIRM BUTTON ---
if st.button("Initialize Secure Order"):
    if name and phone and trx_id:
        st.balloons()
        st.success(f"SUCCESS: Operation Confirmed. Thank you, {name}. Your request is being processed.")
        
        # summary 
        st.markdown(f"""
        <div class="css-1r6slb0" style="border: 1px solid #00e676; color: #00e676; padding: 15px;">
            <b>TRANSACTION SUMMARY:</b><br>
            - Client: {name}<br>
            - Gateway: {method}<br>
            - Amount: {amount} BDT<br>
            - TrxID: {trx_id}<br>
            - Status: PENDING VERIFICATION
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("ERROR: Incomplete Manifest. Please fill all fields.")

# --- FOOTER ---
st.markdown("""
<div class="footer">
    Akash NASA AI • Secure Terminal • Unauthorized Access Prohibited
</div>
""", unsafe_allow_html=True)
