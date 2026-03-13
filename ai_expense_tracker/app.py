import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)


st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#f5f7fa,#e4ecf7);
color:#333;
}

.title{
text-align:center;
font-size:48px;
font-weight:bold;
margin-bottom:10px;
color:#2c3e50;
}

.subtitle{
text-align:center;
color:#6b7c93;
margin-bottom:50px;
}

.card{
background:#ffffff;
border-radius:20px;
padding:40px;
text-align:center;
box-shadow:0px 10px 25px rgba(0,0,0,0.08);
transition:0.3s;
border:1px solid #eef2f7;
}

.card:hover{
transform: translateY(-6px);
box-shadow:0px 18px 35px rgba(0,0,0,0.12);
}

.card h2{
color:#2c3e50;
margin-bottom:10px;
}

.card p{
color:#6b7c93;
}

.card-icon{
font-size:38px;
margin-bottom:15px;
}

a{
text-decoration:none !important;
color:inherit;
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





