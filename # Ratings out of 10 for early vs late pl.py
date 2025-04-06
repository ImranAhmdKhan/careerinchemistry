import matplotlib.pyplot as plt

def plot_career_planning_comparison():
    # Benefits categories
    factors = [
        'Self-Awareness',
        'Opportunity Access',
        'Confidence & Clarity',
        'Profile Strength',
        'Decision Quality'
    ]

    # Ratings out of 10 for early vs late planning
    early_planning = [9, 9, 8, 9, 9]
    late_planning = [4, 5, 5, 6, 5]

    # Set up positions for bars
    x = range(len(factors))
    width = 0.35

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], early_planning, width=width, label='Early Planning', color='skyblue')
    plt.bar([i + width/2 for i in x], late_planning, width=width, label='Late Planning', color='salmon')

    # Add labels and title
    plt.xticks(x, factors, rotation=20)
    plt.ylabel("Impact Level (1–10)")
    plt.title("Why Early Career Planning Matters")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Run the function
plot_career_planning_comparison()
