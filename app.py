
import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")

st.title("Harare Hub 🇿🇼")
st.caption("Harare #1 Marketplace - Live on WhatsApp")

search = st.text_input("🔍 Search", "", placeholder="Search phone, shoes, car...")

products = [
    {"name": "iPhone 13 128GB", "price": "$450", "loc": "Harare CBD", "wa": "263771234567"},
    {"name": "Nike Air Max", "price": "$85", "loc": "Avondale", "wa": "263772345678"},
    {"name": "Samsung 55' TV", "price": "$350", "loc": "Borrowdale", "wa": "263773456789"},
    {"name": "Toyota Corolla 2015", "price": "$6500", "loc": "Harare", "wa": "263774567890"},
]

cols = st.columns(2)
for i, p in enumerate(products):
    if search.lower() in p["name"].lower() or search == "":
        with cols[i%2]:
            st.markdown(f"**{p['name']}**\n\n💰 {p['price']} | 📍 {p['loc']}")
            link = f"https://wa.me/{p['wa']}?text=Hi, I want {p['name']} from Harare Hub"
            st.link_button(f"Buy {p['name']} 📱", link, use_container_width=True)
            st.divider()

st.success("Share your shop: ertdr4tsrvec.streamlit.app")
st.markdown("💳 EcoCash | InnBucks | Paynow | USD Cash")
