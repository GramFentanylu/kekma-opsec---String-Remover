import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton,
    QLabel, QMessageBox, QHBoxLayout, QFormLayout, QGroupBox, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import pymem

from opsecdix import get_stylesheet

# Wielkosc ramki
class OpsecGod(QDialog):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(500, 400)
        self.init_ui()
        self.apply_style()

    def init_ui(self):
        self.outer_layout = QVBoxLayout(self)

        # Główna ramka
        self.frame = QFrame()
        self.frame.setObjectName("MainFrame")
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)

        # pasek tytułu
        title_bar = QHBoxLayout()
        self.title = QLabel("OPSEC GOD")
        self.title.setFont(QFont("Segoe UI", 15, QFont.Bold))
        self.title.setObjectName("TitleLabel")
        close_btn = QPushButton("✕")
        close_btn.setFixedWidth(40)
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #888;
                font-size: 11pt;
                border: none;
            }
            QPushButton:hover {
                color: red;
            }
        """)
        title_bar.addWidget(self.title)
        title_bar.addStretch()
        title_bar.addWidget(close_btn)
        self.frame_layout.addLayout(title_bar)

        # przełączenie motywu
        self.theme_btn = QPushButton("Toggle Dark Mode")
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.frame_layout.addWidget(self.theme_btn)

        # Pola wejściowe
        form_group = QGroupBox()
        form_layout = QFormLayout()

        self.pid_input = QLineEdit()
        self.addr_input = QLineEdit()
        self.len_input = QLineEdit()

        # Set minimum width and expanding size policy to ensure full text visibility
        self.pid_input.setMinimumWidth(200)
        self.addr_input.setMinimumWidth(200)
        self.len_input.setMinimumWidth(200)

        self.pid_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.addr_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.len_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.pid_input.setPlaceholderText("Process ID")
        self.addr_input.setPlaceholderText("Address")
        self.len_input.setPlaceholderText("Length to clear")

        form_layout.addRow("PID:", self.pid_input)
        form_layout.addRow("Address:", self.addr_input)
        form_layout.addRow("Length:", self.len_input)

        form_group.setLayout(form_layout)
        form_group.setMinimumWidth(300)
        self.frame_layout.addWidget(form_group)

        # usun przycisk
        self.remove_btn = QPushButton("Włącz OPSEC")
        self.remove_btn.clicked.connect(self.remove_string)
        self.frame_layout.addWidget(self.remove_btn)

        # przycisk powiadomienia
        self.notify_btn = QPushButton("Wyłącz OPSEC")
        self.notify_btn.clicked.connect(self.show_notification)
        self.frame_layout.addWidget(self.notify_btn)

        # podpis
        author_label = QLabel("Author: gram_fentanylu")
        author_label.setAlignment(Qt.AlignCenter)
        author_label.setStyleSheet("font-size: 11pt;")
        self.frame_layout.addWidget(author_label)

        self.outer_layout.addWidget(self.frame)

    def apply_style(self):
        self.setStyleSheet(get_stylesheet(self.dark_mode))

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_style()

    def remove_string(self):
        try:
            pid = int(self.pid_input.text(), 0)
            address = int(self.addr_input.text(), 0)
            length = int(self.len_input.text(), 0)
            pm = pymem.Pymem()
            pm.open_process_from_id(pid)
            pm.write_bytes(address, b'\x00' * length, length)
            QMessageBox.information(self, "OPSEC", "Zero dowodów!")  # poprawne usuniecie
        except Exception as e:
            QMessageBox.critical(self, "Zjeb", f"Dodaj info i mocny bajpas:\n{e}")  # pierwszy nie usuwa stringa

    def show_notification(self):
        QMessageBox.information(self, "hujowy bajpas", "Proxy z żywca!")  # dolny przycisk

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpsecGod()
    window.show()
    sys.exit(app.exec_())
