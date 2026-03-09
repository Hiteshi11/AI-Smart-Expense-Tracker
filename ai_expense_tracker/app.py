import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)


st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.title{
text-align:center;
font-size:48px;
font-weight:bold;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:#d4d4d4;
margin-bottom:50px;
}

.card-button button{
width:100%;
height:140px;
font-size:20px;
border-radius:18px;
background: rgba(255,255,255,0.08);
border:1px solid rgba(255,255,255,0.2);
backdrop-filter: blur(10px);
color:white;
transition:0.3s;
box-shadow:0px 6px 20px rgba(0,0,0,0.4);
}

.card-button button:hover{
transform:scale(1.05);
background: rgba(255,255,255,0.15);
}

.footer{
text-align:center;
margin-top:60px;
color:#bdbdbd;
}

</style>
""", unsafe_allow_html=True)




# Title
st.markdown(
"""
<div class='big-title'>💰 AI Smart Expense Tracker</div>
<div class='subtitle'>Your AI-powered personal finance assistant</div>
""",
unsafe_allow_html=True
)
# First row
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Dashboard", key="dash"):
        st.switch_page("pages/Dashboard.py")

with col2:
    if st.button("➕ Add Expense", key="add"):
        st.switch_page("pages/Add_Expense.py")

col3, col4 = st.columns(2)

with col3:
    if st.button("🧾 Upload Receipt", key="upload"):
        st.switch_page("pages/Upload_Receipt.py")

with col4:
    if st.button("📈 Analytics", key="analytics"):
        st.switch_page("pages/Analytics.py")

# Footer
st.markdown(
"""
<div class='footer'>
Built with ❤️ 
</div>
""",
unsafe_allow_html=True
)


