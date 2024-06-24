import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMenuBar
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SOME/IP communication simulation tool")
        self.setGeometry(100, 100, 800, 600)  # Đặt kích thước ban đầu

        # Tạo menu bar
        menu_bar = self.menuBar()
        
        # Tạo menu File
        file_menu = menu_bar.addMenu("File")
        
        # Thêm hành động vào menu File
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Tạo widget trung tâm và layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Tạo nhãn và nút bấm
        self.label = QLabel("Hello, PySide6!")
        self.button = QPushButton("Click me")

        # Thêm nhãn và nút bấm vào layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Kết nối nút bấm với phương thức xử lý
        self.button.clicked.connect(self.change_label_text)

    def open_file(self):
        # Thêm logic để mở tệp tại đây
        self.label.setText("Open file action triggered")

    def change_label_text(self):
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Mở cửa sổ chính ở chế độ toàn màn hình
    sys.exit(app.exec())
