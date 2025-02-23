import sys, subprocess
from PyQt5 import QtWidgets, QtGui, QtCore

def run_script(script_name):
    subprocess.run(["python", f"{script_name}.py"])

def create_icon_button(icon_path, size, tooltip, callback):
    btn = QtWidgets.QPushButton()
    btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    btn.setToolTip(tooltip)
    pixmap = QtGui.QPixmap(icon_path).scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    btn.setIcon(QtGui.QIcon(pixmap))
    btn.setIconSize(QtCore.QSize(size, size))
    diameter = size + 10  # Reduced padding
    btn.setFixedSize(diameter, diameter)
    
    # Simplified button styling
    btn.setStyleSheet(f"""
        QPushButton {{
            background-color: #2F80FF;
            border: 1px solid #FFFFFF;
            border-radius: {diameter//2}px;
            padding: 2px;
        }}
        QPushButton:hover {{
            background-color: #4A9CFF;
        }}
        QPushButton:pressed {{
            background-color: #1A5BB5;
        }}
    """)
    
    # Reduced shadow effect
    shadow = QtWidgets.QGraphicsDropShadowEffect()
    shadow.setBlurRadius(8)
    shadow.setColor(QtGui.QColor(0, 0, 0, 100))
    shadow.setOffset(2, 2)
    btn.setGraphicsEffect(shadow)
    
    btn.clicked.connect(callback)
    return btn, diameter

class ScriptRunner(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.menuExpanded = False
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Main widget styling
        self.setStyleSheet("""
            background: rgba(45, 45, 45, 0.9);
            border-radius: 15px;
        """)
        
        # Window shadow effect
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)

        self.menuButton, btn_size = create_icon_button("images/menu.png", 24, "Menu", self.toggleMenu)
        self.mainLayout.addWidget(self.menuButton, alignment=QtCore.Qt.AlignHCenter)

        self.menuContainer = QtWidgets.QWidget()
        self.menuContainer.setMaximumHeight(0)
        self.menuContainer.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.menuContainerLayout = QtWidgets.QVBoxLayout(self.menuContainer)
        self.menuContainerLayout.setContentsMargins(0, 8, 0, 8)
        self.menuContainerLayout.setSpacing(10)
        self.mainLayout.addWidget(self.menuContainer)

        # Subtle background for menu container
        self.menuContainer.setStyleSheet("""
            background: rgba(60, 60, 60, 0.9);
            border-radius: 10px;
        """)

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

        self.scriptButtons = []
        for script, path in self.scripts:
            btn, btn_diameter = create_icon_button(
                path, 24, script.title(), lambda checked, s=script: run_script(s)
            )
            self.menuContainerLayout.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)
            self.scriptButtons.append(btn)

        close_btn, btn_diameter = create_icon_button("images/close.png", 24, "Close", self.close)
        close_btn.setStyleSheet("background-color: #FF4B4B;")
        self.menuContainerLayout.addWidget(close_btn, alignment=QtCore.Qt.AlignHCenter)
        self.scriptButtons.append(close_btn)

        # Calculate expanded height based on new button sizes
        spacing = self.menuContainerLayout.spacing()
        num_buttons = len(self.scriptButtons)
        self.expandedHeight = (btn_diameter * num_buttons) + (spacing * (num_buttons - 1)) + 16
        self.resize(60, 400)
        self.position_window()
        
        # Improved animation setup
        self.anim = QtCore.QPropertyAnimation(self.menuContainer, b"maximumHeight")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QtCore.QEasingCurve.OutCubic)

    def toggleMenu(self):
        if self.anim.state() == QtCore.QAbstractAnimation.Running:
            self.anim.stop()
            
        start = self.menuContainer.maximumHeight()
        end = self.expandedHeight if start == 0 else 0
        self.anim.setStartValue(start)
        self.anim.setEndValue(end)
        self.anim.start()
        self.menuExpanded = (end != 0)

    def position_window(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        self.move(screen.right() - self.width() - 15, (screen.height() - self.height()) // 2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ScriptRunner()
    window.show()
    sys.exit(app.exec_())