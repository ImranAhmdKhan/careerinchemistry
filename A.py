import matplotlib.pyplot as plt
import squarify  # for treemap

# Define data for treemap
labels = [
    "Higher Studies\n(M.Sc., PhD, MBA)", "Govt Exams\n(UPSC, GATE, DRDO)", "Industry Jobs\n(Pharma, QA, R&D)",
    "Teaching\n(B.Ed., Assistant Prof.)", "Non-traditional Roles\n(Journalism, Informatics)", "Entrepreneurship\n(Startups, Funding)",
    "Strong Profile\n(Internships, Publications)", "Soft Skills\n(Communication, Resume)", "Strategic Planning\n(Career Mapping)"
]

# Relative sizes (arbitrary values for visual proportion)
sizes = [20, 18, 16, 12, 10, 10, 8, 8, 8]

# Define colors for categories
colors = [
    "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3",
    "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3", "#ffb3b3"
]

# Plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.85, text_kwargs={'fontsize': 10})
plt.title("Career Roadmap After B.Sc. Chemistry (Treemap)", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import networkx as nx

# Define roadmap as a directed graph
G = nx.DiGraph()

# Define main categories and sub-categories
roadmap = {
    "Career Opportunities after B.Sc": [
        "Higher Studies",
        "Government & Competitive Exams",
        "Jobs in Industry",
        "Teaching & Academia",
        "Non-traditional & Emerging Roles",
        "Entrepreneurship & Startups"
    ],
    "Higher Studies": [
        "M.Sc. (Core/Interdisciplinary)",
        "Integrated PhD",
        "MBA / M.Tech / MPH"
    ],
    "Government & Competitive Exams": [
        "UPSC / SSC / PSC",
        "CSIR-NET / GATE / ICMR",
        "DRDO / ISRO / BARC"
    ],
    "Jobs in Industry": [
        "Pharma / Biotech / FMCG",
        "QA/QC / R&D / Sales / Tech Support"
    ],
    "Teaching & Academia": [
        "School Teaching (B.Ed.)",
        "Asst. Professor (M.Sc. + NET/SET)"
    ],
    "Non-traditional & Emerging Roles": [
        "Science Communication",
        "Environmental Sustainability",
        "Data Analysis / Informatics"
    ],
    "Entrepreneurship & Startups": [
        "Incubation & Funding",
        "Graduate Startup Case Studies"
    ],
    "Building a Strong Profile": [
        "Internships & Projects",
        "Research & Publications",
        "Certifications (Coursera/NPTEL)"
    ],
    "Soft Skills & Employability": [
        "Communication / Presentation",
        "Networking / LinkedIn",
        "Resume / Interview Skills"
    ],
    "Strategic Roadmap": [
        "Short-term vs Long-term Goals",
        "Flexible vs Focused Paths",
        "Sample Career Maps"
    ]
}

# Add nodes and edges
for parent, children in roadmap.items():
    for child in children:
        G.add_edge(parent, child)

# Plotting
plt.figure(figsize=(16, 12))
pos = nx.spring_layout(G, k=1.5, iterations=200)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=9, font_weight='bold', arrowsize=20)

plt.title("Career Roadmap After B.Sc. Chemistry", fontsize=16, fontweight='bold')
plt.axis("off")
plt.show()

import matplotlib.pyplot as plt
import networkx as nx

# Create the graph
G = nx.DiGraph()

# Define the roadmap
roadmap = {
    "Career Opportunities after B.Sc": [
        "Higher Studies",
        "Government & Competitive Exams",
        "Jobs in Industry",
        "Teaching & Academia",
        "Non-traditional & Emerging Roles",
        "Entrepreneurship & Startups",
        "Building a Strong Profile",
        "Soft Skills & Employability",
        "Strategic Roadmap"
    ],
    "Higher Studies": [
        "M.Sc. (Core/Interdisciplinary)",
        "Integrated PhD",
        "MBA / M.Tech / MPH"
    ],
    "Government & Competitive Exams": [
        "UPSC / SSC / PSC",
        "CSIR-NET / GATE / ICMR",
        "DRDO / ISRO / BARC"
    ],
    "Jobs in Industry": [
        "Pharma / Biotech / FMCG",
        "QA/QC / R&D / Sales / Tech Support"
    ],
    "Teaching & Academia": [
        "School Teaching (B.Ed.)",
        "Asst. Professor (M.Sc. + NET/SET)"
    ],
    "Non-traditional & Emerging Roles": [
        "Science Communication",
        "Environmental Sustainability",
        "Data Analysis / Informatics"
    ],
    "Entrepreneurship & Startups": [
        "Incubation & Funding",
        "Graduate Startup Case Studies"
    ],
    "Building a Strong Profile": [
        "Internships & Projects",
        "Research & Publications",
        "Certifications (Coursera/NPTEL)"
    ],
    "Soft Skills & Employability": [
        "Communication / Presentation",
        "Networking / LinkedIn",
        "Resume / Interview Skills"
    ],
    "Strategic Roadmap": [
        "Short-term vs Long-term Goals",
        "Flexible vs Focused Paths",
        "Sample Career Maps"
    ]
}

# Add edges from parent to child
for parent, children in roadmap.items():
    for child in children:
        G.add_edge(parent, child)

# Improved Visualization
plt.figure(figsize=(20, 16))
pos = nx.spring_layout(G, k=1.5, iterations=200, seed=42)

# Node categories
color_map = []
for node in G.nodes():
    if node == "Career Opportunities after B.Sc":
        color_map.append("#1f78b4")  # Root
    elif node in roadmap.keys():
        color_map.append("#33a02c")  # Main Branch
    else:
        color_map.append("#a6cee3")  # Leaves

nx.draw(
    G, pos, with_labels=True, node_size=3000,
    node_color=color_map, edge_color="gray",
    font_size=9, font_weight='bold', arrowsize=15
)

plt.title("Enhanced Career Roadmap After B.Sc. Chemistry", fontsize=18, fontweight='bold')
plt.axis("off")
plt.show()


import matplotlib.pyplot as plt

# Courses and their job prospect ratings (out of 10)
courses = [
    "Biotechnology", "Biochemistry", "Botany", "Chemistry", "Toxicology",
    "Clinical Research", "Bioinformatics", "Forensic Science",
    "Environmental Science", "Nanoscience"
]
job_prospects = [9, 7, 5, 9, 7, 9, 9, 6, 7, 8]

# Plotting the graph
plt.figure(figsize=(12, 6))
bars = plt.bar(courses, job_prospects, color='skyblue')
plt.xlabel("M.Sc. Courses", fontsize=12)
plt.ylabel("Job Prospect Rating (out of 10)", fontsize=12)
plt.title("Job Prospects after M.Sc. at SCLS, Jamia Hamdard", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Annotate bars with their ratings
for bar, rating in zip(bars, job_prospects):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, rating, ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

# Data for plotting
data = {
    "Course": [
        "Biotechnology", "Biochemistry", "Botany", "Chemistry", "Toxicology",
        "Clinical Research", "Bioinformatics", "Forensic Science",
        "Environmental Science", "Nanoscience", "Pharmacovigilance"
    ],
    "Job Prospect (out of 10)": [9, 7, 5, 9, 7, 9, 9, 6, 7, 8, 8],
    "Avg. Salary (LPA)": [4.5, 3.8, 3.2, 5.0, 4.0, 6.0, 6.5, 4.0, 4.2, 5.5, 5.8]
}

df = pd.DataFrame(data)

# Create the bar plot
fig, ax1 = plt.subplots(figsize=(14, 7))

bars = ax1.bar(df["Course"], df["Job Prospect (out of 10)"], color="skyblue", label="Job Prospect (out of 10)")
ax1.set_ylabel("Job Prospect (out of 10)", fontsize=12)
ax1.set_ylim(0, 10)
ax1.set_xticklabels(df["Course"], rotation=45, ha="right")

# Secondary axis for average salary
ax2 = ax1.twinx()
ax2.plot(df["Course"], df["Avg. Salary (LPA)"], color="darkgreen", marker="o", label="Avg. Salary (LPA)")
ax2.set_ylabel("Avg. Salary (LPA)", fontsize=12)
ax2.set_ylim(0, 8)

# Add legends and title
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.title("M.Sc. Courses at SCLS, Jamia Hamdard: Job Prospects and Salary", fontsize=14)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


import matplotlib.pyplot as plt

# Fields and their chances of getting a job for Chemistry graduates
fields = [
    "Pharma Industry", "Environmental Science", "Forensics", "Clinical Research",
    "Food Science", "Cosmetic Chemistry", "Nanotechnology", "Material Science",
    "Agrochemicals", "Cheminformatics", "Patent Analyst"
]

# Assigning a numerical score to likelihood (High = 3, Moderate = 2, Fair = 1)
chances = [3, 3, 2.5, 2, 3, 2, 2, 2.5, 3, 1.5, 2]

# Labels for legend
chance_labels = {3: 'High', 2.5: 'Moderate to High', 2: 'Moderate', 1.5: 'Fair to Moderate', 1: 'Fair'}

# Bar colors based on likelihood
colors = ['green' if val == 3 else 'limegreen' if val == 2.5 else 'orange' if val == 2 else 'gold' if val == 1.5 else 'red' for val in chances]

# Create the bar plot
plt.figure(figsize=(14, 7))
bars = plt.bar(fields, chances, color=colors)
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 3.5)
plt.ylabel("Job Opportunity Level", fontsize=12)
plt.title("Opportunities for Chemistry Graduates in Other Fields", fontsize=14)

# Annotate with labels
for bar, val in zip(bars, chances):
    plt.text(bar.get_x() + bar.get_width()/2, val + 0.1, chance_labels[val], ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()




