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

# Title
st.markdown("""
<h1 style='text-align:center;'>💰 AI Smart Expense Tracker</h1>
<p style='text-align:center;font-size:18px;'>Your AI-powered personal finance assistant</p>
""", unsafe_allow_html=True)

st.markdown("---")


# Card Styling
st.markdown("""
<style>

.card {
    background: linear-gradient(145deg,#1e1e2f,#26263a);
    padding:35px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 6px 25px rgba(0,0,0,0.5);
    transition:0.3s;
}

.card:hover{
    transform:scale(1.05);
    box-shadow:0px 10px 35px rgba(0,0,0,0.7);
}

.card h2{
    color:white;
}

.card p{
    color:#bdbdbd;
}

.card a{
    text-decoration:none;
    color:white;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


# First Row
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>📊 Dashboard</h2>
        <p>View your financial overview</p>
        <br>
        <a href="/Dashboard" target="_self">Open Dashboard</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>➕ Add Expense</h2>
        <p>Add manual expenses</p>
        <br>
        <a href="/Add_Expense" target="_self">Add Expense</a>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# Second Row
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h2>🧾 Upload Receipt</h2>
        <p>Scan receipts using AI</p>
        <br>
        <a href="/Upload_Receipt" target="_self">Upload Receipt</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h2>📈 Analytics</h2>
        <p>Analyze your spending</p>
        <br>
        <a href="/Analytics" target="_self">View Analytics</a>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")

st.markdown(
"""
<p style='text-align:center;color:gray;'>
Built with ❤️ using Streamlit + AI + OCR
</p>
""",
unsafe_allow_html=True
)
