import streamlit as st
from src.data_loader import load_and_clean_data
from src.process_mining import extract_sequences
from src.anomaly_models import detect_anomalies

st.title("Log Processing & Sequence Mining")

st.write("""
Analyzing **BPI Challenge 2019 (Purchase-to-Pay)**. 
Loading the converted CSV dataset directly from the secure local container storage.
""")

# Initialize a session state variable so Streamlit remembers we loaded the data
if "data_loaded" not in st.session_state:
    st.session_state["data_loaded"] = False

# When the button is clicked, change the state to True
if st.button("Load & Process BPI 2019 Dataset"):
    st.session_state["data_loaded"] = True

# Now, run the entire pipeline if the state is True
if st.session_state["data_loaded"]:
    with st.spinner("Parsing fast CSV file. This will only take a few seconds..."):
        file_path = "data/raw/bpi_2019.csv"
        df, status = load_and_clean_data(file_path)
        
    if df is not None:
        st.success("File parsed and cleaned successfully!")
        
        # --- 1. HIGH-LEVEL METRICS ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Events", len(df))
        col2.metric("Unique Cases", df['case_id'].nunique())
        col3.metric("Unique Users", df['user_id'].nunique())
        col4.metric("Unique Activities", df['activity'].nunique())
        
        st.markdown("---")
        
        # --- 2. EXTRACT SEQUENCES ---
        with st.spinner("Extracting behavioral sequences..."):
            case_sequences, variant_counts, pm_status = extract_sequences(df)
            
        if variant_counts is not None:
            st.subheader("Workflow Sequence Analysis")
            st.write(f"Detected **{len(variant_counts)}** unique behavioral paths.")
            
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.write("### The 'Formal' Practices")
                st.write("Standard paths taken by users.")
                st.dataframe(
                    variant_counts.head(5), 
                    column_config={"percentage": st.column_config.ProgressColumn("Frequency (%)", format="%f%%", min_value=0, max_value=100)},
                    hide_index=True
                )
                
            with col_right:
                st.write("### The Deviations & 'Shadow' Practices")
                st.write("Rare, customized, or bypassed paths.")
                st.dataframe(
                    variant_counts.tail(5).sort_values(by='frequency', ascending=True),
                    hide_index=True
                )
            
            # --- 3. AI ANOMALY DETECTION & VISUALIZATION ---
            st.markdown("---")
            st.header("🤖 AI Anomaly Detection & Visualization")
            
            with st.spinner("Running Isolation Forest algorithm..."):
                from src.anomaly_models import detect_anomalies
                full_results, anomalies, ml_status = detect_anomalies(variant_counts)
                
            if anomalies is not None:
                st.warning(f"**Shadow IT & Deviation Alert:** The model flagged **{len(anomalies)}** highly anomalous paths out of {len(variant_counts)}.")
                st.write("These paths represent extreme statistical outliers. Select a path below to reconstruct the user's actual behavior.")
                
                # Create a layout with the table on the left and the graph on the right
                ml_left, ml_right = st.columns([1, 1.5])
                
                with ml_left:
                    st.write("### Flagged Anomalies")
                    # Let the user select a specific anomalous path using a selectbox
                    anomaly_options = anomalies['path'].tolist()
                    selected_path = st.selectbox("Select a deviated path to investigate:", anomaly_options)
                    
                    st.write("**Anomaly Data Table:**")
                    st.dataframe(
                        anomalies,
                        column_config={
                            "percentage": st.column_config.NumberColumn("Frequency (%)", format="%.4f%%"),
                            "is_anomaly": None
                        },
                        hide_index=True,
                        use_container_width=True
                    )
                    
                with ml_right:
                    st.write("### Process Reconstruction Graph")
                    if selected_path:
                        from src.visualizer import draw_process_graph
                        
                        st.write(f"**Visualizing:** {selected_path[:50]}...")
                        
                        # Generate the Graphviz flowchart
                        flowchart = draw_process_graph(selected_path, is_anomaly=True)
                        
                        # Render it as a bulletproof backend image
                        st.graphviz_chart(flowchart, use_container_width=True)
            else:
                st.error(ml_status)
        else:
            st.error(pm_status)
    else:
        st.error(status)