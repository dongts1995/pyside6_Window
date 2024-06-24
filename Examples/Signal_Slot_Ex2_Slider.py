from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# The slot : respinds when something happens
def respond_to_slider(data): 
    print("Slide moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# connect slider
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()