from NoeudBinaire import *
from NoeudHuffman import *

def comptage(txt):
    dic={}
    for i in txt:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic

def dic_to_tab(dic):
    tab=[]
    for i in dic:
        tab.append((i,dic[i]))
    return tab

def tri_tab(tab):
    for i in range (len(tab)):
        maxi=(tab[i], i)
        for j in range (i+1,len(tab)):
            if maxi[0][1]<tab[j][1]:
                maxi=(tab[j], j)
        tab[maxi[1]]=tab[i]
        tab[i]=maxi[0]
    return tab

def code_complete():
    #Demande de la saisie du texte à compresser
    texte_a_compresse = str(input("Insérer le texte à compression :\n"))

    #On calcule la table des effectifs du texte
    table_effectif = comptage(texte_a_compresse)

    #On transforme la table en liste de tuples pour pouvoir lancer la construction de l'arbre
    dictionnaire = tri_tab(dic_to_tab(table_effectif))

    #Construction de l'arbre de Huffman
    arbre_Huffman_racine = NoeudHuffman.construction_arbre(dictionnaire)

    #Calcul de la table d'encodage
    table_encodage = arbre_Huffman_racine.encodage_huffman()

    #Traduction du texte à l'aide de la table des encodages
    texte_a_renvoyer =  NoeudHuffman.compression(texte_a_compresse,table_encodage)

    #Affichage du texte traduit
    print(texte_a_renvoyer)

    return texte_a_renvoyer

if __name__ == "__main__":
    code_complete()

