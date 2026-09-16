import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
st.title("Harare Hub 🇿🇼")
st.caption("Harare #1 Marketplace | Owner: Munashe 0713504734")
st.success("✅ Trusted Seller - Fast Delivery in Harare!")

search = st.text_input("🔍 Search products", "", placeholder="iPhone, Nike, TV...")
MY_WA = "263713504734"

products = [
    {"name": "iPhone 13 128GB", "price": "$450", "loc": "CBD", "img": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"},
    {"name": "Nike Air Max", "price": "$85", "loc": "Avondale", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
    {"name": "Samsung 55\" TV", "price": "$350", "loc": "Borrowdale", "img": "https://images.unsplash.com/photo-1593359677879-a4bb92f367d8?w=400"},
    {"name": "Toyota Corolla 2015", "price": "$6500", "loc": "Harare", "img": "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=400"},
    {"name": "HP Laptop Core i5", "price": "$300", "loc": "CBD", "img": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400"},
    {"name": "2 Room to Rent", "price": "$180/mo", "loc": "Budiriro", "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400"},
]

cols = st.columns(2)
for i, p in enumerate(products):
    if search.lower() in p["name"].lower() or search == "":
        with cols[i%2]:
            st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**\n\n💰 {p['price']} | 📍 {p['loc']}")
            msg = f"Hi Munashe! I want {p['name']} for {p['price']}. Still available? Harare Hub"
            link = f"https://wa.me/{MY_WA}?text={msg.replace(' ', '%20').replace(chr(34), '')}"
            st.link_button(f"Buy NOW 📱", link, use_container_width=True, type="primary")
            st.divider()

st.link_button("📱 Chat Owner on WhatsApp", f"https://wa.me/{MY_WA}", use_container_width=True)
st.markdown("**EcoCash: 0713504734 | USD Cash | InnBucks**")
