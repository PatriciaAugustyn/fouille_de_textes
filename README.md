# Projet M1 - Fouille de textes

> Ce projet a été finalisé le 01/05/2024 ... [ stay tuned ]

## En quoi consiste ce projet ?

Ce projet vise à explorer les techniques d'entraînement de classifieurs par apprentissage automatique et à comparer les performances de différents algorithmes de classification sur une tâche de fouille de texte. Notre sujet portera sur **la classification des recettes de cuisine**.

Ce projet a été réalisé par deux personnes formidables : 
- AUGUSTYN Patricia : Lien [GitHub](https://github.com/PatriciaAugustyn)
- BRISSET Lise : Lien [GitHub](https://github.com/Lise-Brisset)


Pour lancer nos programmes, nous vous proposons de créer un environnement virtuel :

- Créer l'environnement
```
python -m venv venv
```
- Activer l'environnement
```
source venv/bin/activate
```
- Installer les librairies Python :
```
pip install beautifulsoup4 requests
```

Pour lancer nos programmes, voici des lignes de commande que vous pouvez tester :

- **aspiration.sh** :

- **dump.sh** :
```
bash dump.sh boisson
```

Vous pouvez remplacer `boisson` par nos 5 catégories : `aperitif`, `entree`, `plat`, `dessert` et `boisson`

- **recover_data.py** :
```
python3 recover_data.py
```

- **urls_cleaner.py** :
```
python3 urls_cleaner.py
```
