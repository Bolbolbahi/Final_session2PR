class Outils:
    def saisir(self):
        nombres = []
        for i in range (10):
            while True:
                try:
                    valeur = int(input(f"Entrez l'entier #{i+1}: "))
                    nombres.append(valeur)
                    break
                except ValueError:
                    print("Erreur : veuillez entrer un entier valide.")
        return nombres
    def minimum(self,nombres):
        min_value = nombres[0]
        for nombre in nombres:
            if nombre < min_value:
                min_value = nombre
        return min_value

    def maximum(self,nombres):
        max_value = nombres[0]
        for nombre in nombres:
            if nombre > max_value:
                max_value = nombre
        return max_value
    def somme(self,nombres):
        somme = 0
        for nombre in nombres:
            somme += nombre
        return somme
    def moyenne(self,nombres):
        return self.somme(nombres)/len(nombres)

outils = Outils()

liste_nombres = outils.saisir()

print("Minimum :", outils.minimum(liste_nombres))
print("Maximum :", outils.maximum(liste_nombres))
print("Somme :", outils.somme(liste_nombres))
print("Moyenne :", outils.moyenne(liste_nombres))

