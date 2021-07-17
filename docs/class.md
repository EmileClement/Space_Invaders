# Classe

Les classes utilisées sont les suivantes :

![Diagramme de classes](class.svg)

## Classe de representation

Pour representer les élements dans le jeu, on utilise les classes :

- ```Joueur``` qui n'est instancier qu'une seule fois, et qui represente le joueur,

- ```Monster``` qui represente les monstres,

- ```Missile``` qui represente les projectiles.

Des instances de la classe ```Missile``` sont memebres des deux autres classes car elles representent les projeciles de basse.

De plus, les threads ```Joueur_1``` et ```Block_Enemie``` envoie des objet ```Missile``` dans la ```queue_N``` vers le thread ```Projectile``` pour lui signaler les nouveaux missiles à simuler.

## Classe de messagerie

Les classes utiles pour les messages sont ```struct Collision``` qui peremt de transmetre toutes les informations relatives à un choc avec un monstre en même temps, et la class ```enum End_Type``` qui décrit le type de fin de vague que l'on rencontre (défaite des monstre ou du joueur).