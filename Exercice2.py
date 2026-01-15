import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt6.QtCore import Qt


class CalculateurDouble(QWidget):
    def __init__(self):
        super().__init__()
        self.initialiser_interface()

    def calculer_double(self):
        try:
            texte_valeur = self.champ_saisie.text().strip()

            if not texte_valeur:
                QMessageBox.warning(self, 'Erreur', 'Veuillez entrer une valeur.')
                return
            valeur = float(texte_valeur)
            double = valeur * 2

            if double == int(double):
                self.champ_resultat.setText(str(int(double)))
            else:
                self.champ_resultat.setText(str(double))

        except ValueError:
            QMessageBox.warning(self, 'Erreur', 'Veuillez entrer un nombre valide.')

    def sauvegarder_resultat(self):
        texte_resultat = self.champ_resultat.text().strip()

        if not texte_resultat:
            QMessageBox.warning(self, 'Erreur', 'Aucun résultat à sauvegarder. Veuillez d\'abord calculer un double.')
            return

        try:
            with open('resultats.txt', 'w', encoding='utf-8') as fichier:
                fichier.write(texte_resultat)
            QMessageBox.information(self, 'Succès', 'Le résultat a été sauvegardé dans resultats.txt')
        except Exception as e:
            QMessageBox.critical(self, 'Erreur', f'Erreur lors de la sauvegarde : {str(e)}')

    def charger_resultat(self):
        try:
            with open('resultats.txt', 'r', encoding='utf-8') as fichier:
                contenu = fichier.read().strip()

            if not contenu:
                QMessageBox.warning(self, 'Attention', 'Le fichier resultats.txt est vide.')
                return
            try:
                float(contenu)
                self.champ_resultat.setText(contenu)
                QMessageBox.information(self, 'Succès', 'Le résultat a été chargé depuis resultats.txt')
            except ValueError:
                QMessageBox.warning(self, 'Erreur', 'Le contenu du fichier n\'est pas un nombre valide.')

        except FileNotFoundError:
            QMessageBox.warning(self, 'Erreur', 'Le fichier resultats.txt n\'existe pas.')
        except Exception as e:
            QMessageBox.critical(self, 'Erreur', f'Erreur lors du chargement : {str(e)}')