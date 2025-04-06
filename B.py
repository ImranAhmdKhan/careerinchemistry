
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes and edges for career assessment roadmap
G.add_edge("Start Career Planning", "Understand Interests & Strengths")

# Step 1: Interests & Strengths
G.add_edge("Understand Interests & Strengths", "Use MBTI Assessment")
G.add_edge("Understand Interests & Strengths", "Use StrengthsFinder")
G.add_edge("Use MBTI Assessment", "Identify Personality Type")
G.add_edge("Use StrengthsFinder", "Identify Top 5 Strengths")

# Step 2: Reflect & Align
G.add_edge("Identify Personality Type", "Reflect on Career Fit")
G.add_edge("Identify Top 5 Strengths", "Reflect on Career Fit")

# Step 3: Set SMART Goals
G.add_edge("Reflect on Career Fit", "Set SMART Goals")
G.add_edge("Set SMART Goals", "Specific")
G.add_edge("Set SMART Goals", "Measurable")
G.add_edge("Set SMART Goals", "Achievable")
G.add_edge("Set SMART Goals", "Relevant")
G.add_edge("Set SMART Goals", "Time-bound")

# Simulated assessment results
results = {
    "MBTI Type": "INFJ",
    "Top Strengths": ["Strategic", "Learner", "Input", "Achiever", "Analytical"]
}

# Positioning for better visualization
pos = nx.spring_layout(G, k=1.1, iterations=100)

# Draw nodes and edges
plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Title
plt.title("Understanding Interests, Strengths & Setting SMART Career Goals", fontsize=14, fontweight='bold')
plt.axis("off")
plt.tight_layout()
plt.show()

# Print simulated assessment
print("=== Simulated Assessment Output ===")
print(f"MBTI Personality Type: {results['MBTI Type']}")
print("Top 5 Strengths:", ", ".join(results["Top Strengths"]))

import matplotlib.pyplot as plt
import networkx as nx
import ipywidgets as widgets
from IPython.display import display, clear_output

# Input widgets
mbti_input = widgets.Text(description="MBTI Type:")
strengths_input = widgets.Text(description="Top 5 Strengths (comma-separated):")

specific = widgets.Text(description="Specific:")
measurable = widgets.Text(description="Measurable:")
achievable = widgets.Text(description="Achievable:")
relevant = widgets.Text(description="Relevant:")
timebound = widgets.Text(description="Time-bound:")

submit_button = widgets.Button(description="Generate Roadmap", button_style='success')

output = widgets.Output()

# Callback function
def generate_roadmap(b):
    with output:
        clear_output()

        mbti_type = mbti_input.value.strip()
        strengths = [s.strip() for s in strengths_input.value.split(",")]
        smart_goals = {
            "Specific": specific.value,
            "Measurable": measurable.value,
            "Achievable": achievable.value,
            "Relevant": relevant.value,
            "Time-bound": timebound.value
        }

        # Create graph
        G = nx.DiGraph()

        G.add_edge("Start Career Planning", "Understand Interests & Strengths")
        G.add_edge("Understand Interests & Strengths", "MBTI Assessment")
        G.add_edge("Understand Interests & Strengths", "StrengthsFinder")
        G.add_edge("MBTI Assessment", f"Type: {mbti_type or 'N/A'}")
        G.add_edge("StrengthsFinder", f"Strengths: {', '.join(strengths) if strengths else 'N/A'}")
        G.add_edge(f"Type: {mbti_type or 'N/A'}", "Reflect on Career Fit")
        G.add_edge(f"Strengths: {', '.join(strengths) if strengths else 'N/A'}", "Reflect on Career Fit")
        G.add_edge("Reflect on Career Fit", "Set SMART Goals")

        for k, v in smart_goals.items():
            G.add_edge("Set SMART Goals", f"{k}: {v or 'Not provided'}")

        # Visualize
        pos = nx.spring_layout(G, k=1.1, iterations=100)
        plt.figure(figsize=(16, 12))
        nx.draw_networkx_nodes(G, pos, node_color="lightgreen", node_size=3000)
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
        nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
        plt.title("Interactive Career Self-Assessment & SMART Goal Roadmap", fontsize=14, fontweight="bold")
        plt.axis("off")
        plt.show()

        print("\n🎯 Your SMART Goals:")
        for k, v in smart_goals.items():
            print(f"{k}: {v}")

# Bind the callback
submit_button.on_click(generate_roadmap)

# Display form
display(widgets.VBox([
    widgets.HTML("<h3>🔍 Career Self-Assessment Form</h3>"),
    mbti_input,
    strengths_input,
    widgets.HTML("<h4>🎯 Define Your SMART Goals</h4>"),
    specific, measurable, achievable, relevant, timebound,
    submit_button,
    output
]))

