import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background: #F4C2C2;
}

/* Sidebar pastel */
[data-testid="stSidebar"]{
    background: #f3e8ff;
}

/* Title styling */
.title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#f3e8ff;
}

.subtitle{
    text-align:center;
    color:#7a7a9d;
    margin-bottom:40px;
}

/* Pastel cards */
.card{
    background:#f8f5ff;
    border-radius:18px;
    padding:40px;
    text-align:center;
    border:1px solid #e4dcff;
    box-shadow:0px 8px 20px rgba(0,0,0,0.05);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0px 15px 30px rgba(0,0,0,0.1);
}

/* Buttons pastel */
.stButton>button{
    background:#dcd6ff;
    color:#f3e8ff;
    border-radius:12px;
    border:none;
}

.stButton>button:hover{
    background:#c8c1ff;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stSelectbox div{
    background:#f8f5ff;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    background:#f8f5ff;
}

/* Remove link underline */
a{
text-decoration:none !important;
color:inherit;
}

</style>
""", unsafe_allow_html=True)



# Title
st.markdown("<div class='title'>💰 AI Smart Expense Tracker</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>AI powered personal finance assistant</div>",
unsafe_allow_html=True
)
# First row
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <a href="/Dashboard" target="_self">
    <div class="card">
        <h2>📊 Dashboard</h2>
        <p>View financial overview</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Add_Expense" target="_self">
    <div class="card">
        <h2>➕ Add Expense</h2>
        <p>Add manual expenses</p>
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
        <p>Scan receipts with AI</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Analytics" target="_self">
    <div class="card">
        <h2>📈 Analytics</h2>
        <p>Analyze spending patterns</p>
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








