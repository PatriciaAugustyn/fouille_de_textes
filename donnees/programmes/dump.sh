#!/usr/bin/env bash

etiquette=$1
nb_fichiers_html=$(ls ../clean-html/all/${etiquette}/*.html | wc -l)

for (( i=100; i<=${nb_fichiers_html}; i++ ))
do
	dumps=$(lynx -dump -nolist ../clean-html/all/${etiquette}/$i*.html > ../corpus/all/${etiquette}/${etiquette}-$i.txt)
done

# commande lancement : bash dump.sh boisson
