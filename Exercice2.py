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
