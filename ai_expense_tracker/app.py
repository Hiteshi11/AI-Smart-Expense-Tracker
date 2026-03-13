import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(180deg,#f8fafc,#eef2ff);
font-family: 'Segoe UI';
}

/* remove default padding */
.block-container{
padding-top:2rem;
}

/* titles */
.main-title{
text-align:center;
font-size:52px;
font-weight:700;
color:#1e293b;
}

.sub-title{
text-align:center;
color:#64748b;
margin-bottom:50px;
}

/* card design */
.card{
background:white;
border-radius:20px;
padding:35px;
text-align:center;
box-shadow:0px 12px 30px rgba(0,0,0,0.08);
transition:all 0.3s ease;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0px 18px 40px rgba(0,0,0,0.15);
}

/* card icons */
.card-icon{
font-size:40px;
margin-bottom:10px;
}

/* card titles */
.card h2{
color:#1e293b;
font-weight:600;
}

/* card text */
.card p{
color:#64748b;
}

a{
text-decoration:none !important;
color:inherit;
}

</style>
""", unsafe_allow_html=True)



# Title
st.markdown("<div class='main-title'>AI Smart Expense Tracker</div>", unsafe_allow_html=True)

st.markdown(
"<div class='sub-title'>Track, scan and analyze your expenses with AI</div>",
unsafe_allow_html=True
)
# First row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <a href="/Dashboard" target="_self">
    <div class="card">
        <div class="card-icon">📊</div>
        <h2>Dashboard</h2>
        <p>Overview</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Add_Expense" target="_self">
    <div class="card">
        <div class="card-icon">➕</div>
        <h2>Add Expense</h2>
        <p>Manual entry</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/Upload_Receipt" target="_self">
    <div class="card">
        <div class="card-icon">🧾</div>
        <h2>Scan Receipt</h2>
        <p>AI OCR</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Analytics" target="_self">
    <div class="card">
        <div class="card-icon">📈</div>
        <h2>Analytics</h2>
        <p>Insights</p>
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









