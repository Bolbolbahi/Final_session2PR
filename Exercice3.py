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
