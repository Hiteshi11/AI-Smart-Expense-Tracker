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

.big-title{
text-align:center;
font-size:50px;
font-weight:bold;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#cfcfcf;
margin-bottom:40px;
}

.card{
background: rgba(255,255,255,0.08);
border-radius:20px;
padding:40px;
text-align:center;
transition:0.3s;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.2);
box-shadow:0px 8px 30px rgba(0,0,0,0.4);
}

.card:hover{
transform:scale(1.07);
box-shadow:0px 15px 40px rgba(0,0,0,0.6);
}

.card h2{
color:white;
}

.card p{
color:#d1d1d1;
}

.button-link{
display:inline-block;
padding:10px 20px;
margin-top:10px;
border-radius:10px;
background:#00ffd5;
color:black;
font-weight:bold;
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
    <div class="card">
        <h2>📊 Dashboard</h2>
        <p>View your financial overview</p>
        <a class="button-link" href="/Dashboard" target="_self">Open</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>➕ Add Expense</h2>
        <p>Add manual expenses easily</p>
        <a class="button-link" href="/Add_Expense" target="_self">Open</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h2>🧾 Upload Receipt</h2>
        <p>Scan receipts using AI OCR</p>
        <a class="button-link" href="/Upload_Receipt" target="_self">Open</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h2>📈 Analytics</h2>
        <p>Analyze spending patterns</p>
        <a class="button-link" href="/Analytics" target="_self">Open</a>
    </div>
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

