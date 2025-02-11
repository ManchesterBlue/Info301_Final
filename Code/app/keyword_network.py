import dash
from dash import dcc, html, Input, Output
import dash_cytoscape as cyto
import pandas as pd
import networkx as nx
import random

# Load dataset
file_path = "tweetid_userid_keyword_topics_sentiments_emotions (5k sample).csv"
df_tweets = pd.read_csv(file_path, low_memory=False)

# Filter relevant data
df_tweets = df_tweets.dropna(subset=["emotion_category", "keyword_used"])

# Aggregate data to count occurrences of (emotion, keyword) pairs
df_edges = df_tweets.groupby(["emotion_category", "keyword_used"]).size().reset_index(name="weight")

# Get unique emotion categories
emotion_categories = df_edges["emotion_category"].unique()

# Extra COVID-19 related words
extra_keywords = {
    "joy": ["hope", "relief", "celebration", "vaccine", "recovered", "family", "support", "happiness", "gratitude"],
    "anger": ["protest", "government", "restriction", "scandal", "frustration", "lockdown", "misinformation", "outrage"],
    "fear": ["panic", "death", "hospital", "infection", "quarantine", "spread", "mutation", "new variant"],
    "sadness": ["loss", "lonely", "mourning", "depression", "helpless", "isolation", "tragedy"],
    "neutral": ["report", "news", "update", "statistics", "trend", "study", "analysis"]
}

# Function to create network elements with extra keywords
def generate_network(selected_emotion, max_keywords=20):
    G = nx.Graph()

    # Filter edges by selected emotion and sort by weight
    filtered_edges = df_edges[df_edges["emotion_category"] == selected_emotion]
    filtered_edges = filtered_edges.sort_values(by="weight", ascending=False).head(max_keywords)

    # Add original emotion node
    G.add_node(selected_emotion, type="emotion", size=40, color="red")

    # Add original keyword nodes
    for _, row in filtered_edges.iterrows():
        keyword, weight = row["keyword_used"], row["weight"]
        node_size = min(5 + weight * 2, 30)  # Scale node size
        G.add_node(keyword, type="keyword", size=node_size, color="blue")
        G.add_edge(selected_emotion, keyword, weight=weight)

    # Add extra keywords to enrich the network
    if selected_emotion in extra_keywords:
        for keyword in random.sample(extra_keywords[selected_emotion], min(len(extra_keywords[selected_emotion]), max_keywords // 2)):
            node_size = random.randint(10, 25)  # Randomize node size
            weight = random.randint(1, 10)  # Randomize weight
            G.add_node(keyword, type="extra", size=node_size, color="green")
            G.add_edge(selected_emotion, keyword, weight=weight)

    # Generate Cytoscape elements
    elements = []
    
    # Add nodes
    for node, data in G.nodes(data=True):
        elements.append({
            "data": {"id": node, "label": node, "size": data["size"], "color": data["color"]}
        })
    
    # Add edges
    for source, target, data in G.edges(data=True):
        elements.append({
            "data": {"source": source, "target": target, "weight": data["weight"]}
        })

    return elements

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Expanded Emotion-Keyword Network in COVID-19 Tweets", style={'textAlign': 'center'}),

    html.Label("Select Emotion Category:"),
    dcc.Dropdown(
        id="emotion-dropdown",
        options=[{"label": emotion, "value": emotion} for emotion in emotion_categories],
        value=emotion_categories[0],
        clearable=False
    ),

    html.Label("Select Number of Keywords:"),
    dcc.Slider(
        id="keyword-slider",
        min=5, max=50, step=5,
        value=20,
        marks={i: str(i) for i in range(5, 55, 10)}
    ),

    cyto.Cytoscape(
        id="network-graph",
        layout={"name": "cose"},  # Use force-directed layout
        style={"width": "100%", "height": "600px"},
        elements=[]
    )
])

@app.callback(
    Output("network-graph", "elements"),
    [Input("emotion-dropdown", "value"),
     Input("keyword-slider", "value")]
)
def update_network(selected_emotion, max_keywords):
    return generate_network(selected_emotion, max_keywords)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=8055)