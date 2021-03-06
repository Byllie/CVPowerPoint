# Open CV Power Point
![Logo Magic_Hands](logo-magic-hand.png "Logo du  projet")
## __Description du projet.__
Créer un contrôleur de Power Point via les mouvements du présentateur devant une caméra. Le but serait de pouvoir passer des slides, pointer des éléments d'une slide, tout cela à l'aide de mouvements du bras du présentateur.

## __Prérequis.__
  - ~~Demander l'instalation des librairies nécessaires (Open CV, Pyautogui) sur deux ordinateurs portables de la salle 124~~

## __Plan du projet.__
### - Partie 1 : Détection de mouvement :
Détection de mouvements avec la librairie [Open CV](https://pypi.org/project/opencv-python/) pour python.
  - Enlever l'arrière plan (garder que les pixels différents par rapport à des images précédentes). _Gwendal V._
  - Ne garder que la personne principale (pour que des mouvements de personnes en arrière plan ne puissent pas influencer le travail du programme). _Gwendal V._
  - Détecter les mouvements de bras de cette personnne (pour trouver quelle action réaliser sur Power Point). _Joseph J._

### - Partie 2 : Controle sur le système d'exploitation :
Action sur un clavier virtuel avec la librairie python [Pyautogui](https://github.com/asweigart/pyautogui).
  - Créer des fonctions qui vont renvoyer les différentes actions à réaliser à l'aide de raccourcis clavier ou de mouvements de souris (par exemple dans le cas d'un pointeur). _Gwendal V._
  - Renvoyer un affichage vidéo filtré de la caméra (à but pédagogique). _Joseph J._

## __Pour aller plus loins.__
 - Utilisation de médias (Réglage du volume, play, pause, suivant, précédent).
 - Souris virtuelle à l'aide de la caméra (déplacement, clicks, défilements).

## __Avancement.__

| Date | GitHub | Programmation | Oral |
| :---: | :--- | :--- | :--- |
| 2022-01-14 | Création du repository / Création du cahier des charges | Etude de la librairie Open CV python | |
| 2022-01-21 | Création du fichier control_ptt.py et detection.py | Recherche de technique pour détecter les mouvements et création d'une fonction avec Pyautogui | |
| 2022-01-28 | Merge de la branche de dévelopement et la branch principal | Suppression du background, récupération d'un rectangle comprenant les mouvements, calculs de vecteurs afin de détecter un mouvement utilisable. Teste de lien avec notre fonction pyautogui de changement de slide | |
| 2022-02-04 | | Ajout de classe vecteur | |
| 2022-02-11 | | Réalisation de tests sur les différents vecteurs afin de déterminer la validité de ces derniers. Affichage des vecteurs pris valides. | |
| 2022-03-04 | | Correction des bug quant à l'affichage des vecteurs | |
| 2022-03-11 | | Création d'une fonction calculant les mouvements réalisés. Implémentation du mouvement gauche à droite | |
| 2022-03-18 | | Création de logos et réarengement de l'interface utilisateur Tkinter | |
| 2022-03-25 | | Passage de la limite de détection de pixel à % d'écran | |
| 2022-03-30 | Ajout du logo dans le markdown  | | |
| 2022-04-01 | Création d'une branch dédiée aux tests de détection de couleur | Création d'un fichier de test de détection de couleur. Ajout de boutons "radios" dans l'interface Tkinter | |
| 2022-04-08 | | Amélioration de l'interface tkinter. Amélioration de la détection de couleur avec une sélection de couleur | |
| 2022-04-12 | | Ajout des commandes pour le mode musique | |
| ????-??-?? | | AJout de selection couleur via une fenêtre native | |
| ????-??-?? | | AJout de selection couleur via case à remplir en hex | |
| 2022-05-13 | | Ajout du mode souris + finition détection de coueleur (passage en hsv) | |
| 2022-05-14 | | Regler bug du mode souris + docstrings| |
| 2022-05-15 | | Ajout de commentaire explicatif | début diaporama + fiche d'utilisation du projet  | 
| 2022-05-17 | | Correction du ficher de démonstration pour l'oral | Vérification du diaporama |
