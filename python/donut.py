import matplotlib.pyplot as plt
import pandas as pd

df = dataset

# Palette de verts
palette = ['#2ca02c', '#98fb98']

# Agrégation par région
df_region = df.groupby('RegionDescription').agg({
    'commande_livree':'sum',
    'commande_nonlivree':'sum'
}).reset_index()

# Total par type de commande
totals = pd.DataFrame({
    'Type': ['Livrées', 'Non livrées'],
    'Valeur': [df_region['commande_livree'].sum(), df_region['commande_nonlivree'].sum()]
})

# Création du donut
plt.figure(figsize=(6,6))
wedges, texts, autotexts = plt.pie(
    totals['Valeur'],
    labels=totals['Type'],
    autopct='%1.1f%%',
    colors=palette,
    startangle=90,
    wedgeprops=dict(width=0.4)  # largeur pour faire un donut
)
plt.setp(autotexts, size=10, weight="bold")
plt.title("Répartition des commandes livrées vs non livrées (compact)", fontsize=12)
plt.tight_layout()
plt.show()
