from NoeudHuffman import *
from NoeudBinaire import *

def test_noeudHuffman():
    #Test de la fonction tri_noeuds()
    def test_tri_noeuds():
        n1 = NoeudHuffman(('a', 10), None, None)
        n2 = NoeudHuffman(('b', 50), None, None)
        n3 = NoeudHuffman(('c', 20), None, None)
        
        liste = [n1, n2, n3]
        NoeudHuffman.tri_noeuds(liste)
        
        # On vérifie que le premier a bien le poids 50
        assert liste[0].get_v()[1] == 50
        # On vérifie que le dernier a bien le poids 10
        assert liste[2].get_v()[1] == 10
        print("Test tri_noeuds : OK")

    #Test de la fonction construction_arbre()
    def test_construction_arbre():
        table = [('a', 5), ('b', 2)] # Total 7
        racine = NoeudHuffman.construction_arbre(table)
        
        # La racine doit avoir le poids total
        assert racine.get_v()[1] == 7
        # La valeur doit contenir les deux lettres (l'ordre dépend de ton tri)
        assert 'a' in racine.get_v()[0] and 'b' in racine.get_v()[0]
        # On vérifie qu'il y a bien des enfants
        assert racine.get_g() is not None
        assert racine.get_d() is not None
        print("Test construction_arbre : OK")

    def test_huffman_complet():
        table = [('a', 10), ('b', 1)]
        racine = NoeudHuffman.construction_arbre(table)
        dic = racine.encodage_huffman()
        
        # On teste avec les tuples car ce sont tes clés réelles
        assert ('a', 10) in dic
        assert ('b', 1) in dic
        
        # Test de la compression avec ta nouvelle méthode adaptée
        texte = "ab"
        compresse = NoeudHuffman.compression(texte, dic)
        
        # Vérification du résultat
        assert len(compresse) == 2
        assert compresse == dic[('a', 10)] + dic[('b', 1)]
        print("Test Huffman complet : OK")

    #Lancement des 3 tests
    test_tri_noeuds()
    test_construction_arbre()
    test_huffman_complet()

if __name__ == "__main__":
    test_noeudHuffman()