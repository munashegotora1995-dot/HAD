import streamlit as st

st.set_page_config(page_title="Harare Small Business Hub", page_icon="📢", layout="centered")

st.markdown("""
<style>
.hero {
    background: #0A1931;
    padding: 0;
    border-radius: 20px;
    overflow: hidden;
    text-align: center;
    border: 2px solid #D4AF37;
}
</style>
""", unsafe_allow_html=True)

# DISPLAY YOUR GOLD LOGO
st.image("harare_logo_gold.jpg", use_container_width=True)

st.markdown("""
<div style="text-align:center; margin-top:15px;">
    <h2 style="color:#0A1931;">Harare's Marketplace</h2>
    <p>Connect. Advertise. Grow.</p>
</div>
""", unsafe_allow_html=True)
