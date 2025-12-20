# Visualisation des commandes – Northwind

## 1.  Description
Ce projet présente une analyse des commandes (livrées et non livrées) à l’aide de **Power BI** et de visualisations **Python** intégrées.  
Les données proviennent de deux sources distinctes de la base **Northwind** : SQL Server et Microsoft Access.

## 2.  Objectifs
- Analyser et comparer les commandes **livrées** et **non livrées**
- Centraliser des données issues de **sources hétérogènes**
- Concevoir un **modèle décisionnel** cohérent
- Créer des **visualisations interactives** et pertinentes
- Intégrer des **scripts Python** dans Power BI pour enrichir l'analyse

## 3.  Outils et technologies utilisés
- **Power BI** – modélisation, mesures DAX, tableaux de bord
- **Python** – Pandas, Matplotlib (visualisations intégrées dans Power BI)
- **SQL Server** – source principale des données Northwind
- **Microsoft Access** – source complémentaire
- **Overleaf (LaTeX)** – rédaction du rapport
- **CapCut** – montage vidéo de démonstration

## 4. Structure du projet
```text
├── powerbi/
│   └── Northwind.pbix
├── python/
│   ├── commonbert.py
│   ├── courbe.py
│   ├── donuts.py
│   └── Histogramme.py
├── images/
│   ├── tableau_de_bord.png
│   ├── resultatfinal.png
│   ├── commembert.png
│   ├── courbe.png
│   ├── histogramme.png
│   └── donut.png
├── report/
│   └── rapport.pdf
├── video/
│   └── video.txt
└── README.md



## 5. Exécution des scripts Python dans Power BI
Les scripts Python sont intégrés dans Power BI via le **visuel Python**.  
Pour les utiliser :

1. Ouvrir le fichier `powerbi/Northwind.pbix`
2. Insérer un **visuel Python** (icône Py dans la barre de visualisations)
3. Copier-coller le code souhaité depuis le dossier `python/`
4. Cocher les colonnes nécessaires dans le panneau **Données**
5. Le visuel se met à jour automatiquement

## 6. Reproduction des résultats
1. Charger les données depuis **SQL Server** et **Microsoft Access**
2. Vérifier et ajuster le **modèle relationnel** dans Power BI
3. Utiliser les **mesures DAX** existantes ou en créer de nouvelles si besoin
4. Générer les visualisations via les pages du rapport
5. Pour les graphiques Python, suivre la procédure ci-dessus

## 7. Sources des données
- **Northwind SQL Server** – tables de faits et dimensions principales
- **Northwind Access** – tables complémentaires et informations clients

## 8. Auteur
**Zouarqui Aya**  
Master 2 Big Data – Année universitaire 2025/2026
