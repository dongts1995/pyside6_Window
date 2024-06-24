from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # MenuBar
        file_menu = self.addMenu("&File")
        edit_menu = self.addMenu("&Edit")
        window_menu = self.addMenu("&Window")
        setting_menu = self.addMenu("&Setting")
        help_menu = self.addMenu("&Help")

        # Action in Flie
        save_action = QAction("Save", self)
        save_as_action = QAction("Save as ...", self)
        quit_action = QAction("Quit", self)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(quit_action)

        # Action in Edit
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # connect
        quit_action.triggered.connect(quit)

    def quit(self):
        self.app.quit()
