import matplotlib.pyplot as plt
import pandas as pd

# Dataset Power BI
df = dataset

# Palette de verts pour 17 clients
palette_vert = [
    '#006400', '#228B22', '#2E8B57', '#3CB371', '#66CDAA', '#8FBC8F', '#20B2AA',
    '#32CD32', '#98FB98', '#00FF7F', '#7CFC00', '#ADFF2F', '#9ACD32', '#6B8E23',
    '#556B2F', '#66CDAA', '#8FBC8F'
]

# Agrégation commandes livrées par client
df_clients = df.groupby('id_seqclient')['commande_livree'].sum().reset_index()

# On garde les 17 clients avec le plus de commandes
df_clients_top17 = df_clients.sort_values(by='commande_livree', ascending=False).head(17)

# Création du camembert
plt.figure(figsize=(8,8))
plt.pie(
    df_clients_top17['commande_livree'],
    labels=df_clients_top17['id_seqclient'].astype(str),
    autopct='%1.1f%%',
    colors=palette_vert,
    startangle=90
)
plt.title("Répartition des commandes livrées des 17 clients principaux\n(Chaque secteur = part d'un client)", fontsize=12)
plt.tight_layout()
plt.show()
