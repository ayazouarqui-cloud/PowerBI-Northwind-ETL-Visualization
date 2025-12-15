import matplotlib.pyplot as plt
import pandas as pd

df = dataset

# Palette
palette2 = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Agrégation commandes non livrées par employé
df_emp = df.groupby('LastName')['commande_nonlivree'].sum().reset_index()

plt.figure(figsize=(8,4))
plt.bar(df_emp['LastName'], df_emp['commande_nonlivree'], color=palette2[:len(df_emp)])
plt.title("Commandes non livrées par Employé")
plt.xlabel("Employé")
plt.ylabel("Commandes non livrées")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
