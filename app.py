
import streamlit as st

# Set page configuration
st.set_page_config(page_title="MVP Dashboard", layout="wide")

# CSS for dark mode
st.markdown("""

    .main {
        background-color: #0d1117;
    }
    .alert {
        background: #8b0000;
        color: #fff;
        text-align: center;
        padding: 40px;
        font-size: 3em;
        font-weight: bold;
        border: 3px solid #ff0000;
        text-transform: uppercase;
        letter-spacing: 4px;
    }
    .card {
        background: #161b22;
        padding: 20px;
        border: 2px solid #30363d;
        border-radius: 8px;
        text-align: center;
        color: #e0e0e0;
    }
    h2 {
        color: #58a6ff;
    }
    .green {
        color: #00ff00;
    }
    .yellow {
        color: #ffcc00;
    }
    .red {
        color: #ff4444;
    }

""", unsafe_allow_html=True)

# ALERT section
st.markdown('ALERT: SECURITY BREACH DETECTED', unsafe_allow_html=True)

# Metrics Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('Systems Online95%', unsafe_allow_html=True)

with col2:
    st.markdown('Threat LevelCRITICAL', unsafe_allow_html=True)

with col3:
    st.markdown('Mission Readiness72%', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    st.write("Dashboard is running")
