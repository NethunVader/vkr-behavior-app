import graphviz
import streamlit as st

@st.cache_data
def draw_process_graph(path_string, is_anomaly=False):
    """
    Converts a sequential path string into a visual directed graph.
    Automatically compresses repeating sequential activities.
    """
    raw_nodes = path_string.split(" ➔ ")
    
    # 1. Compress repeating nodes (fixes the 150-box issue)
    nodes = []
    current_node = raw_nodes[0]
    count = 1
    
    for activity in raw_nodes[1:]:
        if activity == current_node:
            count += 1
        else:
            # Add a line break \n and the multiplier
            label = f"{current_node}\n(x{count})" if count > 1 else current_node
            nodes.append(label)
            current_node = activity
            count = 1
            
    final_label = f"{current_node}\n(x{count})" if count > 1 else current_node
    nodes.append(final_label)
    
    # 2. Initialize the Graphviz directed graph
    dot = graphviz.Digraph(comment='Process Flow')
    dot.attr(rankdir='LR', size='12,5')
    
    # Set colors based on whether it is a shadow/anomalous practice
    node_color = '#ffcccc' if is_anomaly else '#ccffcc'
    border_color = '#cc0000' if is_anomaly else '#006600'
    
    # 3. Create the visual nodes and the arrows connecting them
    for i, activity in enumerate(nodes):
        node_id = str(i)
        dot.node(node_id, activity, style='filled,bold', fillcolor=node_color, color=border_color, shape='box', fontname='Helvetica')
        
        if i > 0:
            prev_node_id = str(i - 1)
            dot.edge(prev_node_id, node_id, color='#555555', penwidth='2.0')
            
    return dot