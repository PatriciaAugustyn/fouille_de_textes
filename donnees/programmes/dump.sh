#!/usr/bin/env bash

chemin=$1
etiquette=$2
nb_fichiers_html=$(ls ../aspirations/${chemin}/*.html | wc -l)

for (( i=1; i<=${nb_fichiers_html}; i++ ))
do
	dumps=$(lynx -dump -nolist ../aspirations/${chemin}/${etiquette}-$i.html > ../dumps-text/${chemin}/${etiquette}-$i.txt)
done
