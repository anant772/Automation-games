import sys
import subprocess
from PyQt5 import QtWidgets, QtGui, QtCore

# Function to run your scripts
def run_script(script_name):
    subprocess.run(["python", f"{script_name}.py"])

class ScriptRunner(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        transparent_color = "black"
        self.setStyleSheet(f"background-color: {transparent_color};")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(7)
        self.setLayout(self.layout)

        # Define the scripts with their corresponding image paths
        self.scripts = [
            ("timer", "images/timer.png"),
            ("sailing", "images/sailing.png"),
            ("summoning", "images/summoning.png"),
            ("gaming", "images/gaming.png"),
            ("gardening", "images/gardening.png"),
            ("candy", "images/candy.png"),
            ("dungeon", "images/dungeon.png"),
            ("Bubo", "images/Bubo.png")
        ]

        # Desired icon size and button styling parameters
        icon_size = 25
        padding = 2
        border_radius = icon_size // 2

        # Load and create buttons for each script
        for script, path in self.scripts:
            button = QtWidgets.QPushButton()
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button.setToolTip(script)

            # Load icon image and resize it to the new size
            pixmap = QtGui.QPixmap(path).scaled(icon_size, icon_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            icon = QtGui.QIcon(pixmap)
            button.setIcon(icon)
            button.setIconSize(QtCore.QSize(icon_size, icon_size))
            button.setFixedSize(icon_size + (padding * 4), icon_size + (padding * 4))
            button.clicked.connect(lambda checked, s=script: run_script(s))
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: white;
                    border: none;
                    padding: {padding}px;
                    border-radius: {border_radius}px; /* Rounded corners */
                }}
                QPushButton:hover {{
                    background-color: blue;
                }}
                QPushButton:pressed {{
                    background-color: green;
                }}
            """)

            self.layout.addWidget(button)

        # Create a custom close button
        close_button = QtWidgets.QPushButton()
        close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        close_button.setToolTip("Close")


        # Load the close icon and resize it to the new size
        close_pixmap = QtGui.QPixmap("images/close.png").scaled(icon_size, icon_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        close_icon = QtGui.QIcon(close_pixmap)
        close_button.setIcon(close_icon)
        close_button.setIconSize(QtCore.QSize(icon_size, icon_size))
        close_button.clicked.connect(self.close)
        close_button.setFixedSize(icon_size + (padding * 4), icon_size + (padding * 4))

        # Set style for the close button with rounded corners
        close_button.setStyleSheet(f"""
            QPushButton {{
                background-color: white;
                border: none;
                padding: {padding}px;
                border-radius: {border_radius}px; /* Rounded corners */
            }}
            QPushButton:hover {{
                background-color: blue;
            }}
            QPushButton:pressed {{
                background-color: green;
            }}
        """)
        self.layout.addWidget(close_button)
        self.resize(50, 400)
        self.position_window()

    def position_window(self):
        # Get the available screen geometry
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        window_width = self.width()
        window_height = self.height()

        x = screen.right() - window_width
        y = (screen.height() - window_height) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ScriptRunner()
    window.show()
    sys.exit(app.exec_())
