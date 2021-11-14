# Readme

Le dataset utilisé ici est celui des valeurs foncières de 2020. 

## Disposition des fichiers

Le dataset étant trop lourd, j'ai posté ici, uniquement le dataframe que j'ai utilisé pour mes analyses "modified_df.csv".

Vous retrouvrez donc le fichier "project.ipynb" qui est le notebook utilisé pour ce travail.

Toutefois, le fichier utilisé pour streamlit est le fichier "streamlit.py" qui ne contient aucune des modifications faites sur le dataset initial. Il contient juste les analyses donc les rendus visuels.

## Traitement des données

Il contenait au départ environs 2 millions de lignes mais parès traitement de la données, il n'en restait qu'environs 600 000. Le nombre de colonnes est quitté de 43 à 22. Pour le traitement des données, j'ai d'abord supprimé les colonnes qui avaient plus de 50% d'informations manquantes. En ce qui concerne les lignes, j'ai supprimé celles qui manquaient d'informations aussi.

Ensuite, j'ai uniformisé les types de chaque colonne

Enfin, j'ai renvoyé le résultat dans un fichier csv sous le nom "modified_df.csv"

## Analyse

Mon analyse a été axée principalement sur une analyse statistique. En effet, j'ai mené une étude pour par exemple, repérer quels sont les critères qui influencent le plus le prix d'un local. Ces critères étaient par exemple le département, le nombre de pièce du local en question, la surface du terrain...

J'ai aussi fait une analyse temporelle afin de suivre les achats en fonctions de la période dans l'année

Enfin, j'ai fait une analyse géographiques afin de repérer sur une carte par exemple les zones ayant le plus eu d'achats.
