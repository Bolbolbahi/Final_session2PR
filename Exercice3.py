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