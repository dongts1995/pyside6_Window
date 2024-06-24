from PySide6.QtWidgets import QApplication
from UsingQWidget_RockWidget import RockWidget
import sys

app = QApplication(sys.argv)

widget = RockWidget()
widget.show()

app.exec()