import streamlit as st

st.title("Secure Access")
st.write("Please authenticate to access the log processing and sequence mining tools.")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

    if submit:
        # Simple mock authentication for development
        if username == "admin" and password == "vkr2026":
            st.session_state["logged_in"] = True
            st.success("Authentication successful! You can now access the Data Processing page.")
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")