# Carnet
> Ce carnet va vous permettre d'écrire nos questions, le compte-rendu de vos discussions, nos problèmes rencontrés etc.. Cela nous permettra de rédiger la documentation finale.

## Semaine 1

### Patricia

Pendant la pause, nous avons définit notre sujet qui portera sur la catégorisation des recettes de cuisine. Avec ma camarade nous avons décidé de travailler sur ce sojet suite à notre fort intérêt pour la nourriture :)

Nous avons défini les catégories suivantes pour la classification des recettes :

1. **"Apéritif"** : Cette catégorie regroupe les recettes de petits gâteaux apéritifs faits maison.

2. **"Entrée"** : Ici, nous incluons les recettes d'entrées telles que les soupes froides, terrines, verrines, salades, etc.

3. **"Plat"** : Cette catégorie englobe les recettes de plats divers et variés.

4. **"Dessert"** : Toutes les recettes de desserts, quelle que soit leur nature, seront classées ici.

5. **"Boisson"** : Cette catégorie comprend les recettes de boissons faites maison, comme les cocktails, sirops, smoothies, milkshakes, etc.

Mais aussi, pendant cette pause, nous avons commencé à collecter des URLs de sites de recettes afin de constituer une base de données pour l'entraînement de notre programme. Ces liens sont actuellement répertoriés dans un document Google Calc.


Pour une meilleure organisation, nous avons classé les sites en deux catégories distinctes :

**Exemples de sites pour le test de notre programme :**
- [www.cuisineaz.com](www.cuisineaz.com)
- [https://larecette.net/](https://larecette.net/)
- [https://www.cuisineactuelle.fr/](https://www.cuisineactuelle.fr/)


**Exemples de sites pour l'entraînement du programme :**
- [www.750g.com](www.750g.com)
- [cuisine.journaldesfemmes.fr](cuisine.journaldesfemmes.fr)
- [chefsimon.com](chefsimon.com)
- [www.elle.fr](www.elle.fr)
- [marmithon.org](marmithon.org)
- [www.mesrecettesfaciles.fr](www.mesrecettesfaciles.fr)


### Lise

(26/02/2024)

- Nous avons choisis de travailler sur la classification des recettes de cuisine avec un corpus de liens depuis internet.

- Nos catégories seraient : apéritif / entrée / plat / dessert / boisson .


## Semaine 2 et 3

### Patricia
Cette semaine, j'ai terminé à récolter les liens pour la partie ***test***. Mais aussi, Lise a regardé les droits d’utilisation des données des sites de recettes de cuisine. En regardant, nous avons vu que nous pouvons aspirer les liens car nous ne sommes pas dans un cas où nous allons récupérer les liens pour une fin commerciale, mais dans le cas d'un devoir (privé).

De plus, cette semaine Lise a presque terminé de récupérer les liens pour notre partie ***entraînement***. 

Comme nous nous rencontrons tous les mardi pour en parler, nous allons voir la suite du projet et parler de l'avancement !

**(12/03/24)**
Lise a lancé le programme aspiration.sh pour récolter nos URLs d'entrainement et créer nos fichiers HTML. Ce programme a été récupéré, suite au cours de PPE1 du semestre 1.
En regardant ces fichiers, nous avons vu que le lien :
- [cuisine.journaldesfemmes.fr](cuisine.journaldesfemmes.fr) renvoyait des fichiers vides avec des erreurs

Ainsi, nous avons changé ce lien par celui-ci :
- [https://www.regal.fr/recettes](https://www.regal.fr/recettes)

### Lise

(12/03/24)

J'ai lancé le script d'aspiration qui est présent dans le dossier donnees/programmes/aspiration.sh. Ce dernier a été repris du travail fait en PPE1 au semestre dernier. Il vient aspirer nos URLs et créer nos fichiers xml d'aspiration. Ces derniers ont été rangés dans le dossier donnees/aspirations/ puis dans des sous dossiers triés par données d'entrainement ou de test et par type d'étiquette.
Le programme se lance de la manière suivante : bash aspiration.sh <nom_étiquette> <url_à_aspirer>.
En lançant l'aspiration, nous nous sommes rendu compte qu'un site bloque les aspirations, nou s devons donc trouver de nouvelles urls.

(13/02/24)

Nous avons ajouté les txt des urls de test, et ainsi fait leurs aspirations qui ont été rangées dans le dossier donnees/aspirations/test/ par site et par étiquette.

(17/03/24)

Ajout du programme qui récupère les dumps-text des aspirations html de nos sites.
La commande principale est la suivante `dumps=$(lynx -dump -nolist ../aspirations/${chemin}/${etiquette}-$i.html > ../dumps-text/${chemin}/${etiquette}-$i.txt)`. Elle peremt de récupérer les fichiers du dossier d'aspirations et de prendre le text sans url et les placer dans des dossiers prévus à cet effet dans `dumps-text/`. Voici l'exemple d'une commande lancé pour convertir les aspirations en dumps-text : `bash dump.sh entrainement/aperitif aperitif` pour les urls d'entrainement ou `bash dump.sh test/cuisineaz/entree cuisineaz_entree` pour les urls de test.
Le programme prend en argument une partie du chemin des aspirations et les étiquettes de chaque fichier.
Une boucle est utilisée pour itérer sur les fichiers de chaque dossier d'aspiration, elle tourne le nombre de fois correspondant au nombre de fichiers dans chaque dossier. Ceci est définit par la commande suivante : `ls ../aspirations/${chemin}/*.html | wc -l`, elle compte le nombre de fichier html dans le dossier indiqué en chemin.

Idée pour la suite :
- Pourrions-nous peut être faire un nettoyage dans nos données pour ne garder que ce qui nous intéresse à l'aide de regex. Par exemple : retirer tous les contenus textes des menus déroulant des pages, ne garder que les listes d'ingrédients et les indications de préparation.
