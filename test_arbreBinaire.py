from NoeudBinaire import *
def test_NoeudBinaire():
    g = NoeudBinaire('G', None, None)
    f = NoeudBinaire('F', g, None)
    e = NoeudBinaire('E', None, f)
    d = NoeudBinaire('D', None, None)
    c = NoeudBinaire('C', None, None)
    b = NoeudBinaire('B', c, d)
    a = NoeudBinaire('A', b, e)

    assert g.get_v() == 'G'
    g.set_v('Z')
    assert g.get_v() == 'Z'
    g.set_v('G')
    
    try:
        a.set_gauche("eurreur")
    except TypeError:
        pass

    assert g.arbre_f() is True
    assert a.arbre_f() is False
    assert e.arbre_gauche() is False
    assert e.arbre_droit() is True
    
    arbre_vide = NoeudBinaire(None, None, None)
    assert arbre_vide.arbre_v() is True

    assert g.hauteur() == 1
    assert a.hauteur() == 4

    assert a.prefixe() == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert a.suffixe() == ['C', 'D', 'B', 'G', 'F', 'E', 'A']
    assert a.infixe() == ['C', 'B', 'D', 'A', 'E', 'G', 'F']
    assert a.Largeur() == ['A', 'B', 'E', 'C', 'D', 'F', 'G']

if __name__ == "__main__":
    test_NoeudBinaire()