import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt6.QtCore import Qt


class CalculateurDouble(QWidget):
    def __init__(self):
        super().__init__()
        self.initialiser_interface()