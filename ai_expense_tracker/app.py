import streamlit as st

st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Background + global style
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.title{
text-align:center;
font-size:50px;
font-weight:bold;
}

.subtitle{
text-align:center;
font-size:18px;
color:#d1d1d1;
margin-bottom:40px;
}

.card{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(10px);
border-radius:20px;
padding:40px;
text-align:center;
transition:0.3s;
border:1px solid rgba(255,255,255,0.2);
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
}

.card:hover{
transform:scale(1.07);
box-shadow:0px 12px 35px rgba(0,0,0,0.6);
}

.card h2{
color:white;
}

.card p{
color:#d4d4d4;
}

.card a{
text-decoration:none;
font-weight:bold;
color:#00ffd5;
font-size:16px;
}

.footer{
text-align:center;
margin-top:60px;
color:#bdbdbd;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>💰 AI Smart Expense Tracker</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>AI powered personal finance assistant</div>", unsafe_allow_html=True)

# First row
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>📊 Dashboard</h2>
        <p>View financial overview and spending insights</p>
        <br>
        <a href="/Dashboard" target="_self">Open Dashboard →</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>➕ Add Expense</h2>
        <p>Add manual expenses quickly</p>
        <br>
        <a href="/Add_Expense" target="_self">Add Expense →</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Second row
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h2>🧾 Upload Receipt</h2>
        <p>Scan receipts using OCR AI</p>
        <br>
        <a href="/Upload_Receipt" target="_self">Scan Receipt →</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h2>📈 Analytics</h2>
        <p>Analyze your spending patterns</p>
        <br>
        <a href="/Analytics" target="_self">View Analytics →</a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built with ❤️ using Streamlit + AI + OCR</div>", unsafe_allow_html=True)
