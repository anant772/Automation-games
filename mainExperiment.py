import sys, subprocess
from PyQt5 import QtWidgets, QtGui, QtCore
import csv

def run_script(script_name):
    subprocess.run(["python", f"{script_name}.py"])

def create_icon_button(icon_path, size, tooltip, callback):
    btn = QtWidgets.QPushButton()
    btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn.setToolTip(tooltip)
    pixmap = QtGui.QPixmap(icon_path).scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    btn.setIcon(QtGui.QIcon(pixmap))
    btn.setIconSize(QtCore.QSize(size, size))
    diameter = size + 4
    btn.setFixedSize(diameter + 3, diameter + 3)
    btn.setStyleSheet(f"""
        QPushButton {{background-color: white; border: none; padding: 2px; border-radius: {diameter//2}px;}}
        QPushButton:hover {{background-color: blue;}}
        QPushButton:pressed {{background-color: green;}}
    """)
    btn.clicked.connect(callback)
    return btn, diameter


def load_scripts_from_file(self, filepath):
    try:
        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 2:  # Ensure there are at least 2 columns
                    name = row[0].strip()
                    path = row[1].strip()
                    self.scripts.append((name, path))
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. No scripts loaded.")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")


class ScriptRunner(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.menuExpanded = False
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainLayout.setSpacing(5)

        self.menuButton, btn_size = create_icon_button("images/menu.png", 25, "Menu", self.toggleMenu)
        self.mainLayout.addWidget(self.menuButton, alignment=QtCore.Qt.AlignHCenter)

        self.menuContainer = QtWidgets.QWidget()
        self.menuContainer.setMaximumHeight(0)
        self.menuContainer.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.menuContainerLayout = QtWidgets.QVBoxLayout(self.menuContainer)
        self.menuContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.menuContainerLayout.setSpacing(10)
        self.mainLayout.addWidget(self.menuContainer)

        self.scripts = []
        load_scripts_from_file(self, "scripts.txt")

        self.scriptButtons = []
        for script, path in self.scripts:
            btn, btn_diameter = create_icon_button(
                path, 25, script, lambda checked, s=script: run_script(s)
            )
            self.menuContainerLayout.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)
            self.scriptButtons.append(btn)

        close_btn, btn_diameter = create_icon_button("images/close.png", 25, "Close", self.close)
        self.menuContainerLayout.addWidget(close_btn, alignment=QtCore.Qt.AlignHCenter)
        self.scriptButtons.append(close_btn)

        spacing = self.menuContainerLayout.spacing()
        num_buttons = len(self.scriptButtons)
        self.expandedHeight = (btn_diameter * num_buttons) + (spacing * (num_buttons - 1))
        self.resize(60, 400)
        self.position_window()
        self.anim = QtCore.QPropertyAnimation(self.menuContainer, b"maximumHeight")
        self.anim.setDuration(300)

    def toggleMenu(self):
        start, end = (self.expandedHeight, 0) if self.menuExpanded else (0, self.expandedHeight)
        self.anim.setStartValue(start)
        self.anim.setEndValue(end)
        self.anim.start()
        self.menuExpanded = not self.menuExpanded

    def position_window(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        self.move(screen.right() - self.width(), (screen.height() - self.height()) // 2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ScriptRunner()
    window.show()
    sys.exit(app.exec_())
    
