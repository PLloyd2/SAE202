class NoeudBinaire():
    def __init__(self, v, g, d):
        self.v=v
        self.set_gauche(g) 
        self.set_droit(d)

        
    def __str__(self, h=0):
        "Affichage de l'arbre binaire de manière structurée"
        if h == 0:#le début
            chaine = str(self.v) + "\n" 
        else:
            chaine = "     " * (h - 1) + "|--> " + str(self.v) + "\n" #affichage du noeud avec une indentation en fonction de sa hauteur
        if self.g is None and self.d is None:#si c'est une feuille
            return chaine
        if self.g is not None:#si il y a un enfant gauche
            chaine += self.g.__str__(h + 1)
        else: #si il n'y a pas d'enfant gauche, on affiche une ligne vide pour garder la structure de l'arbre
            chaine += "     " * h + "|--> \n"
            
        if self.d is not None: #si il y a un enfant droit
            chaine += self.d.__str__(h + 1) #affichage de l'enfant droit avec une indentation en fonction de sa hauteur
        else:
            chaine += "     " * h + "|--> \n" #si il n'y a pas d'enfant droit, on affiche une ligne vide pour garder la structure de l'arbre
        return chaine
        
    
    def get_v(self):
        return self.v
    def get_g(self):
        return self.g
    def get_d(self):
        return self.d
    
    def set_v(self, nouveau_v):
        self.v=nouveau_v              
    def set_gauche(self, nouveau_g):
        if nouveau_g is not None and not isinstance(nouveau_g, NoeudBinaire):
            raise TypeError("L'enfant gauche doit être de type NoeudBinaire ou None.")
        self.g = nouveau_g
    def set_droit(self, nouveau_d):
        if nouveau_d is not None and not isinstance(nouveau_d, NoeudBinaire):
            raise TypeError("L'enfant droit doit etre de type NoeudBinaire ou None.")
        self.d = nouveau_d

    def arbre_gauche(self):
        """Retourne True si le noeud a un enfant gauche, False sinon"""
        return self.g is not None
    def arbre_droit(self):
        """Retourne True si le noeud a un enfant droit, False sinon"""
        return self.d is not None
    def arbre_f(self):
        """Retourne True si le noeud est une feuille, False sinon"""
        return self.g is None and self.d is None
    def arbre_v(self):
        """Retourne True si le noeud est un arbre vide, False sinon"""
        return self.v is None and self.g is None and self.d is None
    
    def hauteur(self):
        """Retourne la hauteur de l'arbre binaire"""
        if self.arbre_v():
            return 0
        if self.arbre_gauche():
            hg=self.g.hauteur()
        else:
            hg=0
        if self.arbre_droit():
            hd=self.d.hauteur()
        else:
            hd=0
        return 1+max(hg,hd)

    def prefixe(self):
        """Retourne la liste des valeurs de l'arbre binaire selon un parcours en préfixe"""
        tab=[]
        if self.v is not None: 
            tab.append(self.v)
        if self.arbre_gauche():
            tab+=self.g.prefixe()
        if self.arbre_droit():
            tab+=self.d.prefixe()
        return tab
    
    def suffixe(self):
        """Retourne la liste des valeurs de l'arbre binaire selon un parcours en suffixe"""
        tab=[]
        if self.arbre_gauche():
            tab+=self.g.suffixe()
        if self.arbre_droit():
            tab+=self.d.suffixe()
        tab.append(self.v)
        return tab
    
    def infixe(self):
        """Retourne la liste des valeurs de l'arbre binaire selon un parcours en infixe"""
        tab=[]
        if self.arbre_gauche():
            tab+=self.g.infixe()
        tab.append(self.v)
        if self.arbre_droit():
            tab+=self.d.infixe()
        return tab
    
    def Largeur(self):
        """Retourne la liste des valeurs de l'arbre binaire selon un parcours en largeur"""
        tab=[]
        racine=[self]
        while len(racine)>0:
            noeud= racine.pop(0)
            tab.append(noeud.v)
            if noeud.g is not None:
                racine.append(noeud.g)
            if noeud.d is not None:
                racine.append(noeud.d)
        return tab
