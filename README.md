# User Information Behavior Analysis in Corporate Information Systems

This project is a diagnostic tool designed to analyze Corporate Information System (CIS) event logs to uncover the gap between **formal business processes** and **actual employee working practices**. It leverages process mining and unsupervised machine learning to detect behavioral deviations and potential Shadow IT practices.

## Research Objectives
The core objective is to identify how users deviate from prescribed workflows, providing insights into:
* **Process Bottlenecks:** Identifying inefficiencies in manual entry tasks.
* **Maverick Behavior:** Detecting procurement and authorization workarounds.
* **Shadow IT:** Flagging non-standard software or procedure usage via anomaly detection.

## Key Methodology
The tool follows a structured pipeline to transform raw logs into actionable intelligence:



1.  **Data Ingestion:** Automated parsing of standard process mining event logs (BPI Challenge formats).
2.  **Sequence Mining:** Reconstructing individual user behavioral paths (trace variants).
3.  **Anomaly Detection:** Utilizing the **Isolation Forest** algorithm to statistically isolate outliers (deviated workflows) from formal procedures.
4.  **Visual Analytics:** Automatic flowchart generation to interpret and validate flagged anomalies.

## Technology Stack
* **Backend:** Python 3.10, Pandas, scikit-learn
* **Process Mining:** PM4Py
* **Visualization:** Graphviz (for process flow reconstruction)
* **Frontend:** Streamlit
* **Infrastructure:** Dockerized environment for reproducible research

## Getting Started

### Prerequisites
* Docker Desktop
* VS Code with Dev Containers extension

### Setup
1.  Clone this repository:
    ```bash
    git clone [https://github.com/NethunVader/vkr-behavior-app.git](https://github.com/NethunVader/vkr-behavior-app.git)
    cd vkr-behavior-app
    ```
2.  Open the project in VS Code and **Rebuild in Container**.
3.  Place your dataset (`.csv`) in `data/raw/`.
4.  Run the application:
    ```bash
    streamlit run app.py
    ```

## Academic Context
This tool was developed as part of the thesis project: *"Analysis of User Information Behavior in Corporate Information Systems."* It is intended for researchers and compliance officers to bridge the gap between documented organizational protocols and real-world employee digital behavior.

---
*Developed by Abenezer Fikadu Gerbi*