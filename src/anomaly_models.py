import pandas as pd
from sklearn.ensemble import IsolationForest
import streamlit as st

@st.cache_data
def detect_anomalies(variant_counts):
    """
    Uses Isolation Forest to detect anomalous pathways based on
    frequency and sequence complexity.
    """
    try:
        df = variant_counts.copy()
        
        # 1. Feature Engineering
        # Calculate the length of each path (number of steps taken)
        df['path_length'] = df['path'].apply(lambda x: len(x.split(' ➔ ')))
        
        # We will use 'frequency' and 'path_length' as our model features
        features = df[['frequency', 'path_length']]
        
        # 2. Model Initialization
        # 'contamination' sets the expected percentage of anomalies (set to 1% here)
        model = IsolationForest(contamination=0.01, random_state=42)
        
        # 3. Fit and Predict
        # Isolation Forest outputs -1 for anomalies, 1 for normal data points
        df['anomaly_score'] = model.fit_predict(features)
        df['is_anomaly'] = df['anomaly_score'].apply(lambda x: True if x == -1 else False)
        
        # Filter and isolate the detected anomalies
        anomalies = df[df['is_anomaly'] == True].sort_values(by='frequency', ascending=True)
        
        # Drop the technical score column for a cleaner UI presentation
        anomalies = anomalies.drop(columns=['anomaly_score'])
        
        return df, anomalies, "Success"
        st.markdown("---")
        st.header("🤖 AI Anomaly Detection")
        
        with st.spinner("Running Isolation Forest algorithm..."):
            from src.anomaly_models import detect_anomalies
            full_results, anomalies, ml_status = detect_anomalies(variant_counts)
            
        if anomalies is not None:
            st.warning(f"**Shadow IT & Deviation Alert:** The model flagged **{len(anomalies)}** highly anomalous paths out of {len(variant_counts)}.")
            
            st.write("These paths represent extreme statistical outliers based on their frequency and complexity. They warrant immediate compliance review.")
            
            st.dataframe(
                anomalies,
                column_config={
                    "percentage": st.column_config.NumberColumn("Frequency (%)", format="%.4f%%"),
                    "is_anomaly": None # Hide this column since they are all True here
                },
                hide_index=True,
                use_container_width=True
            )
        else:
            st.error(ml_status)
        
    except Exception as e:
        return None, None, f"Error in anomaly detection: {str(e)}"