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
class Affichage :
    def afficher (self, lignes):
        for ligne in lignes:
            print(ligne)


n=int(input("Entrez un entier n : "))

triangle = Triangle(n)
affichage = Affichage()

affichage.afficher(triangle.triangle_droite())
print()
affichage.afficher(triangle.triangle_gauche())
print()

