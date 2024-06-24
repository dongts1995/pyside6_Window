#Version 2: Setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customixe your application's main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press me!")
        # set our button as the centraal widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()