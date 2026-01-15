class Triangle:
    def __init__(self, n):
        self.n = n
    def triangle_gauche(self):
        lignes=[]
        for i in range(1,self.n+1):
            lignes.append("*"*i)
        return lignes
    def triangle_droite(self):
        lignes=[]
        for i in range(1,self.n+1):
            espaces=" "*(self.n-i)
            etoiles="*"*i
            lignes.append(espaces+etoiles)
        return lignes

class Affichage:
    def afficher_cote_a_cote(self, triangle_droite, triangle_gauche):
        for d, g in zip(triangle_droite, triangle_gauche):
            print(d + "    " + g)
n=int(input("Entrez un entier n : "))

triangle = Triangle(n)
affichage = Affichage()

droite = triangle.triangle_droite()
gauche = triangle.triangle_gauche()

affichage.afficher_cote_a_cote(droite, gauche)

