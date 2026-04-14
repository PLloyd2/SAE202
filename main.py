import sys
import os
import time
from unidecode import unidecode
from NoeudBinaire import *
from NoeudHuffman import *
import time

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

    if len(sys.argv) < 2:
        print("Erreur : Spécifiez le dossier en paramètre (ex: python3 main.py input/)")
        return

    input_dir = sys.argv[1]

    for f in os.listdir(input_dir):
        if f.endswith('.txt'):
            f_path = os.path.join(input_dir, f)
            print(f"\nFichier {f_path} chargé.")

            # Ouvrir et lire le fichier
            with open(f_path, 'r', encoding='utf-8') as file:
                contenu_brut = file.read()
            
            texte = unidecode(contenu_brut)
            print("Encodage du texte en ASCII OK.")
            print("Construction de l'arbre de Huffman. Compression du texte.")

            #début du programme de compression
            debut = time.time()

            #On calcule la table des effectifs du texte
            table_effectif = comptage(texte)

            #On transforme la table en liste de tuples pour pouvoir lancer la construction de l'arbre
            dictionnaire = tri_tab(dic_to_tab(table_effectif))

            #Construction de l'arbre de Huffman
            arbre_Huffman_racine = NoeudHuffman.construction_arbre(dictionnaire)
            print("Construction de l'arbre OK.")
            #Calcul de la table d'encodage
            table_encodage = arbre_Huffman_racine.encodage_huffman()
            
            #Traduction du texte à l'aide de la table des encodages
            texte_compresse =  NoeudHuffman.compression(texte,table_encodage)

            #fin du programme de compression
            fin = time.time()
            temps_execution = round(fin-debut,4) #temps d'exécution du programme de compression (hors calcul de la mémoire)

            #Taille des texte
            texte_binaire = ""
            for c in texte:
                texte_binaire += NoeudHuffman.ascii_vers_base2(c)

            taille_avant_compression = len(texte_binaire)
            taille_apres_compression = len(texte_compresse)

            taux_compression = round(taille_apres_compression/taille_avant_compression, 2)

            #Affichage du texte traduit
            print("\nTexte compressé :")
            print(texte_compresse)

            #Affichage des données utiles
            print("\nTaille du texte avant la compression : ", taille_avant_compression, "bits")
            print("Taille du texte après la compression : ", taille_apres_compression, "bits")
            print("Taux de compression : ", taux_compression*100, "%")
            print("Temps d'éxécution du programme de compression",temps_execution,"secondes")
            
            #preuve de la décompression
            texte_decompresse = arbre_Huffman_racine.decompression(texte_compresse)
            if texte == texte_decompresse:
                print("Test de décompression : SUCCÈS ")
            else:
                print("Test de décompression : ÉCHEC")
if __name__ == "__main__":
    code_complete()