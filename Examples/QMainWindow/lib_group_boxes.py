from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QLabel, QWidget, QLineEdit
from PySide6.QtGui import QFont, Qt

class MessageGroup(QGroupBox):
    def __init__(self):
        super().__init__("Message :")
        self.setLayout(QVBoxLayout())

        # Create QTextEdit for logging messages
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)  # Make it read-only
        self.log_text_edit.setFont(QFont("Courier"))
        self.layout().addWidget(self.log_text_edit)

class TracesGroup(QGroupBox):
    def __init__(self):
        super().__init__("SOME/IP Traces :")
        self.setLayout(QVBoxLayout())

        # Add a table to Group 2
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)  # Example row count
        self.table_widget.setColumnCount(9)  # 10 columns
        self.table_widget.horizontalHeader().setFont("Courier")
        self.table_widget.verticalHeader().setFont("Courier")
        self.table_widget.setHorizontalHeaderLabels(['Time', 'Source IP', 'Destination IP', 'Payload Length', 'Payload Data', 'Packet Length', 'Message Type', 'Source Port', 'Destination Port'])

        # Allow columns to be resized
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)

        # Set fixed row height to ensure only one line of text per row
        font_metrics = self.table_widget.fontMetrics()
        row_height = font_metrics.height() + 1  # Adjust as needed for padding
        self.table_widget.verticalHeader().setDefaultSectionSize(row_height)
        self.table_widget.setShowGrid(False)
        
        self.layout().addWidget(self.table_widget)

class RequestGroup(QGroupBox):
    def __init__(self):
        super().__init__("Request : ")
        self.setLayout(QVBoxLayout())

        # Create buttons for Signal 1
        label1 = QLabel("Request ID 1")
        label1.setAlignment(Qt.AlignCenter)
        lineEdit1 = QLineEdit()
        send_button1 = QPushButton("Send")
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(label1,1)
        button_layout1.addWidget(lineEdit1,2)
        button_layout1.addWidget(send_button1)

        # Create buttons for Signal 2
        label2 = QLabel("Request ID 2")
        label2.setAlignment(Qt.AlignCenter)
        lineEdit2 = QLineEdit()
        send_button2 = QPushButton("Send")
        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(label2,1)
        button_layout2.addWidget(lineEdit2,2)
        button_layout2.addWidget(send_button2)

        # Create buttons for Signal 3
        label3 = QLabel("Request ID 3")
        label3.setAlignment(Qt.AlignCenter)
        lineEdit3 = QLineEdit()
        send_button3 = QPushButton("Send")
        button_layout3 = QHBoxLayout()
        button_layout3.addWidget(label3,1)
        button_layout3.addWidget(lineEdit3,2)
        button_layout3.addWidget(send_button3)

        # Create buttons for Signal 4
        label4 = QLabel("Request ID 4")
        label4.setAlignment(Qt.AlignCenter)
        lineEdit4 = QLineEdit()
        send_button4 = QPushButton("Send")
        button_layout4 = QHBoxLayout()
        button_layout4.addWidget(label4,1)
        button_layout4.addWidget(lineEdit4,2)
        button_layout4.addWidget(send_button4)

        # Create buttons for Signal 5
        label5 = QLabel("Request ID 5")
        label5.setAlignment(Qt.AlignCenter)
        lineEdit5 = QLineEdit()
        send_button5 = QPushButton("Send")
        button_layout5 = QHBoxLayout()
        button_layout5.addWidget(label5,1)
        button_layout5.addWidget(lineEdit5,2)
        button_layout5.addWidget(send_button5)

        button_layouts = QVBoxLayout()
        button_layouts.addLayout(button_layout1)
        button_layouts.addLayout(button_layout2)
        button_layouts.addLayout(button_layout3)
        button_layouts.addLayout(button_layout4)
        button_layouts.addLayout(button_layout5)

        self.layout().addLayout(button_layouts)


class TopicGroup(QGroupBox):
    def __init__(self):
        super().__init__("Topic : ")
        self.setLayout(QVBoxLayout())

        # Create buttons for Signal 1
        label1 = QLabel("Signal 1 value")
        label1.setAlignment(Qt.AlignCenter)
        lineEdit1 = QLineEdit()
        send_button1 = QPushButton("Send")
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(label1,1)
        button_layout1.addWidget(lineEdit1,2)
        button_layout1.addWidget(send_button1)

        # Create buttons for Signal 2
        label2 = QLabel("Signal 2 value")
        label2.setAlignment(Qt.AlignCenter)
        lineEdit2 = QLineEdit()
        send_button2 = QPushButton("Send")
        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(label2,1)
        button_layout2.addWidget(lineEdit2,2)
        button_layout2.addWidget(send_button2)

        # Create buttons for Signal 3
        label3 = QLabel("Signal 3 value")
        label3.setAlignment(Qt.AlignCenter)
        lineEdit3 = QLineEdit()
        send_button3 = QPushButton("Send")
        button_layout3 = QHBoxLayout()
        button_layout3.addWidget(label3,1)
        button_layout3.addWidget(lineEdit3,2)
        button_layout3.addWidget(send_button3)

        # Create buttons for Signal 4
        label4 = QLabel("Signal 4 value")
        label4.setAlignment(Qt.AlignCenter)
        lineEdit4 = QLineEdit()
        send_button4 = QPushButton("Send")
        button_layout4 = QHBoxLayout()
        button_layout4.addWidget(label4,1)
        button_layout4.addWidget(lineEdit4,2)
        button_layout4.addWidget(send_button4)

        # Create buttons for Signal 5
        label5 = QLabel("Signal 5 value")
        label5.setAlignment(Qt.AlignCenter)
        lineEdit5 = QLineEdit()
        send_button5 = QPushButton("Send")
        button_layout5 = QHBoxLayout()
        button_layout5.addWidget(label5,1)
        button_layout5.addWidget(lineEdit5,2)
        button_layout5.addWidget(send_button5)

        button_layouts = QVBoxLayout()
        button_layouts.addLayout(button_layout1)
        button_layouts.addLayout(button_layout2)
        button_layouts.addLayout(button_layout3)
        button_layouts.addLayout(button_layout4)
        button_layouts.addLayout(button_layout5)

        self.layout().addLayout(button_layouts)
