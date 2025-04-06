import matplotlib.pyplot as plt

def plot_extended_career_sectors():
    sectors = [
        "Pharma Industry", "Chemical Mfg", "R&D", "Teaching", "QC/QA",
        "Food & Beverage", "Cosmetics", "Polymer Industry", "Paints & Dyes", "Textile Chemistry",
        "Forensics", "Oil & Petrochemicals", "Environmental", "Water Treatment", "Agrochemicals",
        "Energy Materials", "Nanotech/Materials", "Glass & Ceramics", "Paper & Pulp", "Cement & Construction",
        "Industrial Safety", "Biotech", "Clinical Labs", "Patent/IPR", "Sales/Marketing",
        "Lab Analyst", "Computational Chem", "Scientific Writing", "Science Journalism", "Regulatory Affairs",
        "Govt Labs (CSIR, DRDO)", "Civil Services", "Pharma Regulatory", "Entrepreneurship", "NGOs/Policy", "Chem Trade/Consultancy"
    ]

    # Assign demand index (1 to 10)
    demand_index = [
        9, 8, 8, 7, 8,
        7, 6, 6, 6, 5,
        7, 6, 7, 6, 7,
        8, 7, 5, 4, 6,
        5, 7, 6, 7, 5,
        6, 7, 6, 6, 6,
        8, 7, 7, 7, 6, 5
    ]

    # Plot
    plt.figure(figsize=(14, 12))
    bars = plt.barh(sectors, demand_index, color='mediumorchid')
    plt.xlabel("Demand / Popularity Index (1 = Low, 10 = High)", fontsize=12)
    plt.title("📈 Career Sectors After B.Sc. Chemistry (Extended View)", fontsize=14, fontweight='bold')
    plt.xlim(0, 10)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Value label
    for bar in bars:
        plt.text(bar.get_width() + 0.2, bar.get_y() + 0.1, f'{bar.get_width()}', va='center', fontsize=8)

    plt.tight_layout()
    plt.show()

# Run the function
plot_extended_career_sectors()

import matplotlib.pyplot as plt

def plot_env_colored_career_sectors():
    sectors = [
        "Pharma Industry", "Chemical Mfg", "R&D", "Teaching", "QC/QA",
        "Food & Beverage", "Cosmetics", "Polymer Industry", "Paints & Dyes", "Textile Chemistry",
        "Forensics", "Oil & Petrochemicals", "Environmental", "Water Treatment", "Agrochemicals",
        "Energy Materials", "Nanotech/Materials", "Glass & Ceramics", "Paper & Pulp", "Cement & Construction",
        "Industrial Safety", "Biotech", "Clinical Labs", "Patent/IPR", "Sales/Marketing",
        "Lab Analyst", "Computational Chem", "Scientific Writing", "Science Journalism", "Regulatory Affairs",
        "Govt Labs (CSIR, DRDO)", "Civil Services", "Pharma Regulatory", "Entrepreneurship", "NGOs/Policy", "Chem Trade/Consultancy"
    ]

    demand_index = [
        9, 8, 8, 7, 8,
        7, 6, 6, 6, 5,
        7, 6, 7, 6, 7,
        8, 7, 5, 4, 6,
        5, 7, 6, 7, 5,
        6, 7, 6, 6, 6,
        8, 7, 7, 7, 6, 5
    ]

    # Sectors considered environment-related
    env_sectors = {
        "Environmental", "Water Treatment", "Agrochemicals", "NGOs/Policy", "Waste-to-Wealth / Circular Economy Startups"
    }

    # Assign bar colors
    colors = ['forestgreen' if s in env_sectors else 'mediumorchid' for s in sectors]

    # Plotting
    plt.figure(figsize=(14, 12))
    bars = plt.barh(sectors, demand_index, color=colors)
    plt.xlabel("Demand / Popularity Index (1 = Low, 10 = High)", fontsize=12)
    plt.title("🌿 Career Sectors After B.Sc. Chemistry\n(Highlighting Environmental Paths)", fontsize=15, fontweight='bold')
    plt.xlim(0, 10)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        plt.text(bar.get_width() + 0.2, bar.get_y() + 0.1, f'{bar.get_width()}', va='center', fontsize=8)

    # Add legend
    import matplotlib.patches as mpatches
    green_patch = mpatches.Patch(color='forestgreen', label='Environmental Sectors')
    purple_patch = mpatches.Patch(color='mediumorchid', label='Other Sectors')
    plt.legend(handles=[green_patch, purple_patch], loc='lower right')

    plt.tight_layout()
    plt.show()

# Run it
plot_env_colored_career_sectors()

import matplotlib.pyplot as plt

def plot_colored_by_category():
    sectors = [
        "Pharma Industry", "Chemical Mfg", "R&D", "Teaching", "QC/QA",
        "Food & Beverage", "Cosmetics", "Polymer Industry", "Paints & Dyes", "Textile Chemistry",
        "Forensics", "Oil & Petrochemicals", "Environmental", "Water Treatment", "Agrochemicals",
        "Energy Materials", "Nanotech/Materials", "Glass & Ceramics", "Paper & Pulp", "Cement & Construction",
        "Industrial Safety", "Biotech", "Clinical Labs", "Patent/IPR", "Sales/Marketing",
        "Lab Analyst", "Computational Chem", "Scientific Writing", "Science Journalism", "Regulatory Affairs",
        "Govt Labs (CSIR, DRDO)", "Civil Services", "Pharma Regulatory", "Entrepreneurship", "NGOs/Policy", "Chem Trade/Consultancy"
    ]

    demand_index = [
        9, 8, 8, 7, 8,
        7, 6, 6, 6, 5,
        7, 6, 7, 6, 7,
        8, 7, 5, 4, 6,
        5, 7, 6, 7, 5,
        6, 7, 6, 6, 6,
        8, 7, 7, 7, 6, 5
    ]

    # Sector category mapping
    category_colors = {
        'Environmental': 'forestgreen',
        'Pharmaceutical': 'mediumblue',
        'Academia/Research': 'goldenrod',
        'Core Industry': 'slateblue',
        'Healthcare/Clinical': 'crimson',
        'Government/Regulatory': 'darkorange',
        'Entrepreneurship/Policy': 'darkcyan',
        'Communication/Creative': 'orchid',
        'Sales/Business': 'teal',
        'Computational/Tech': 'darkviolet',
    }

    sector_category = {
        "Pharma Industry": 'Pharmaceutical',
        "Chemical Mfg": 'Core Industry',
        "R&D": 'Academia/Research',
        "Teaching": 'Academia/Research',
        "QC/QA": 'Core Industry',
        "Food & Beverage": 'Core Industry',
        "Cosmetics": 'Core Industry',
        "Polymer Industry": 'Core Industry',
        "Paints & Dyes": 'Core Industry',
        "Textile Chemistry": 'Core Industry',
        "Forensics": 'Healthcare/Clinical',
        "Oil & Petrochemicals": 'Core Industry',
        "Environmental": 'Environmental',
        "Water Treatment": 'Environmental',
        "Agrochemicals": 'Environmental',
        "Energy Materials": 'Academia/Research',
        "Nanotech/Materials": 'Academia/Research',
        "Glass & Ceramics": 'Core Industry',
        "Paper & Pulp": 'Core Industry',
        "Cement & Construction": 'Core Industry',
        "Industrial Safety": 'Core Industry',
        "Biotech": 'Academia/Research',
        "Clinical Labs": 'Healthcare/Clinical',
        "Patent/IPR": 'Government/Regulatory',
        "Sales/Marketing": 'Sales/Business',
        "Lab Analyst": 'Core Industry',
        "Computational Chem": 'Computational/Tech',
        "Scientific Writing": 'Communication/Creative',
        "Science Journalism": 'Communication/Creative',
        "Regulatory Affairs": 'Government/Regulatory',
        "Govt Labs (CSIR, DRDO)": 'Government/Regulatory',
        "Civil Services": 'Government/Regulatory',
        "Pharma Regulatory": 'Government/Regulatory',
        "Entrepreneurship": 'Entrepreneurship/Policy',
        "NGOs/Policy": 'Entrepreneurship/Policy',
        "Chem Trade/Consultancy": 'Sales/Business',
    }

    # Assign colors
    colors = [category_colors.get(sector_category[s], 'gray') for s in sectors]

    # Plotting
    plt.figure(figsize=(14, 14))
    bars = plt.barh(sectors, demand_index, color=colors)
    plt.xlabel("Demand / Popularity Index (1 = Low, 10 = High)", fontsize=12)
    plt.title("🎯 B.Sc. Chemistry Career Paths\n(Categorized by Sector)", fontsize=15, fontweight='bold')
    plt.xlim(0, 10)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Add labels
    for bar in bars:
        plt.text(bar.get_width() + 0.2, bar.get_y() + 0.1, f'{bar.get_width()}', va='center', fontsize=8)

    # Custom legend
    import matplotlib.patches as mpatches
    legend_handles = [mpatches.Patch(color=color, label=label) for label, color in category_colors.items()]
    plt.legend(handles=legend_handles, loc='upper right', ncol=2, fontsize=9)

    plt.tight_layout()
    plt.show()

# Run it
plot_colored_by_category()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_colored_and_bold_interdisciplinary():
    sectors = [
        "Pharma Industry", "Chemical Mfg", "R&D", "Teaching", "QC/QA",
        "Food & Beverage", "Cosmetics", "Polymer Industry", "Paints & Dyes", "Textile Chemistry",
        "Forensics", "Oil & Petrochemicals", "Environmental", "Water Treatment", "Agrochemicals",
        "Energy Materials", "Nanotech/Materials", "Glass & Ceramics", "Paper & Pulp", "Cement & Construction",
        "Industrial Safety", "Biotech", "Clinical Labs", "Patent/IPR", "Sales/Marketing",
        "Lab Analyst", "Computational Chem", "Scientific Writing", "Science Journalism", "Regulatory Affairs",
        "Govt Labs (CSIR, DRDO)", "Civil Services", "Pharma Regulatory", "Entrepreneurship", "NGOs/Policy", "Chem Trade/Consultancy"
    ]

    demand_index = [
        9, 8, 8, 7, 8,
        7, 6, 6, 6, 5,
        7, 6, 7, 6, 7,
        8, 7, 5, 4, 6,
        5, 7, 6, 7, 5,
        6, 7, 6, 6, 6,
        8, 7, 7, 7, 6, 5
    ]

    # Define sector categories
    category_colors = {
        'Environmental': 'forestgreen',
        'Pharmaceutical': 'mediumblue',
        'Academia/Research': 'goldenrod',
        'Core Industry': 'slateblue',
        'Healthcare/Clinical': 'crimson',
        'Government/Regulatory': 'darkorange',
        'Entrepreneurship/Policy': 'darkcyan',
        'Communication/Creative': 'orchid',
        'Sales/Business': 'teal',
        'Computational/Tech': 'darkviolet',
    }

    sector_category = {
        "Pharma Industry": 'Pharmaceutical',
        "Chemical Mfg": 'Core Industry',
        "R&D": 'Academia/Research',
        "Teaching": 'Academia/Research',
        "QC/QA": 'Core Industry',
        "Food & Beverage": 'Core Industry',
        "Cosmetics": 'Core Industry',
        "Polymer Industry": 'Core Industry',
        "Paints & Dyes": 'Core Industry',
        "Textile Chemistry": 'Core Industry',
        "Forensics": 'Healthcare/Clinical',
        "Oil & Petrochemicals": 'Core Industry',
        "Environmental": 'Environmental',
        "Water Treatment": 'Environmental',
        "Agrochemicals": 'Environmental',
        "Energy Materials": 'Academia/Research',
        "Nanotech/Materials": 'Academia/Research',
        "Glass & Ceramics": 'Core Industry',
        "Paper & Pulp": 'Core Industry',
        "Cement & Construction": 'Core Industry',
        "Industrial Safety": 'Core Industry',
        "Biotech": 'Academia/Research',
        "Clinical Labs": 'Healthcare/Clinical',
        "Patent/IPR": 'Government/Regulatory',
        "Sales/Marketing": 'Sales/Business',
        "Lab Analyst": 'Core Industry',
        "Computational Chem": 'Computational/Tech',
        "Scientific Writing": 'Communication/Creative',
        "Science Journalism": 'Communication/Creative',
        "Regulatory Affairs": 'Government/Regulatory',
        "Govt Labs (CSIR, DRDO)": 'Government/Regulatory',
        "Civil Services": 'Government/Regulatory',
        "Pharma Regulatory": 'Government/Regulatory',
        "Entrepreneurship": 'Entrepreneurship/Policy',
        "NGOs/Policy": 'Entrepreneurship/Policy',
        "Chem Trade/Consultancy": 'Sales/Business',
    }

    interdisciplinary_sectors = {
        "Environmental", "Water Treatment", "Agrochemicals", "Nanotech/Materials", "Biotech", "Computational Chem",
        "Forensics", "Energy Materials", "Patent/IPR", "Regulatory Affairs", "Entrepreneurship", "Scientific Writing",
        "Science Journalism", "NGOs/Policy", "Civil Services"
    }

    # Get colors and edge styles
    bar_colors = [category_colors.get(sector_category[s], 'gray') for s in sectors]
    edge_styles = ['black' if s in interdisciplinary_sectors else 'none' for s in sectors]
    edge_widths = [2 if s in interdisciplinary_sectors else 0.5 for s in sectors]

    # Plot
    plt.figure(figsize=(14, 15))
    bars = []
    for i, (s, val) in enumerate(zip(sectors, demand_index)):
        bar = plt.barh(s, val, color=bar_colors[i], edgecolor=edge_styles[i], linewidth=edge_widths[i])
        bars.append(bar)

    plt.xlabel("Demand / Popularity Index (1 = Low, 10 = High)", fontsize=12)
    plt.title("📘 B.Sc. Chemistry Career Paths\nColored by Sector & Bolded for Interdisciplinary Fields", fontsize=15, fontweight='bold')
    plt.xlim(0, 10)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    # Labels
    for i, bar in enumerate(bars):
        plt.text(demand_index[i] + 0.2, i, f'{demand_index[i]}', va='center', fontsize=8)

    # Legend
    legend_handles = [mpatches.Patch(color=color, label=label) for label, color in category_colors.items()]
    legend_handles.append(mpatches.Patch(edgecolor='black', facecolor='white', linewidth=2, label='Interdisciplinary Sector'))
    plt.legend(handles=legend_handles, loc='upper right', ncol=2, fontsize=9)

    plt.tight_layout()
    plt.show()

# Run
plot_colored_and_bold_interdisciplinary()


import matplotlib.pyplot as plt
import pandas as pd

# Creating the data manually based on the image
data = {
    'Course': [
        'Certificate (Forensic Tox)', 'B.Sc. (Biotech)', 'B.Sc. (Clinical Research)',
        'B.Sc. (Bio/Bot/Chem/Tox)', 'B.Sc. (Forestry)', 'B.Sc. (Mat. Sci. & Nanotech)',
        'M.Sc. (Biochem)', 'M.Sc. (Botany)', 'M.Sc. (Chemistry)', 'M.Sc. (Toxicology)',
        'M.Sc. (Biotech)', 'M.Sc. (Biotech) SFS', 'M.Sc. (Clinical Research)',
        'M.Sc. (Forensic Science)', 'M.Sc. (Pharmacovigilance)',
        'M.Tech. (Biotech)', 'M.Tech. (Biotech) SFS'
    ],
    '1st Year': [
        30000, 130000, 115000, 110000, 110000, 100000, 110000, 100000,
        100000, 100000, 120000, 220000, 120000, 110000, 100000,
        50000, 150000
    ],
    '2nd Year': [
        0, 130000, 115000, 110000, 110000, 100000, 110000, 100000,
        100000, 100000, 120000, 220000, 120000, 110000, 100000,
        50000, 150000
    ],
    '3rd Year': [
        0, 130000, 115000, 110000, 110000, 100000, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0
    ],
    '4th Year': [
        0, 130000, 115000, 110000, 110000, 100000, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]
}

df = pd.DataFrame(data)
df.set_index('Course', inplace=True)

# Plotting a grouped bar chart
fig, ax = plt.subplots(figsize=(14, 8))
df.plot(kind='bar', stacked=False, ax=ax)

plt.title('Year-wise Fee Structure for Courses in School of Chemical and Life Sciences (Jamia Hamdard)', fontsize=14)
plt.ylabel('Fee (INR)', fontsize=12)
plt.xlabel('Course', fontsize=12)
plt.xticks(rotation=90)
plt.legend(title='Year')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# Data for M.Sc. courses fee comparison among private universities in Delhi NCR
msc_fee_comparison = {
    'University': [
        'Jamia Hamdard', 'Amity University', 'Galgotias University', 'Sharda University'
    ],
    'M.Sc. Biotechnology': [
        240000, 300000, 180000, 340000  # Approximate total 2-year fees
    ],
    'M.Sc. Chemistry': [
        200000, 280000, 160000, 300000
    ],
    'M.Sc. Forensic Science': [
        220000, 300000, 0, 310000  # Galgotias doesn't list this clearly
    ],
    'M.Sc. Clinical Research': [
        240000, 0, 0, 0  # Only Jamia Hamdard offers this prominently
    ]
}

msc_df = pd.DataFrame(msc_fee_comparison)
msc_df.set_index('University', inplace=True)

# Plotting the grouped bar chart for M.Sc. fee comparison
fig, ax = plt.subplots(figsize=(12, 7))
msc_df.plot(kind='bar', ax=ax)

plt.title('M.Sc. Course Fee Comparison (Total 2-Year Fee) Among Private Universities in Delhi NCR', fontsize=14)
plt.ylabel('Fee (INR)', fontsize=12)
plt.xlabel('University', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Course', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
