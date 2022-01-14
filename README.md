# Open CV Power Point

## Description du projet.
Créer un contrôleur de Power Point via les mouvements du présentateur devant une caméra. Le but serait de pouvoir passer des slides, pointer des éléments d'une slide, tout cela à l'aide de mouvements du bras du présentateur.

## Prérequis.
  - Demander l'instalation des librairies nécessaires (Open CV, Pyautogui) sur deux ordinateurs portables de la salle 124.

## Partie 1 : Détection de mouvement.
Détection de mouvements avec la librairie [Open CV](https://pypi.org/project/opencv-python/) pour python.
  - Enlever l'arrière plan (garder que les pixels différents par rapport à des images précédentes). __Gwendal V.__
  - Ne garder que la personne principale (pour que des mouvements de personnes en arrière plan ne puissent pas influencer le travail du programme). __Gwendal V.__
  - Détecter les mouvements de bras de cette personnne (pour trouver quelle action réaliser sur Power Point). __Joseph J.__

## Partie 2 : Controle sur le système d'exploitation.
Action sur un clavier virtuel avec la librairie python [Pyautogui](https://github.com/asweigart/pyautogui).
  - Créer des fonctions qui vont renvoyer les différentes actions à réaliser à l'aide de raccourcis clavier ou de mouvements de souris (par exemple dans le cas d'un pointeur). __Gwendal V.__
  - Renvoyer un affichage vidéo filtré de la caméra (à but pédagogique). __Joseph J.__

## Pour aller plus loins.
 - Utilisation de médias (Réglage du volume, play, pause, suivant, précédent).
 - Souris virtuelle à l'aide de la caméra (déplacement, clicks, défilements).
