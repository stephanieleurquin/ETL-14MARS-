import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1️⃣ Données de ventes
# -------------------------
ventes = [
    {'produit': 'ordinateur', 'quantite': 2},
    {'produit': 'souris', 'quantite': 5},
    {'produit': 'clavier', 'quantite': 3},
    {'produit': 'ordinateur', 'quantite': 1},
    {'produit': 'souris', 'quantite': 2},
    {'produit': 'webcam', 'quantite': 4},
]

# Charger dans un DataFrame
df = pd.DataFrame(ventes)
print("Données originales :")
print(df)

# -------------------------
# 2️⃣ Transformation
# -------------------------
# Somme des quantités par produit
df_grouped = df.groupby('produit')['quantite'].sum().reset_index()

# Classement par nombre de ventes
df_grouped['rang'] = df_grouped['quantite'].rank(method='dense', ascending=False).astype(int)

print("\nDonnées transformées :")
print(df_grouped)

# -------------------------
# 3️⃣ Visualisation
# -------------------------
plt.figure(figsize=(6,4))
sns.barplot(data=df_grouped, x='produit', y='quantite', palette='viridis')
plt.title("Top ventes par produit")
plt.ylabel("Quantité vendue")
plt.xlabel("Produit")
plt.show()
