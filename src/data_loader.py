import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_and_clean_data(file_path):
    try:
        if not os.path.exists(file_path):
            return None, f"File not found at {file_path}"

        # 1. Read the new fast CSV
        df = pd.read_csv(file_path)
        
        # 2. Map the XES-style columns
        column_mapping = {
            'case:concept:name': 'case_id',
            'concept:name': 'activity',
            'time:timestamp': 'timestamp',
            'org:resource': 'user_id'
        }
        df = df.rename(columns=column_mapping)
        
        # 3. Clean and sort
        df = df.dropna(subset=['timestamp', 'activity', 'user_id', 'case_id'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
        df = df.sort_values(by=['case_id', 'timestamp']).reset_index(drop=True)
        
        return df, "Success"
        
    except Exception as e:
        return None, f"Error: {str(e)}"