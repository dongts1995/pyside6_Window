from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction, QIcon

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Tool Bar", parent)
        
        # Add Start action
        self.start_action = QAction(QIcon("start.png"), "Start", self)
        self.start_action.setStatusTip("START")
        self.start_action.setCheckable(True)
        self.start_action.triggered.connect(self.parent().start_timer)
        self.addAction(self.start_action)

        # Add Stop action
        self.stop_action = QAction(QIcon("stop.png"), "Stop", self)
        self.stop_action.setStatusTip("STOP")
        self.stop_action.setCheckable(True)
        self.stop_action.triggered.connect(self.parent().stop_timer)
        self.addAction(self.stop_action)

        # Connect actions to slots
        self.start_action.triggered.connect(self.start_triggered)
        self.stop_action.triggered.connect(self.stop_triggered)

    def start_triggered(self):
        if self.start_action.isChecked():
            self.stop_action.setChecked(False)
            print("Start triggered")

    def stop_triggered(self):
        if self.stop_action.isChecked():
            self.start_action.setChecked(False)
            print("Stop triggered")
