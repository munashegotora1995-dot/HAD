import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
st.title("Harare Hub 🇿🇼")
st.caption("0783949268 - Fast Delivery")
MY_WA = "263783949268"

# --- UPLOAD AREA - MAIN PAGE NOW ---
st.header("📸 Add Your Product")
c1, c2 = st.columns(2)
with c1:
    p_name = st.text_input("Product Name", "iPhone 13")
    p_price = st.text_input("Price", "$450")
    p_loc = st.text_input("Location", "Harare CBD")
with c2:
    p_photo = st.file_uploader("Tap to Upload Photo", type=["jpg","jpeg","png"], key="up")

if p_photo:
    st.image(p_photo, width=200)
    if st.button(f"✅ ADD {p_name} TO SHOP", type="primary", use_container_width=True):
        if "myprods" not in st.session_state:
            st.session_state.myprods = []
        st.session_state.myprods.append({"name":p_name,"price":p_price,"loc":p_loc,"photo":p_photo})
        st.success("ADDED! Scroll down to see it!")
        st.balloons()

# --- SHOW PRODUCTS ---
st.divider()
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
            st.write(f"**{p['name']}** - {p['price']}")
            st.link_button("Buy 📱", f"https://wa.me/{MY_WA}?text=Hi!%20I%20want%20{p['name']}", use_container_width=True)
            st.divider()
