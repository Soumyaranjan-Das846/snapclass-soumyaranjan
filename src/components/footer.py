# import streamlit as st


# def footer_home():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#                 <p style="font-weight:bold; color:white;">
#     © 2026 SnapClass | AI-Powered Attendance System</p>
#         # <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
#         # <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)


# def footer_dashboard():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
#         <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)
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