import streamlit as st

# --- আপনার সেটিংস ---
MY_NUMBER = "01967840830"  # আপনার বিকাশ ও নগদ নম্বর
AI_NAME = "Akash NASA AI"  # আপনার এআই ব্র্যান্ডের নাম

# পেজ সেটআপ
st.set_page_config(page_title=AI_NAME, page_icon="🚀", layout="centered")

# মূল ইন্টারফেস শুরু
st.markdown(f"<h1 style='text-align: center; color: #0047AB;'>🚀 {AI_NAME}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>স্বাগতম! <b>{AI_NAME}</b> এক্টিভেট করতে নিচের পেমেন্ট ও অর্ডার ফর্মটি সম্পন্ন করুন।</p>", unsafe_allow_html=True)

st.markdown("---")

# পেমেন্ট মেথড সেকশন
st.subheader("🏦 পেমেন্ট করার মাধ্যম")
st.info(f"নিচের যেকোনো একটি নম্বরে **৫,০০০ টাকা** 'Send Money' করুন।")

col1, col2 = st.columns(2)

with col1:
    # বিকাশ লোগো এবং নম্বর
    st.image("https://www.logo.wine/a/logo/BKash/BKash-Logo.wine.svg", width=150)
    st.markdown(f"**বিকাশ (Personal):** \n### {MY_NUMBER}")

with col2:
    # নগদ লোগো এবং নম্বর
    st.image("https://www.logo.wine/a/logo/Nagad/Nagad-Logo.wine.svg", width=150)
    st.markdown(f"**নগদ (Personal):** \n### {MY_NUMBER}")

st.markdown("---")

# অর্ডার ফর্ম সেকশন
st.subheader("📝 অর্ডারের তথ্য পূরণ করুন")
st.write(f"<b>{AI_NAME}</b> ব্যবহারের জন্য নিচের ফর্মটি সঠিক তথ্য দিয়ে পূরণ করে সাবমিট করুন।", unsafe_allow_html=True)

with st.form("order_details"):
    name = st.text_input("আপনার পুরো নাম", placeholder="যেমন: শান্ত")
    sender_num = st.text_input("যে নম্বর থেকে টাকা পাঠিয়েছেন", placeholder="01XXXXXXXXX")
    user_pass = st.text_input(f"{AI_NAME} লগইন করার জন্য একটি পাসওয়ার্ড দিন", type="password", help="এই পাসওয়ার্ড দিয়ে পরে আপনি লগইন করবেন")
    trx_id = st.text_input("Transaction ID (যদি থাকে)", placeholder="TrxID")
    
    submitted = st.form_submit_button("অর্ডার কনফার্ম করুন")

    if submitted:
        if name and sender_num and user_pass:
            st.success(f"ধন্যবাদ {name}! আপনার পেমেন্ট রিকোয়েস্টটি আকাশের কাছে পাঠানো হয়েছে।")
            st.balloons()
            
            # অর্ডারের সামারি
            st.markdown("### ✅ আপনার অর্ডার সামারি:")
            st.code(f"ব্র্যান্ড: {AI_NAME}\nক্রেতার নাম: {name}\nপ্রেরক নম্বর: {sender_num}\nসেট করা পাসওয়ার্ড: {user_pass}\nট্রানজেকশন আইডি: {trx_id}")
            
            st.warning(f"আকাশ আপনার পেমেন্ট চেক করে খুব শীঘ্রই আপনার <b>{AI_NAME}</b> এক্টিভেট করে দিবে।", unsafe_allow_html=True)
        else:
            st.error("দয়া করে নাম, নম্বর এবং পাসওয়ার্ড—এই তিনটি তথ্য অবশ্যই পূরণ করুন।")

# ফুটার
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>© ২০২৬ {AI_NAME} ডেভেলপমেন্ট সার্ভিস - ময়মনসিংহ, বাংলাদেশ।</p>", unsafe_allow_html=True)