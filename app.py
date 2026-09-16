import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Harare Small Business Hub", page_icon="📢", layout="wide")

# BLUE & GOLD THEME
st.markdown("""
<style>
    .stApp { background-color: #0A1931; }
    h1, h2, h3 { color: #D4AF37 !important; }
    .main-header {
        background: linear-gradient(135deg, #0A1931 0%, #1A3A5F 100%);
        border: 3px solid #D4AF37;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }
    .stTabs [data-baseweb="tab"] { color: #D4AF37; font-weight: bold; }
    .stButton>button { background: #D4AF37; color: #0A1931; font-weight: bold; }
    div[data-testid="stContainer"] { border-color: #D4AF37 !important; }
</style>
""", unsafe_allow_html=True)

if "shop" not in st.session_state:
    st.session_state.shop = []

ECOCASH = "0783949268"
WA = "263783949268"

# ONLY ONE HEADER - BIG WORDS, BLUE & GOLD, NO FLAG, NO LOGO
st.markdown("""
<div class="main-header">
    <h1 style="font-size:42px; margin:0; letter-spacing:4px; color:#D4AF37;">HARARE SMALL BUSINESS HUB</h1>
    <p style="color:#FFFFFF; font-size:16px; margin-top:10px;">Empowering Harare Businesses | Advertise from $5</p>
    <p style="color:#D4AF37; font-size:14px;">🔵 Blue & Gold Premium Brand</p>
</div>
""", unsafe_allow_html=True)

t_shop, t_sell, t_ads = st.tabs(["🛒 SHOP", "📦 SELL", "💰 ADVERTISE"])

with t_sell:
    with st.container(border=True):
        st.subheader("Add Product FREE")
        c1,c2 = st.columns(2)
        with c1:
            name = st.text_input("Product*")
            price = st.text_input("Price*")
            stock = st.number_input("Stock*", 1, 1000, 10)
        with c2:
            loc = st.selectbox("Location", ["CBD","Borrowdale","Avondale","Mbare","Highfields","Chitungwiza"])
            phone = st.text_input("WhatsApp*")
            photo = st.file_uploader("Photo*", type=["jpg","png","jpeg"])
        if st.button("PUBLISH FREE", type="primary", use_container_width=True):
            if name and price and phone and photo:
                st.session_state.shop.append({"name":name,"price":price,"stock":stock,"loc":loc,"phone":phone,"img":photo.getvalue(),"boost":0,"expiry":None})
                st.success("Published!"); st.balloons()

with t_shop:
    q = st.text_input("What are you looking for?", placeholder="iPhone, TV, Shoes...")
    def active(p):
        if p.get("expiry") and datetime.now() > p["expiry"]:
            p["boost"]=0; return False
        return p.get("boost",0)>0
    boosted = sorted([p for p in st.session_state.shop if active(p)], key=lambda x: x["boost"], reverse=True)
    normal = [p for p in st.session_state.shop if not active(p)]
    if not boosted+normal:
        st.info("No products yet. Be first to sell!")
    cols = st.columns(2)
    for i,p in enumerate(boosted+normal):
        if q.lower() in p["name"].lower():
            with cols[i%2]:
                with st.container(border=True):
                    if active(p):
                        st.markdown(f"<span style='color:#D4AF37;'>⭐ FEATURED - {(p['expiry']-datetime.now()).days+1} days left</span>", unsafe_allow_html=True)
                    st.image(p["img"], use_container_width=True)
                    st.write(f"**{p['name']}** - {p['price']} | {p['loc']}")
                    st.link_button("Chat Seller 📱", f"https://wa.me/263{p['phone'][-9:]}?text=Hi,%20{p['name']}", use_container_width=True, type="primary")

with t_ads:
    st.markdown("### <span style='color:#D4AF37;'>💰 Advertising Packages</span>", unsafe_allow_html=True)
    st.success(f"EcoCash: {ECOCASH}")
    c1,c2,c3 = st.columns(3)
    with c1: st.info("**$5**\n7 Days")
    with c2: st.info("**$10**\n14 Days")
    with c3: st.info("**$20**\n30 Days")
    prod = st.selectbox("Your Product", [p["name"] for p in st.session_state.shop] if st.session_state.shop else ["Add product first"])
    plan = st.selectbox("Package", ["$5 - 7 Days","$10 - 14 Days","$20 - 30 Days"])
    proof = st.file_uploader("EcoCash Proof", type=["jpg","png","jpeg"])
    if st.button("✅ ACTIVATE NOW", type="primary", use_container_width=True):
        if proof and not prod.startswith("Add"):
            d = 7 if "$5" in plan else 14 if "$10" in plan else 30
            b = 1 if d==7 else 2 if d==14 else 3
            for p in st.session_state.shop:
                if p["name"]==prod:
                    p["boost"]=b; p["expiry"]=datetime.now()+timedelta(days=d)
            st.success(f"Boosted {d} days!")
            st.link_button("Send Proof to Admin", f"https://wa.me/{WA}?text=Paid%20{plan}%20for%20{prod}", use_container_width=True)

st.caption("Harare Small Business Hub | ertdr4tsrvec.streamlit.app | Support: 0783949268")
