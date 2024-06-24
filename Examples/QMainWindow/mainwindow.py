from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QTextEdit
from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtGui import QTextCursor, QFont
from lib_menubar import MenuBar
from lib_toolbar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("SOME/IP communication simulation tool")
        self.setGeometry(100, 100, 800, 600)  # Init size

        # Menu Bar
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Create the group boxes
        group1 = QGroupBox("Message :")
        group2 = QGroupBox("SOME/IP Traces :")
        group3 = QGroupBox("Request : ")
        group4 = QGroupBox("Topic : ")

        # Add some content to the group boxes
        group1.setLayout(QVBoxLayout())
        # Create QTextEdit for logging messages
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)  # Make it read-only
        group1.layout().addWidget(self.log_text_edit)

        group2.setLayout(QVBoxLayout())
        # Add a table to Group 2
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)  # Example row count
        self.table_widget.setColumnCount(9)  # 5 columns
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])

        # Allow columns to be resized
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        
        # Populate the table with some example data
        for row in range(0):
            for col in range(9):
                item = QTableWidgetItem(f"Item {row},{col}")
                self.table_widget.setItem(row, col, item)
        
        group2.layout().addWidget(self.table_widget)

        group3.setLayout(QVBoxLayout())

        group4.setLayout(QVBoxLayout())

        # Create buttons for group 4
        clear_button_4 = QPushButton("Clear")
        send_button_4 = QPushButton("Send")

        # Create layout for buttons in group 4
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(clear_button_4)
        buttons_layout.addWidget(send_button_4)
        # group4.layout().addLayout(buttons_layout)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the main vertical layout
        main_layout = QVBoxLayout(central_widget)

        # Create the horizontal layout for group 2 and group 3, group 4
        upper_layout = QHBoxLayout()
        
        # Create the vertical layout for the left part (group 3, group 4)
        left_layout = QVBoxLayout()
        left_layout.addWidget(group3, 2)
        left_layout.addWidget(group4, 2)
        left_layout.addLayout(buttons_layout, 1)

        upper_layout.addLayout(left_layout, 3)
        upper_layout.addWidget(group2, 2)

        # Add left and right layouts to the main layout
        main_layout.addLayout(upper_layout, 3)
        
        # Add group1 to the bottom of the window
        main_layout.addWidget(group1, 1)

        # Setup timer to add a row every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_table_row)
        # self.timer.start(1000)  # 1000 milliseconds = 1 second

        self.current_row = 0

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # 1000 milliseconds = 1 second

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()

    def add_table_row(self):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        for col in range(9):
            item = QTableWidgetItem(f"Item {self.current_row},{col}")
            self.table_widget.setItem(row_position, col, item)
            item.setFont(QFont("Courier")) 
        self.current_row += 1
        self.table_widget.scrollToBottom()

        message = "Log message {self.log_counter}\n"
        self.log_text_edit.append(message)  # Append message to QTextEdit
        self.log_text_edit.moveCursor(QTextCursor.End)

    def toolbar_button_click(self):
        self.statusBar().showMessage("Some message ...", 3000)

    def quit(self):
        self.app.quit()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec()
