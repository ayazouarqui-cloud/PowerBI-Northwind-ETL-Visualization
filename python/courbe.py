import matplotlib.pyplot as plt
import pandas as pd

df = dataset

# Couleur
color3 = '#2ca02c'

# Agrégation commandes livrées par mois
df_time = df.groupby('AnneeMois')['commande_livree'].sum().reset_index()

plt.figure(figsize=(10,4))
plt.plot(df_time['AnneeMois'], df_time['commande_livree'], color=color3, marker='o', linewidth=2)
plt.title("Évolution des commandes livrées")
plt.xlabel("Année-Mois")
plt.ylabel("Commandes livrées")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
