# opsecdix.py
# Centralized styles for light and dark themes to ensure consistent button sizes and UI appearance

light_theme_stylesheet = """
QWidget {
    background-color: #f4f4f4;
    color: #000;
    font-family: Segoe UI;
    font-size: 10pt;
}
QLabel#TitleLabel {
    color: black;
    background: transparent;
}
QLineEdit {
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
}
QPushButton {
    background-color: #007acc;
    color: white;
    border-radius: 6px;
    padding: 6px 12px;
    min-width: 80px;
    min-height: 28px;
}
QPushButton:hover {
    background-color: #005fa3;
}
QFrame#MainFrame {
    border: 2px solid #ccc;
    border-radius: 10px;
    background-color: #ffffff;
}
"""

dark_theme_stylesheet = """
QWidget {
    background-color: #222;
    color: white;
    font-family: Segoe UI;
    font-size: 10pt;
}
QLabel#TitleLabel {
    color: white;
    background: transparent;
}
QLineEdit {
    padding: 6px 12px;
    background-color: #333;
    color: white;
    border: 1px solid #555;
    border-radius: 6px;
}
QPushButton {
    background-color: #008cba;
    color: white;
    border-radius: 6px;
    padding: 6px 12px;
    min-width: 80px;
    min-height: 28px;
}
QPushButton:hover {
    background-color: #007199;
}
QFrame#MainFrame {
    border: 2px solid #444;
    border-radius: 10px;
    background-color: #2b2b2b;
}
"""

def get_stylesheet(dark_mode: bool) -> str:
    return dark_theme_stylesheet if dark_mode else light_theme_stylesheet
