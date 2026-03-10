import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)


st.markdown("""
<style>


.stApp{
background: linear-gradient(135deg,#141E30,#243B55);
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
color:#cfcfcf;
margin-bottom:50px;
}

.card{
background: rgba(255,255,255,0.08);
border-radius:20px;
padding:45px;
text-align:center;
backdrop-filter: blur(12px);
border:1px solid rgba(255,255,255,0.15);
box-shadow:0px 10px 35px rgba(0,0,0,0.4);
transition: all 0.35s ease;
}

.card:hover{
transform: translateY(-8px) scale(1.04);
box-shadow:0px 20px 50px rgba(0,0,0,0.6);
}

.card h2{
color:white;
margin-bottom:12px;
font-size:26px;
}

.card p{
color:#d1d1d1;
font-size:15px;
}

.card-icon{
font-size:40px;
margin-bottom:15px;
}

a{
text-decoration:none !important;
color:inherit;
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
    st.markdown("""
    <a href="/Dashboard" target="_self">
    <div class="card">
        <div class="card-icon">📊</div>
        <h2>Dashboard</h2>
        <p>View your financial overview</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Add_Expense" target="_self">
    <div class="card">
        <div class="card-icon">➕</div>
        <h2>Add Expense</h2>
        <p>Add manual expenses easily</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <a href="/Upload_Receipt" target="_self">
    <div class="card">
        <div class="card-icon">🧾</div>
        <h2>Upload Receipt</h2>
        <p>Scan receipts using AI OCR</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Analytics" target="_self">
    <div class="card">
        <div class="card-icon">📈</div>
        <h2>Analytics</h2>
        <p>Analyze your spending patterns</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown(
"""
<div class='footer'>
Built with ❤️ 
</div>
""",
unsafe_allow_html=True
)




