# Projet MagikHand

_Joseph Jaujay / Gwendal Vantourout_

### Librairies nécessaires :

- [CV2 (Open CV python)](https://pypi.org/project/opencv-python/).
- [Pyautogui](https://github.com/asweigart/pyautogui).
- [Tkinter](https://docs.python.org/fr/3/library/tkinter.html).
- Autres librairies diverses telles que _numpy_, _math_ et _time_.

### Utilisation :

Ouvrir et exécuter le programme python [_detection.py_](./detection.py).

#### -> Pour le mode PowerPoint :
1. Une fois la fenêtre Tkinter ouverte, selectionner "PowerPoint". Vous pouvez également à cette occasion modifier différents paramètres vidéos (pixellisation, sensibilité, longueur du déplacement nécessaire au déclanchement d'un action.)
2. Il faut ensuite cliquer sur le bouton de lancement ("Lancer la camera"), et partir de l'arrière plan pendant 5 secondes. En effet, la detection de mouvement se base sur la différence entre une image d'arrière plan, et l'image en direct. Ainsi, au bout du delay de 5 secondes, le programme enregistre l'arrière plan. Il faut donc qu'il n'y ai rien qui ne puisse bouger (par exemple l'utilisateur), mais également ne pas bouger le cadrage de la caméra.
3. Une fois l'arrière plan enregistré, le programme cherchera automatiquement le groupe de pixels changeants qui sont situés le plus a droite. Ainsi, c'est la main droite, lorsqu'elle est bien désolidarisée du corps, qui est détectée. Lorsque qu'un mouvement est détecté (mouvement raisonnablement lent de la main droite vers la droite ou la gauche), les vecteurs de déplacements calculés s'afficherons de couleur sur la fenêtre vidéo.
4. Pour pouvoir ensuite utiliser le programme dans un PowerPoint, il suffit de selectionner la fenêtre d'un diaporama pour que ce dernier s'anime au gré de vos mouvements.
5. Pour arrêter le programme, il suffit tout simplement de presser la touche "q" _(comme "quit")_ du clavier.

#### -> Pour le mode Musique :
1. Une fois la fenêtre Tkinter ouverte, selectionner "Musique". Vous pouvez également à cette occasion modifier différents paramètres vidéos.
2. De même, une fois le programme lancé il attendra 5 secondes avant d'enregistrer l'arrière plan. Il est donc demandé à l'utilisateur de se retirer du champs de la caméra utilisée, et de ne plus modifier le cadrage.
3. Encore une fois, la détection de mouvement se base sur le pixel le plus à droite de votre corps (votre bras droit). Ainsi, en montant ou descendant votre bras, vous augmenterez ou baisserez le son de votre ordinateur. Et d'un mouvement vers la gauche, vous passerez à la musique suivante, tandis qu'un mouvement vers la droite vosu fera revenir à morceau précédent.
4. Pour arrêter le programme il suffit encore une fois de presser "q".

#### -> Pour le monde Souris :
1. Selectionner le mode "Souris".
2. Selectionner une couleur en rentrant le code hexadécimal, ou via la fenêtre sélélection de couleur, ou encore via la caméra. Pour sélectionner une couleur via la caméra, cliquez sur le bouton "Choisir la couleur depuis la camera" et placez l'objet de la couleur à sélectionner au centre de la caméra (représenté par une petite croix dans la fenêtre vidéo) jusqu'à ce que la dite fenêtre disparaisse.
3. Lancer le mode souris. La couleur sera automatiquement détectée, et bougera le curseur de la souris en concéquance.
4. Pour stopper le programme, presser la touche "q" du clavier.