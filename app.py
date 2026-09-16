import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
st.title("Harare Hub 🇿🇼")
st.caption("Harare #1 | 0783949268")
MY_WA = "263783949268"

st.sidebar.header("📸 Add Product")
p_name = st.sidebar.text_input("Product Name", "iPhone 13")
p_price = st.sidebar.text_input("Price", "$450")
p_loc = st.sidebar.text_input("Location", "Harare CBD")
p_photo = st.sidebar.file_uploader("Upload YOUR Photo", type=["jpg","jpeg","png"])

if st.sidebar.button("Add Product +", type="primary", use_container_width=True):
    if p_photo:
        if "myprods" not in st.session_state:
            st.session_state.myprods = []
        st.session_state.myprods.append({"name":p_name,"price":p_price,"loc":p_loc,"photo":p_photo})
        st.sidebar.success(f"Added {p_name}!")
        st.rerun()
    else:
        st.sidebar.error("Upload photo first!")

search = st.text_input("🔍 Search", "")

defaults = [
    {"name":"iPhone 13 128GB","price":"$450","loc":"CBD","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"},
    {"name":"Samsung TV 55","price":"$350","loc":"Borrowdale","img":"https://images.unsplash.com/photo-1593359677879-a4bb92f367d8?w=400"},
]

prods = []
if "myprods" in st.session_state:
    prods.extend(st.session_state.myprods)
prods.extend(defaults)

cols = st.columns(2)
for i,p in enumerate(prods):
    if search.lower() in p["name"].lower():
        with cols[i%2]:
            if "photo" in p:
                st.image(p["photo"], use_container_width=True)
            else:
                st.image(p["img"], use_container_width=True)
            st.write(f"**{p['name']}** - {p['price']} - {p['loc']}")
            link = f"https://wa.me/{MY_WA}?text=Hi!%20I%20want%20{p['name']}"
            st.link_button("Buy 📱", link, use_container_width=True)
            st.divider()

st.link_button("Chat 0783949268", f"https://wa.me/{MY_WA}", use_container_width=True)
