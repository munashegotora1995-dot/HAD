import streamlit as st

st.set_page_config(page_title="Harare Hub 🇿🇼", page_icon="🛒", layout="wide")

# HEADER
st.title("Harare Hub 🇿🇼")
st.markdown("#### Sell Anything in Harare | WhatsApp: 0783949268")
MY_WA = "263783949268"

# --- SUPER EASY UPLOAD BOX ---
st.markdown("### 📸 Add New Product")
with st.container(border=True):
    with st.form("sell_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Product Name *", placeholder="e.g. iPhone 13")
            price = st.text_input("Price *", placeholder="e.g. $450")
        with col2:
            loc = st.text_input("Location", placeholder="e.g. Harare CBD")
            photo = st.file_uploader("📷 Product Photo *", type=["jpg","png","jpeg"], help="Tap to choose from gallery")
        
        # BIG FRIENDLY BUTTON
        add_btn = st.form_submit_button("🚀 ADD TO MY SHOP", type="primary", use_container_width=True)
        
        if add_btn:
            if not name or not price or not photo:
                st.error("Please fill Name, Price AND Photo")
            else:
                if "myprods" not in st.session_state:
                    st.session_state.myprods = []
                st.session_state.myprods.append({"name":name,"price":price,"loc":loc,"photo":photo})
                st.success(f"✅ {name} added!")
                st.balloons()

# --- PRODUCTS GRID ---
st.divider()
st.subheader("🛒 My Shop")
search = st.text_input("🔍 Search products", placeholder="Type iPhone, TV...")

# Default demo products
defaults = [
    {"name":"iPhone 13 128GB","price":"$450","loc":"CBD","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"},
    {"name":"Samsung TV 55\"","price":"$350","loc":"Borrowdale","img":"https://images.unsplash.com/photo-1593359677879-a4bb92f367d8?w=400"},
]

all_items = []
if "myprods" in st.session_state:
    all_items.extend(st.session_state.myprods)
all_items.extend(defaults)

# Filter
filtered = [p for p in all_items if search.lower() in p["name"].lower()]

if not filtered:
    st.info("No products found. Add your first one above! 👆")

cols = st.columns(2)
for i, p in enumerate(filtered):
    with cols[i % 2]:
        with st.container(border=True):
            if "photo" in p:
                st.image(p["photo"], use_container_width=True)
            else:
                st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**")
            st.caption(f"💰 {p['price']} | 📍 {p.get('loc','Harare')}")
            wa_link = f"https://wa.me/{MY_WA}?text=Hi%20Munashe%2C%20I%20want%20{p['name']}%20for%20{p['price']}"
            st.link_button("Buy on WhatsApp 📱", wa_link, use_container_width=True, type="primary")

st.divider()
st.link_button("💬 Chat Owner 0783949268", f"https://wa.me/{MY_WA}", use_container_width=True)
