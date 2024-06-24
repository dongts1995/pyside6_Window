#Version 1: Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens
def button_clicked(data):
    print("You click the button, didn't you! ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) # setCheckable giá trị check sẽ thay đổi từ F -> T và ngược lại
# Makes the button checkable. It;s unchecked by default. Further clicks toggle between checked and cunchecked states


# click is a signal f QPushutton. Its emmited when you click on the button. You can wire a slot to the signal using the syntax bellow:
button.clicked.connect(button_clicked)

button.show()
app.exec()