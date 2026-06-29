import streamlit as st

st.title("Analysis of User Information Behavior in Corporate Information Systems")
st.subheader("Diagnostic Tool for Informal Practices & Shadow IT")

st.markdown("---")

st.write("""
Welcome to the research portal. This analytical tool is designed to process corporate information system (CIS) event logs to uncover the hidden realities of organizational workflows.

### Project Focus
Modern digital transformation often reveals a critical gap between **formal business processes** and the **real working practices** of employees. This tool utilizes process mining and machine learning algorithms to:
* Reconstruct actual user sequences from semi-structured log data.
* Identify bottlenecks, bypassed protocols, and "maverick" behaviors.
* Highlight statistical anomalies indicative of Shadow IT practices.

### Methodology
Currently configured to evaluate **Corporate Purchasing Deviations** (e.g., BPI Challenge data), the pipeline leverages `scikit-learn` for clustering and anomaly detection to separate standard operational friction from high-risk deviations.

---
*Research by Abenezer Fikadu Gerbi*
""")

if not st.session_state.get("logged_in"):
    st.info("👈 Please navigate to the Secure Login page using the sidebar to access the processing tools.")