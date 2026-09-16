import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")
st.title("Harare Hub 🇿🇼")
st.caption("WhatsApp Orders: 0783949268")
MY_WA = "263783949268"

# --- EASY UPLOAD - FIXED ---
st.markdown("### 📸 Add Product")
if "myprods" not in st.session_state:
    st.session_state.myprods = []

with st.container(border=True):
    name = st.text_input("Product Name", placeholder="iPhone 13")
    price = st.text_input("Price", placeholder="$450")
    loc = st.text_input("Location", placeholder="Harare CBD")
    photo = st.file_uploader("Choose Photo from Gallery", type=["jpg","jpeg","png"])

    if photo:
        st.image(photo, caption="Preview", width=200)
    
    if st.button("🚀 ADD TO SHOP", type="primary", use_container_width=True):
        if not photo:
            st.error("❌ Please choose a photo first!")
        elif not name or not price:
            st.error("❌ Fill Name and Price!")
        else:
            # SAVE AS BYTES - This never fails
            st.session_state.myprods.append({
                "name": name,
                "price": price,
                "loc": loc,
                "img_bytes": photo.getvalue()  # <-- FIX
            })
            st.success(f"✅ {name} added to shop!")
            st.balloons()

# --- SHOW SHOP ---
st.divider()
st.subheader(f"My Shop ({len(st.session_state.myprods)} products)")
search = st.text_input("🔍 Search")

defaults = [
    {"name":"iPhone 13 Demo","price":"$450","loc":"CBD","url":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"},
]

all_prods = st.session_state.myprods + defaults

cols = st.columns(2)
for i, p in enumerate(all_prods):
    if search.lower() in p["name"].lower():
        with cols[i%2]:
            with st.container(border=True):
                if "img_bytes" in p:
                    st.image(p["img_bytes"], use_container_width=True)
                else:
                    st.image(p["url"], use_container_width=True)
                st.write(f"**{p['name']}**")
                st.caption(f"{p['price']} | {p['loc']}")
                link = f"https://wa.me/{MY_WA}?text=Hi!%20I%20want%20{p['name']}%20{p['price']}"
                st.link_button("Buy 📱", link, use_container_width=True)

st.link_button("Chat 0783949268", f"https://wa.me/{MY_WA}", use_container_width=True)
