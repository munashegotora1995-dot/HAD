import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")

st.title("Harare Hub 🇿🇼")
st.caption("Harare #1 Marketplace - Owner: Munashe | WhatsApp: 0713504734")
st.success("✅ All orders go to Munashe - Fast delivery in Harare!")

search = st.text_input("🔍 Search", "", placeholder="Search phone, shoes, car...")

MY_WA = "263713504734"

products = [
    {"name": "iPhone 13 128GB", "price": "$450", "loc": "Harare CBD"},
    {"name": "Nike Air Max", "price": "$85", "loc": "Avondale"},
    {"name": "Samsung 55' TV", "price": "$350", "loc": "Borrowdale"},
    {"name": "Toyota Corolla 2015", "price": "$6500", "loc": "Harare"},
    {"name": "HP Laptop Core i5", "price": "$300", "loc": "CBD"},
    {"name": "2 Room to Rent", "price": "$180/month", "loc": "Budiriro"},
]

cols = st.columns(2)
for i, p in enumerate(products):
    if search.lower() in p["name"].lower() or search == "":
        with cols[i%2]:
            st.markdown(f"**{p['name']}**\n\n💰 {p['price']} | 📍 {p['loc']}")
            msg = f"Hi Munashe! I want to buy {p['name']} for {p['price']} on Harare Hub. Is it available?"
            link = f"https://wa.me/{MY_WA}?text={msg.replace(' ', '%20')}"
            st.link_button(f"Buy NOW 📱 - {p['name']}", link, use_container_width=True)
            st.divider()

st.markdown("---")
st.markdown("### 💳 Payments")
st.markdown("**EcoCash:** 0713504734 | **InnBucks | Paynow | USD Cash**")
st.markdown("📍 Delivery in Harare - CBD, Avondale, Borrowdale, Budiriro")
st.link_button("📱 Chat with Owner on WhatsApp", f"https://wa.me/{MY_WA}", use_container_width=True)
