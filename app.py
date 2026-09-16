import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
if "shop" not in st.session_state:
    st.session_state.shop = []

ECOCASH = "0783949268"
WA = "263783949268"

st.title("Harare Hub 🇿🇼 | Harare's Marketplace")
t_shop, t_sell, t_boost = st.tabs(["🛒 SHOP", "📦 SELL", "💰 ADVERTISE $5+"])

with t_sell:
    with st.container(border=True):
        st.subheader("Add Product - Free")
        c1,c2 = st.columns(2)
        with c1:
            name = st.text_input("Product Name*")
            price = st.text_input("Price*")
            stock = st.number_input("In Stock*", 1, 1000, 10)
        with c2:
            loc = st.selectbox("Location", ["CBD","Borrowdale","Avondale","Mbare","Highfields","Chitungwiza","Other"])
            phone = st.text_input("Your WhatsApp* (078...)")
            photo = st.file_uploader("Photo*", type=["jpg","png","jpeg"])
        if st.button("PUBLISH FREE", type="primary", use_container_width=True):
            if all([name][price][phone][photo]):
                st.session_state.shop.append({
                    "name":name,"price":price,"stock":stock,"loc":loc,"phone":phone,
                    "img":photo.getvalue(),"boost":0,"expiry":None
                })
                st.success("Free product published! Now BOOST it in ADVERTISE tab to get sales FAST")
                st.balloons()

with t_shop:
    q = st.text_input("🔍 What are you looking for?", placeholder="iPhone, TV, Shoes...")
    # Sort: boosted first
    def is_active(p):
        if p.get("expiry") and datetime.now() > p["expiry"]:
            p["boost"]=0
            return False
        return p.get("boost",0) > 0

    boosted = [p for p in st.session_state.shop if is_active(p)]
    normal = [p for p in st.session_state.shop if not is_active(p)]
    # Sort boosted by higher package first
    boosted = sorted(boosted, key=lambda x: x["boost"], reverse=True)
    all_p = boosted + normal

    if not all_p:
        st.info("No products yet. Be first to sell!")
    else:
        cols = st.columns(2)
        for i,p in enumerate(all_p):
            if q.lower() in p["name"].lower():
                with cols[i%2]:
                    with st.container(border=True):
                        if is_active(p):
                            days_left = (p["expiry"] - datetime.now()).days + 1
                            st.markdown(f"⭐ **FEATURED** - {days_left} days left")
                        st.image(p["img"], use_container_width=True)
                        st.write(f"**{p['name']}**")
                        st.caption(f"💰 {p['price']} | 📦 {p['stock']} left | 📍 {p['loc']}")
                        link = f"https://wa.me/263{p['phone'][-9:]}?text=Hi,%20I%20want%20{p['name']}%20from%20Harare%20Hub"
                        st.link_button("Chat Seller 📱", link, use_container_width=True, type="primary")

with t_boost:
    st.subheader("💰 Advertise Packages")
    st.success(f"Pay EcoCash: {ECOCASH} - Name: Munashe")

    with st.container(border=True):
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown("### $5 Package")
            st.write("✅ Top of Shop\n✅ 7 Days\n✅ ⭐ Badge")
        with c2:
            st.markdown("### $10 Package")
            st.write("🔥 Top + Status Post\n✅ 14 Days\n✅ Double Views")
        with c3:
            st.markdown("### $20 Package")
            st.write("👑 VIP Banner\n✅ 30 Days\n✅ WhatsApp Broadcast")

        st.divider()
        prod = st.selectbox("Which product to advertise?", [p["name"] for p in st.session_state.shop] if st.session_state.shop else ["Add product in SELL tab first"])
        plan = st.selectbox("Choose Package", ["$5 - 7 Days", "$10 - 14 Days", "$20 - 30 Days"])
        proof = st.file_uploader("Upload EcoCash Proof Screenshot*", type=["jpg","png","jpeg"])

        if st.button("✅ I PAID - ACTIVATE NOW", type="primary", use_container_width=True):
            if not proof or prod.startswith("Add"):
                st.error("Upload proof & add product first")
            else:
                days = 7 if "$5" in plan else 14 if "$10" in plan else 30
                boost_val = 1 if days==7 else 2 if days==14 else 3
                for p in st.session_state.shop:
                    if p["name"] == prod:
                        p["boost"] = boost_val
                        p["expiry"] = datetime.now() + timedelta(days=days)
                st.success(f"✅ {prod} boosted for {days} days! Customers will see it FIRST now!")
                st.link_button("Send Proof to Admin WhatsApp", f"https://wa.me/{WA}?text=Hi%20Admin,%20I%20paid%20{plan}%20for%20{prod}.%20EcoCash%20{prod}", use_container_width=True)
                st.balloons()

    st.info("**How it works:**\n1. EcoCash $5/$10/$20 to 0783949268\n2. Upload screenshot here\n3. We verify & your product jumps to TOP automatically\n4. You get more WhatsApp orders")

st.caption("Share app: ertdr4tsrvec.streamlit.app | Support: 0783949268")
