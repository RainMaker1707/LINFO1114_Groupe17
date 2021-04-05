# LINFO1114_Groupe17
Projet dans le cadre du cours LINFO1114 - Mathématiques discrètes de l'UCLouvain

Différentes commandes vous sont accessible:
- -v, --verbose: affiche le fichier csv choisi et le temps d'exécution des différents algorithmes.
- -t, --test: Permet de faire tourner les test avant le programme main.
- -to, --testOnly: Permet de faire tourner uniquement les tests.
- -f FILE, --file FILE: vous permet de spécifier un fichier .csv d'entrée qui sera transofrmer en matrice et utilisé 
afin de faire tourner nos algorithmes.

Merci d'utiliser des fichiers .csv ou de n'importe quel format respectant la syntaxe:
int / float, int / float, int / float, ... , int / float\n pour chaque ligne d'entrée dans votre fichier.

Les conditions du projet étant que le graphe est non dirigé une matrice non carré (n x n) et non symétrique sera refusé
par l'implementation de dijkstra.

Les algorithmes se trouvent dans le dossier "scripts"
et les graphes de test dans le dossier "res".