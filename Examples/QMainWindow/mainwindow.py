from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar, QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QTextEdit, QSplitter
from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtGui import QAction, QIcon, QFont, QTextCursor, QColor
from lib_menubar import MenuBar
from lib_toolbar import ToolBar
from lib_group_boxes import MessageGroup, TracesGroup, RequestGroup, TopicGroup
import random

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("SOME/IP communication simulation tool")
        self.setGeometry(100, 100, 800, 600)  # Init size

        # 1. Menu Bar
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # 2. Toolbar
        self.tool_bar = ToolBar(self)
        self.tool_bar.setIconSize(QSize(16,16))
        self.addToolBar(self.tool_bar)

        # 3. StatusBar 
        self.setStatusBar(QStatusBar(self))

        # 4. Body
        self.request_group = RequestGroup()
        self.topic_group = TopicGroup()
        self.traces_group = TracesGroup()
        self.message_group = MessageGroup()
        # Create buttons Clear and Send
        buttons_layout = QHBoxLayout()
        clear_button = QPushButton("Clear All")
        send_button = QPushButton("Send All")
        buttons_layout.addWidget(clear_button)
        buttons_layout.addWidget(send_button)

        # 5. Layout for central_widget
        # Create the vertical layout for the left part (group 3, group 4)
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.request_group, 2)
        left_layout.addWidget(self.topic_group, 2)
        left_layout.addLayout(buttons_layout, 1)
        # Create the horizontal layout for group 2 and group 3, group 4
        upper_layout = QHBoxLayout()
        upper_layout.addLayout(left_layout, 3)
        upper_layout.addWidget(self.traces_group, 2)
        # Create the main vertical layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.addLayout(upper_layout, 3)
        main_layout.addWidget(self.message_group, 1)

        # 6. Setup timer to add a row every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_out)

        # 99. Variable
        self.current_row = 0
        self.random_number = random.randint(-100, 100)

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # 1000 milliseconds = 1 second

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()

    def time_out(self):
        row_position = self.traces_group.table_widget.rowCount()
        self.traces_group.table_widget.insertRow(row_position)
        self.traces_group.table_widget.setColumnWidth(0, 60)
        self.traces_group.table_widget.setColumnWidth(1, 60)
        self.traces_group.table_widget.setColumnWidth(2, 60)
        self.traces_group.table_widget.setColumnWidth(3, 200)
        self.traces_group.table_widget.setColumnWidth(4, 60)
        self.traces_group.table_widget.setColumnWidth(5, 60)
        self.traces_group.table_widget.setColumnWidth(6, 60)
        self.traces_group.table_widget.setColumnWidth(7, 60)
        self.traces_group.table_widget.setColumnWidth(8, 60)
        self.traces_group.table_widget.setColumnWidth(9, 60)
        for col in range(9):
            item = QTableWidgetItem(f"Item {self.current_row},{col}")
            if(col == 0):
                self.random_number = random.randint(-100, 100)
                val = self.current_row*1000 + self.random_number
                if(val<0):
                    val = -val
                item = QTableWidgetItem(f"{val}")
            if(col == 1):
                item = QTableWidgetItem("160.48.199.98")
            if(col == 2):
                item = QTableWidgetItem("239.255.42.99")
            if(col == 3):
                item = QTableWidgetItem("00 A1 FF 09 99 11 00 00 00 00 C0 00 FF FF FF FF")
            self.traces_group.table_widget.setItem(row_position, col, item)
            item.setFont(QFont("Courier")) 
            item.setForeground(QColor(72, 118, 255))  # Light blue color
            # self.traces_group.table_widget.setItem(row_position, col, item)
        self.current_row += 1
        self.traces_group.table_widget.scrollToBottom()

        message = f"Sending message {self.current_row} ...\n"
        self.message_group.log_text_edit.append(message)  # Append message to QTextEdit
        self.message_group.log_text_edit.moveCursor(QTextCursor.End)

    def quit(self):
        self.app.quit()