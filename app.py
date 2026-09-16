import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
st.title("Harare Hub 🇿🇼")
st.caption("Owner: Munashe | 0783949268")
MY_WA = "263783949268"

# --- ADD YOUR PRODUCT WITH YOUR PHOTO ---
st.sidebar.header("📸 Add Your Product")
with st.sidebar:
    with st.form("add"):
        name = st.text_input("Product Name", "iPhone 13")
        price = st.text_input("Price", "$450")
        loc = st.text_input("Location", "Harare CBD")
        uploaded = st.file_uploader("Upload YOUR Photo", type=["jpg","jpeg","png"])
        add = st.form_submit_button("Add Product +")
        if add:
            if uploaded:
                st.session_state.setdefault("custom", []).append({"name": name, "price": price, "loc": loc, "file": uploaded})
                st.success(f"Added {name}!")
            else:
                st.warning("Please upload photo!")

# --- PRODUCTS ---
search = st.text_input("🔍 Search", "", placeholder="Search...")
default_products = [
    {"name": "iPhone 13 128GB", "price": "$450", "loc": "CBD", "img": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"},
    {"name": "Nike Air Max", "price": "$85", "loc": "Avondale", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
    {"name": "Samsung 55\" TV", "price": "$350", "loc": "Borrowdale", "img": "https://images.unsplash.com/photo-1593359677879-a4bb92f367d8?w=400"},
]

all_products = default_products.copy()
if "custom" in st.session_state:
    for c in st.session_state.custom:
        all_products.insert(0, {"name": c["name"], "price": c["price"], "loc": c["loc"], "file": c["file"]})

cols = st.columns(2)
for i, p in enumerate(all_products):
    if search.lower() in p["name"].lower() or search == "":
        with cols[i%2]:
            if "file" in p:
                st.image(p["file"], use_container_width=True)
            else:
                st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**\n\n💰 {p['price']} | 📍 {p['loc']}")
            msg = f"Hi Munashe! I want {p['name']} for {p['price']}. Harare Hub"
            link = f"https://wa.me/{MY_WA}?text={msg.replace(' ', '%20')}"
            st.link_button(f"Buy NOW 📱", link, use_container_width=True, type="primary")
            st.divider()

st.markdown("---")
st.link_button("📱 WhatsApp 0783949268", f"https://wa.me/{MY_WA}", use_container_width=True)
