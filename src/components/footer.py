
import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center;">
            <p style="
                font-weight:700;
                color:#FFD700;
                font-size:16px;
                letter-spacing:0.5px;
                text-shadow: 0 0 8px rgba(255,215,0,0.4);
            ">
                🎓 SnapClass | AI-Powered Attendance System
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center;">
            <p style="
                font-weight:700;
                color:#2563EB;
                font-size:16px;
                letter-spacing:0.5px;
            ">
                🎓 SnapClass | AI-Powered Attendance System
            </p>
        </div>
    """, unsafe_allow_html=True)
