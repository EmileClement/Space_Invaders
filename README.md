# Projet Space Invaders

## Technique:

### Interaction entre les threads:
![Diagramme d'état du domaine](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/EmileClement/Space_Invaders/master/Biblio/UML/threads.puml&fmt=svg)

### Communication UDP


### Jsp pourquoi le read me est cassé

Pour indiquer le joueur, on utilise 1 et pour les méchants on utilise 0.

### Game_master

Si le game master reçoit un message via FHandle, une des deux entités est morte. Si la variable vaut 0, les méchants sont mort. Si elle vaut 1, le joueur est mort.
 
