import streamlit as st
import pandas as pd

# পেজ সেটআপ
st.set_page_config(page_title="Akash NASA AI", layout="centered")

# ডার্ক নিওন স্টাইল
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ffcc; }
    h1 { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Akash NASA AI - Payment Dashboard")
st.write("নিচে আপনার অর্ডারের তথ্য পূরণ করুন।")

# ইনপুট ফিল্ড
name = st.text_input("আপনার নাম লিখুন")
phone = st.text_input("আপনার মোবাইল নম্বর")
amount = st.number_input("টাকার পরিমাণ", min_value=1)
method = st.selectbox("পেমেন্ট মাধ্যম", ["Bkash", "Nagad", "Rocket"])
trx_id = st.text_input("Transaction ID (TrxID)")

if st.button("Confirm Order"):
    if name and phone and trx_id:
        # এখানে আপনার কাঙ্ক্ষিত সঠিক কোডটি দেওয়া হলো যা এরর দেবে না
        st.success(f"ধন্যবাদ {name}! আপনার {amount} টাকার অর্ডারটি সফলভাবে গ্রহণ করা হয়েছে।")
        st.balloons()
    else:
        st.error("দয়া করে সব তথ্য সঠিকভাবে পূরণ করুন।")
