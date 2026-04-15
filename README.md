SAÉ 2.02 - Compression de données par codage de Huffman
Ce projet vise à implémenter l'algorithme de Huffman, une méthode de compression de données sans perte, en utilisant la programmation orientée objet en Python.


Structure du projet
NoeudBinaire.py : Contient la classe de base pour la création et la gestion d'arbres binaires.
NoeudHuffman.py : Contient la classe héritée gérant spécifiquement la logique de l'algorithme de Huffman.
main.py : Script principal permettant de traiter en lot les fichiers textes à compresser.
input/ : Dossier devant contenir les fichiers textes (.txt) à traiter.
Fonctionnalités implémentées


La classe NoeudBinaire
Gestion de base : Constructeur, Getters, et Setters.
Tests d'état : Vérification si un nœud a un fils droit/gauche, s'il est une feuille, ou s'il est un arbre vide.
Métriques : Calcul récursif de la hauteur de l'arbre.
Parcours d'arbre : Implémentation des parcours préfixe, infixe, suffixe et en largeur.


La classe NoeudHuffman
Construction de l'arbre : Algorithme itératif (construction_arbre) fusionnant les deux nœuds de poids minimal jusqu'à l'obtention de la racine finale.
Génération des encodages : Parcours récursif pour attribuer 0 à la branche gauche et 1 à la branche droite, générant ainsi le dictionnaire de Huffman avec le code unique de chaque caractère.
Compression : Transformation du texte en une suite de 0 et de 1 optimisée à partir du dictionnaire généré.
Décompression : Algorithme permettant de reconstituer le texte d'origine.
Utilitaires : Nettoyage des caractères spéciaux (via unidecode), comptage des occurrences, tri personnalisé des nœuds, et calcul des tailles (conversion ASCII vers base 2).


Utilisation
Placez vos fichiers textes (extension .txt) dans le dossier nommé input/ situé à la racine du projet.
Ouvrez votre terminal et placez-vous dans le répertoire du projet.
Lancez le script en passant le nom du dossier en argument :
python main.py input/

