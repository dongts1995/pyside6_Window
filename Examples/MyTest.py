from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QToolBar, QStatusBar, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGroupBox
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GroupBox Layout Example")

        # Create the group boxes
        group1 = QGroupBox("Group 1")
        group2 = QGroupBox("Group 2")
        group3 = QGroupBox("Group 3")
        group4 = QGroupBox("Group 4")

        # Add some content to the group boxes
        group1.setLayout(QVBoxLayout())
        group1.layout().addWidget(QLabel("Content of Group 1"))

        group2.setLayout(QVBoxLayout())
        group2.layout().addWidget(QLabel("Content of Group 2"))

        group3.setLayout(QVBoxLayout())
        group3.layout().addWidget(QLabel("Content of Group 3"))

        group4.setLayout(QVBoxLayout())
        group4.layout().addWidget(QLabel("Content of Group 4"))

        # Create actions for the menu and toolbar
        exit_action = self.create_action("&Exit", self.close)

        # Create the menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit_action)

        # Create the tool bar
        tool_bar = self.addToolBar("Tool Bar")
        tool_bar.addAction(exit_action)

        # Create the status bar
        self.statusBar().showMessage("Ready", 3000)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the main vertical layout
        main_layout = QVBoxLayout(central_widget)

        # Create the horizontal layout for group 2 and group 3, group 4
        upper_layout = QHBoxLayout()
        

        # Create the vertical layout for the left part (group 3, group 4)
        left_layout = QVBoxLayout()
        left_layout.addWidget(group3, 1)
        left_layout.addWidget(group4, 1)

        upper_layout.addLayout(left_layout, 3)
        upper_layout.addWidget(group2, 2)

        # Add left and right layouts to the main layout
        main_layout.addLayout(upper_layout, 3)
        

        # Add group1 to the bottom of the window
        main_layout.addWidget(group1, 1)

    def create_action(self, text, slot=None, shortcut=None, icon=None, tip=None):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        return action

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    app.exec()
