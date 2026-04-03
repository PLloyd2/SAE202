from NoeudBinaire import *

class NoeudHuffman(NoeudBinaire):
    
    #Ce constructeur reprend les attributs de la classe parent
    def __init__(self,v,g,d):
        super().__init__(v,g,d)

    def encodage_huffman(self, code="", dic=None):
        #Création d'un dictionnaire {valeur,encodage}
        if dic is None:
            dic={}
        #Si la branche courante est un arbre, on affecte la valeur son chemin depuis la racine au dictionnaire
        if self.arbre_f():
            dic[self.v]=code 
        else:
            #On parcourt toutes les branches à gauche de la branche courante s'il en existe
            if self.arbre_gauche():
                self.g.encodage_huffman(code + "0", dic)
            
            #On parcourt toutes les branches à droite de la branche courante s'il en existe
            if self.arbre_droit():
                self.d.encodage_huffman(code + "1", dic)
        return dic
    
    @staticmethod
    def compression(texte, dic_encodage):
        # Variable qui correspond au texte traduit après la compression
        resultat = ""

        for char in texte:
            # On parcourt les clés du dictionnaire pour trouver celle qui contient notre caractère
            for cle_tuple in dic_encodage:
                # cle_tuple ressemble à ('a', 10)
                if cle_tuple[0] == char:
                    resultat += dic_encodage[cle_tuple]
                    break
        return resultat
    
    @staticmethod
    def tri_noeuds(liste_noeud):
        """Trie une liste d'objets NoeudHuffman par ordre décroissant de poids."""
        for i in range(len(liste_noeud)):
            maxi = i
            for j in range(i + 1, len(liste_noeud)):
                poids_maxi = liste_noeud[maxi].get_v()[1]
                poids_actuel = liste_noeud[j].get_v()[1]
                
                if poids_maxi < poids_actuel:
                    maxi = j
                    
            t = liste_noeud[i]
            liste_noeud[i] = liste_noeud[maxi]
            liste_noeud[maxi] = t

    @staticmethod
    def construction_arbre(table_effectif):
        liste_noeud = []
        #On initialise tous les tuples de la table des effectifs à une feuille
        for i in table_effectif:
            liste_noeud.append(NoeudHuffman(i,None,None))
        
        #Algorithme de Huffman
        while len(liste_noeud) > 1:
            noeud_gauche = liste_noeud.pop()
            noeud_droit = liste_noeud.pop()

            tuple_g = noeud_gauche.get_v()
            tuple_d = noeud_droit.get_v()

            nouveau_t = (tuple_g[0] + tuple_d[0], tuple_g[1] + tuple_d[1])

            nouveau_noeud = NoeudHuffman(nouveau_t,noeud_gauche,noeud_droit)
            liste_noeud.append(nouveau_noeud)

            NoeudHuffman.tri_noeuds(liste_noeud)
        
        return liste_noeud[0] #On retourne uniquement la racine


        
        
    