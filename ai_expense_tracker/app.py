import streamlit as st


st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #F6F8FB;
}

/* Remove large padding */
.block-container {
    padding-top: 2rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 700;
    color: #1F2937;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6B7280;
    margin-bottom: 40px;
}

/* Cards */
.card {
    background: white;
    border-radius: 16px;
    padding: 30px;
    text-align: center;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
}

/* Hover */
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.1);
}

/* Icon */
.card-icon {
    font-size: 36px;
    margin-bottom: 10px;
}

/* Title */
.card h3 {
    color: #1F2937;
}

/* Text */
.card p {
    color: #6B7280;
}

/* Remove underline from links */
a {
    text-decoration: none !important;
    color: inherit;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown("<div class='title'>AI Smart Expense Tracker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Manage and analyze your expenses with AI</div>", unsafe_allow_html=True)
# First row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <a href="/Dashboard" target="_self">
    <div class="card">
        <div class="card-icon">📊</div>
        <h3>Dashboard</h3>
        <p>Overview</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Add_Expense" target="_self">
    <div class="card">
        <div class="card-icon">➕</div>
        <h3>Add Expense</h3>
        <p>Manual entry</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/Upload_Receipt" target="_self">
    <div class="card">
        <div class="card-icon">🧾</div>
        <h3>Scan Receipt</h3>
        <p>AI OCR</p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Analytics" target="_self">
    <div class="card">
        <div class="card-icon">📈</div>
        <h3>Analytics</h3>
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










