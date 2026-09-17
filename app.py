import streamlit as st
import sqlite3, os, uuid
from datetime import datetime

# --- CONFIG WITH YOUR GOLD ICON ---
st.set_page_config(
    page_title="Harare Small Business Hub",
    page_icon="app_icon.png",
    layout="centered"
)

BASE = os.path.dirname(__file__)
DB = os.path.join(BASE, "ads.db")

def init_db():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS ads (
        id TEXT PRIMARY KEY,
        business TEXT,
        title TEXT,
        price TEXT,
        location TEXT,
        whatsapp TEXT,
        description TEXT,
        image TEXT,
        created TIMESTAMP
    )""")
    con.commit()
    con.close()

def fmt_wa(n):
    n = ''.join(filter(str.isdigit, n))
    if n.startswith('0'): n = '263' + n[1:]
    if not n.startswith('263'): n = '263' + n
    return n

def save_img(file):
    if not file: return ""
    ext = file.name.split('.')[-1]
    fname = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(BASE, fname)
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    return fname

init_db()

# --- LUXURY GOLD & NAVY STYLING ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
.stApp {background: #F8F5F0;}
.hero-wrap {
    border: 2px solid #D4AF37;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(10,25,49,0.3);
}
.gold-text {
    font-family: 'Playfair Display', serif;
    color: #D4AF37;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- HERO WITH NAVY GOLD LOGO ---
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.image("harare_navy_gold.jpg", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- SECOND ROW WITH TRANSPARENT LOGO ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo_transparent.png", use_container_width=True)

st.markdown("<h3 style='text-align:center; color:#0A1931;'>Connect. Advertise. Grow.</h3>", unsafe_allow_html=True)

# --- TABS ---
tab1, tab2 = st.tabs(["📢 Browse Ads", "➕ Post Your Business"])

with tab1:
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT * FROM ads ORDER BY created DESC").fetchall()
    con.close()
    if not rows:
        st.info("No ads yet. Be the first to post!")
    for r in rows:
        id,biz,title,price,loc,wa,desc,img,created = r
        with st.container(border=True):
            if img and os.path.exists(os.path.join(BASE, img)):
                st.image(os.path.join(BASE, img))
            st.markdown(f"**{title}** - ${price}")
            st.caption(f"{biz} | {loc}")
            st.write(desc)
            st.link_button(f"💬 WhatsApp {biz}", f"https://wa.me/{fmt_wa(wa)}")

with tab2:
    with st.form("post"):
        biz = st.text_input("Business Name")
        title = st.text_input("What are you selling?")
        price = st.text_input("Price (USD)")
        loc = st.selectbox("Location", ["Harare CBD", "Eastlea", "Avondale", "Borrowdale", "Highfield", "Chitungwiza", "Other"])
        wa = st.text_input("WhatsApp Number")
        desc = st.text_area("Description")
        img = st.file_uploader("Business Photo", type=["jpg","png","jpeg"])
        submit = st.form_submit_button("Post to Hub - $1", type="primary")
        if submit:
            if not all([biz,title,price,wa]):
                st.error("Fill all required fields")
            else:
                img_name = save_img(img)
                con = sqlite3.connect(DB)
                con.execute("INSERT INTO ads VALUES (?,?,?,?,?,?,?,?,?)",
                    (str(uuid.uuid4()), biz, title, price, loc, wa, desc, img_name, datetime.now()))
                con.commit()
                con.close()
                st.success("✅ Posted! Your ad is now live in Harare Hub")
                st.balloons()

# --- FOOTER WITH ICON ---
st.divider()
c1,c2 = st.columns([1,5])
with c1:
    st.image("app_icon.png", width=50)
with c2:
    st.caption("© 2026 Harare Small Business Hub | Gold & Navy Luxury Edition")
