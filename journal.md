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


## Semaine 4 et 5

### Lise

(14/04/24)

#### constitution du corpus all/ :

Je me suis occupée des urls de train. Nous avons eu un rappel qui était de faire 80% de train et 20% de test. Or, nous étions parti sur 50/50, ce qui n'était pas une très bonne idée, car il faut une assez grande quantité de train pour obtenir un modèle performant et un minimum de test pour vérifié si ce dernier catégorise correctement et pas de manière aléatoire.

Cependant, en revisionnant la vidéo tuto de Weka, nous avons compris que le logiciel fait lui-même le split entre train et test. Ainsi notre corpus peut être regroupé dans un même dossier et non pas séparé entre train et test.
J'ai donc fait un script basé sur le programme beautifulsoup créé par Patricia, qui permet de récupéré les balises nous intéressant en fonction du site parcouru. Voir `recover_date.py`.
J'ai placé toutes les urls train + test dans de nouveaux fichiers txt nommés comme `all_url_plat_ent.txt` pour pouvoir toutes les parcourir en même temps et renvoyé les fichiers html correspondant dans le dossier `/clean-text/all/`.
Le programme va parcourir de lui-même chaque fichier txt contenant les urls des 5 étiquettes différentes.

```py
etiquettes=["entree", "plat", "dessert", "aperitif", "boisson"]

for num_eti in range(len(etiquettes)):
    etiquette = etiquettes[num_eti]

    with open(f"../URLs/all_url_{etiquette}_ent_clean.txt", "r") as urls:
        for i, line in enumerate(urls):

        [...]

                with open(f"../clean-text/all/{etiquette}/{k}_{etiquette}_{site}.html", "w", encoding="utf-8") as file:
                    file.write(str(content))
    print("Aspiration de ",etiquettes[num_eti], " terminée !")
```

En procédant comme celà, nous avons remarqué que des urls posées problèmes en particulier celles du site chefsimon et 750g. En effet, dans le cas du site chefsimon, le problème vient du fait que le site n'est pas homogène et les div ne sont aps nommées de la même manière entre chaque page. Pour le site 750g, le problème est que pour certaines urls, les recettes sont inéxistantes et la page présente juste un lien vers un autre site contenant la recette en question.
Nous avons donc retiré manuellement les urls dans ce cas. Car après de nombreux essaie par le code, nous n'avons pas trouvé de manière automatique de passer automatiquement les urls qui n'ont pas la div demandée avec beautifulsoup.


#### choix des div :

Concernant le choix des div, comme les sites ne sont pas tous formés de la même manière, nous avons choisi que dans le pire des cas nous prendrons les instructions de la recette (car ce dernier contient du vocabulaire + les citations des ingrédients), dans le meilleur des cas nous prenons le titre, la liste d'ingrédients et les instructions. Nous devons nous restreindre à ces choix car pour certains sites nous aurions été contraintes à prendre aussi en compte toutes les informations textuelles renvoyant à d'autres articles de recette, et ceci aurait influencer nos futurs résultats.
Ex : avoir une suggestion d'article d'un dessert alors que la recette actuelle est une entrée.
Voilà les effectif avant / après nettoyage manuel :

- aperitif : 190 -> 180
- plat : 190 -> 182
- entree : 190 -> 175
- dessert : 190 -> 190
- boisson : 190 -> 166


#### suppression des doublons

A ce stade de notre avancement, nous nous sommes rendues compte de la présence de doublons dans les listes de nos urls. Pour remédier à cela automatiquement, nous avons fait un programme qui vient retirer les doublons et réécrit une nouvelle liste sans doublons dans un nouveau document txt contenant le mot clean, tel que `all_url_plat_ent.txt` devient `all_url_plat_ent_clean.txt`. Voilà la liste de nos nouveaux effectifs pour chaque étiquettes :

- aperitif : 180 -> 169
- plat : 182 -> 182
- entree : 175 -> 173
- dessert : 190 -> 183
- boisson : 166 -> 163

Le programme servant à faire ce nettoyage s'appelle `urls_cleaner.py` et contient les lignes de code suivantes :

```py
etiquettes=["aperitif", "entree", "plat", "dessert", "boisson"]

for i in range(len(etiquettes)):
    txt = open(f"../URLs/all_url_{etiquettes[i]}_ent.txt", "r")
    urls = txt.readlines()
    txt.close()

    urls_nettoyees = []
    for url in urls:
        if url not in urls_nettoyees:
            urls_nettoyees.append(url)
        else:
            continue

    txt_nettoye = open(f"../URLs/all_url_{etiquettes[i]}_ent_clean.txt", "a")
    txt_nettoye.writelines(urls_nettoyees)
    txt_nettoye.close()
```


#### prochain objectif :

Savoir si la variation de nos effectifs pose problème pour la suite, convertir tous ces fichiers html en format txt vers le dossier `donnees/corpus/all/`.

(20/04/24)

#### constitution du corpus entier final de manipulation pour weka

==> La variabilité de nos effectifs dans les données n'est aps grave car ce qui compte c'est la quantité de mots que contient chaque partie du corpus par étiquette.

Le corpus corpus/all/ vient d'être créé. Il contient tout les html du corpus clean-html/all/ en version dump-text.
C'est ce corpus que l'on va lancé dans Weka.
Le dossier clean-text/ a été renommé en clean-html/ car il ne contient que des documents html.

C'est le script bash dump.sh qui a été utilisé pour convertir tous nos documents html en document dump-text. Quelque modification y ont été faite car les fichiers n'était plus nommés de la même manière :

```sh
#!/usr/bin/env bash

etiquette=$1
nb_fichiers_html=$(ls ../clean-html/all/${etiquette}/*.html | wc -l)

for (( i=100; i<=${nb_fichiers_html}; i++ ))
do
	dumps=$(lynx -dump -nolist ../clean-html/all/${etiquette}/$i*.html > ../corpus/all/${etiquette}/${etiquette}-$i.txt)
done

# commande lancement : bash dump.sh boisson
```

`for (( i=100; i<=${nb_fichiers_html}; i++ ))` et `../clean-html/all/${etiquette}/$i*.html` : ces deux lignes ont subits des modifications pour d'abord convertir les fichiers entre 0 et 10 puis les fichiers entre 10 et 100 et les fichiers au dessus de 100.
