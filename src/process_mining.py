import pandas as pd
import streamlit as st

@st.cache_data
def extract_sequences(df):
    """
    Groups events by case_id to extract the sequential path of activities.
    Calculates the frequency of each unique path (variant).
    """
    try:
        # Group by case_id and create a list of activities in chronological order
        sequences = df.groupby('case_id')['activity'].agg(list).reset_index()
        
        # Convert the list of activities into a single string path (e.g., "A -> B -> C")
        sequences['path'] = sequences['activity'].apply(lambda x: " ➔ ".join(x))
        
        # Count how many times each exact path occurs
        variant_counts = sequences['path'].value_counts().reset_index()
        variant_counts.columns = ['path', 'frequency']
        
        # Calculate the percentage to show dominance of certain paths
        total_cases = len(sequences)
        variant_counts['percentage'] = (variant_counts['frequency'] / total_cases * 100).round(2)
        
        return sequences, variant_counts, "Success"
        
    except Exception as e:
        return None, None, f"Error extracting sequences: {str(e)}"