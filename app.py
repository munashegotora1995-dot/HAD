import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
if "shop" not in st.session_state:
    st.session_state.shop = []

MY_ECOCASH = "0783949268"
MY_WA = "263783949268"

st.title("Harare Hub 🇿🇼")
tab_shop, tab_sell, tab_ads = st.tabs(["🛒 SHOP", "📦 SELL FREE", "💰 ADVERTISE / BOOST"])

with tab_sell:
    st.subheader("Add Product - Free")
    with st.container(border=True):
        c1,c2 = st.columns(2)
        with c1:
            pname = st.text_input("Product Name*")
            price = st.text_input("Price*")
            stock = st.number_input("Stock", 1, 1000, 5)
        with c2:
            loc = st.text_input("Location*", "CBD")
            phone = st.text_input("Your WhatsApp*")
            photo = st.file_uploader("Photo*", type=["jpg","png","jpeg"])
        if st.button("PUBLISH FREE", type="primary", use_container_width=True):
            if all([pname, price, phone, photo]):
                st.session_state.shop.append({
                    "name":pname,"price":price,"stock":stock,"loc":loc,"phone":phone,
                    "img":photo.getvalue(),"boost":False,"date":datetime.now()
                })
                st.success("Published! Now go to ADVERTISE tab to BOOST to top!")
                st.balloons()

with tab_shop:
    q = st.text_input("🔍 Search what you want")
    # Show boosted first
    boosted = [p for p in st.session_state.shop if p.get("boost")]
    normal = [p for p in st.session_state.shop if not p.get("boost")]
    all_sorted = boosted + normal

    cols = st.columns(2)
    for i,p in enumerate(all_sorted):
        if q.lower() in p["name"].lower():
            with cols[i%2]:
                with st.container(border=True):
                    if p.get("boost"):
                        st.markdown("⭐ **FEATURED - SPONSORED**")
                    st.image(p["img"], use_container_width=True)
                    st.write(f"**{p['name']}** - {p['price']}")
                    st.caption(f"📦 {p['stock']} left | 📍 {p['loc']}")
                    wa = f"https://wa.me/263{p['phone'][-9:]}?text=Hi,%20I%20want%20{p['name']}"
                    st.link_button("Buy on WhatsApp", wa, use_container_width=True, type="primary")

with tab_ads:
    st.subheader("💰 Make More Sales - Advertise")
    st.info(f"EcoCash Payment Number: {MY_ECOCASH} (Munashe)")

    with st.container(border=True):
        st.markdown("### 🔥 BOOST YOUR PRODUCT TO TOP")
        st.write("**$2** = Top of Shop for 7 days. Customers see you FIRST.")
        st.write("**$5** = Featured Banner + We post to our WhatsApp Status (5k views)")

        prod_to_boost = st.selectbox("Which product to boost?", [p["name"] for p in st.session_state.shop] if st.session_state.shop else ["No products yet - Add in SELL tab"])
        plan = st.radio("Choose Plan", ["$2 BOOST 7 Days", "$5 FEATURED 14 Days", "$15 Verified Shop Monthly"])
        proof = st.file_uploader("Upload EcoCash SMS Screenshot / Payment Proof", type=["jpg","png","jpeg"])

        if st.button("✅ I HAVE PAID - ACTIVATE BOOST", use_container_width=True, type="primary"):
            if proof:
                # In real app, you manually verify. For now auto-boost
                for p in st.session_state.shop:
                    if p["name"] == prod_to_boost:
                        p["boost"] = True
                st.success("Payment received! Your product is now BOOSTED to top! We will verify EcoCash in 5 mins.")
                st.link_button("Send Proof to Admin on WhatsApp", f"https://wa.me/{MY_WA}?text=Hi,%20I%20paid%20{plan}%20for%20{prod_to_boost}.%20My%20EcoCash%20is%20...", use_container_width=True)
            else:
                st.error("Upload EcoCash proof first")

    st.divider()
    st.markdown("#### How Business Owners Pay You:")
    st.write(f"1. EcoCash: Dial *151*1*1*{MY_ECOCASH}*{plan.split()[0][1:]}#\n2. Screenshot SMS\n3. Upload proof here + WhatsApp us\n4. You verify on EcoCash app and tap approve")
    st.write("**No automatic payment needed - You verify manually. Easy for Zimbabwe!**")

st.divider()
st.caption(f"Support: {MY_ECOCASH} | Link to share: ertdr4tsrvec.streamlit.app")
