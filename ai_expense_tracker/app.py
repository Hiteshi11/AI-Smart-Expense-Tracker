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
padding:40px;
text-align:center;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.2);
box-shadow:0px 8px 30px rgba(0,0,0,0.4);
transition:0.3s;
}

.card:hover{
transform:scale(1.06);
box-shadow:0px 12px 40px rgba(0,0,0,0.6);
}

.card h2{
color:white;
margin-bottom:10px;
}

.card p{
color:#d1d1d1;
}

.open-text{
margin-top:10px;
font-size:15px;
color:#00ffd5;
}

a{
text-decoration:none;
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
        <h2>📊 Dashboard</h2>
        <p>View your financial overview</p>
        <div class="open-text">Open →</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Add_Expense" target="_self">
    <div class="card">
        <h2>➕ Add Expense</h2>
        <p>Add manual expenses quickly</p>
        <div class="open-text">Open →</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <a href="/Upload_Receipt" target="_self">
    <div class="card">
        <h2>🧾 Upload Receipt</h2>
        <p>Scan receipts using AI OCR</p>
        <div class="open-text">Open →</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Analytics" target="_self">
    <div class="card">
        <h2>📈 Analytics</h2>
        <p>Analyze your spending patterns</p>
        <div class="open-text">Open →</div>
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



