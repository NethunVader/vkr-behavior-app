import streamlit as st

#config main window
st.set_page_config(
    page_title="VKR Behavior Analysis",
    layout="wide"
)

#initialize the session state for auth
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

#setup the pages
landing_page = st.Page("views/landing.py", title="Project Overview", default=True)
login_page = st.Page("views/login.py", title="Login")
processing_page = st.Page("views/processing.py", title="Data Processing and Mining")

#navigation
if st.session_state["logged_in"]:
    pg = st.navigation([landing_page, processing_page])
else:
    pg = st.navigation([landing_page, login_page])

#run the router
pg.run()