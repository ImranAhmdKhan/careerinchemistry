import matplotlib.pyplot as plt
import numpy as np

# Alfred Nobel's skill set (1-10 scale)
skills = [
    "Chemistry", "Explosives Engineering", "Patent Strategy",
    "Business Management", "Multilingual Communication", 
    "Scientific Innovation", "Philanthropy", "Literary Writing"
]
proficiency = [9, 10, 9, 8, 7, 10, 9, 6]

# Prepare radar chart
labels = np.array(skills)
stats = np.array(proficiency)
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]]))
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, stats, color='darkred', linewidth=2)
ax.fill(angles, stats, color='salmon', alpha=0.4)

# Decorations
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_title("Skill Set Mapping of Alfred Nobel", size=14, weight='bold', pad=20)

plt.tight_layout()
plt.show()
