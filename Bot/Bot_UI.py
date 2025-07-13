import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QTextEdit, QVBoxLayout, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon
from PyQt5.QtCore import Qt

class BotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.current_base = "Main Base"
        self.setWindowTitle("Clash of Clans Bot")
        self.setWindowIcon(QIcon("clash_icon.jpg"))
        QApplication.setWindowIcon(QIcon("clash_icon.jpg"))
        self.setGeometry(600, 300, 600, 400)
        self.setFixedSize(600, 400)
        self.init_ui()

    def init_ui(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))  # VS Code background
        palette.setColor(QPalette.WindowText, QColor("#F9D923"))
        palette.setColor(QPalette.Base, QColor("#1e1e1e"))
        palette.setColor(QPalette.Text, QColor("#FFFFFF"))
        palette.setColor(QPalette.Button, QColor("#1e1e1e"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        self.setPalette(palette)

        serious_font = QFont("Segoe UI", 10)
        self.setFont(serious_font)

        self.main_layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Clash of Clans Bot")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title_label.setStyleSheet("color: #F9D923")
        title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title_label)

        # Change Base Button
        base_layout = QHBoxLayout()
        base_layout.addStretch(1)
        self.base_button = QPushButton(self.current_base)
        self.base_button.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px; border: 2px solid white; border-radius: 15px; padding: 10px 20px;")
        self.base_button.clicked.connect(self.toggle_base)
        base_layout.addWidget(self.base_button)
        base_layout.addStretch(1)
        self.main_layout.addLayout(base_layout)

        # Builder Buttons
        self.builder_buttons_layout = QHBoxLayout()
        self.elixir_button = QPushButton("Collect Elixir")
        self.coins_button = QPushButton("Collect Coins")
        for btn in [self.elixir_button, self.coins_button]:
            btn.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px; border: 2px solid white; border-radius: 15px; padding: 10px 20px;")
        self.builder_buttons_layout.addWidget(self.elixir_button)
        self.builder_buttons_layout.addWidget(self.coins_button)
        self.main_layout.addLayout(self.builder_buttons_layout)
        self.builder_buttons_layout.setSpacing(10)
        self.builder_buttons_layout.setContentsMargins(20, 0, 20, 0)
        self.toggle_builder_buttons(False)

        # Status
        self.status = QLabel(f"Status: {self.current_base} Selected")
        self.status.setFont(QFont("Segoe UI", 14))
        self.status.setStyleSheet("color: #F9D923")
        self.status.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.status)

        # Log Output
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.main_layout.addWidget(self.log)

        # Start/Stop Buttons
        bottom_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Bot")
        self.stop_btn = QPushButton("Stop Bot")
        for btn in [self.start_btn, self.stop_btn]:
            btn.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px; border: 2px solid white; border-radius: 15px; padding: 10px 20px;")
        self.stop_btn.setEnabled(False)
        bottom_layout.addWidget(self.start_btn)
        bottom_layout.addWidget(self.stop_btn)
        self.main_layout.addLayout(bottom_layout)

        self.setLayout(self.main_layout)

    def toggle_base(self):
        is_builder = self.current_base == "Main Base"
        self.current_base = "Builder Base" if is_builder else "Main Base"
        self.setWindowTitle("Clash of Clans Bot")
        self.status.setText(f"Status: {self.current_base} Selected")
        self.base_button.setText(self.current_base)
        self.toggle_builder_buttons(self.current_base == "Builder Base")

    def toggle_builder_buttons(self, show):
        for i in range(self.builder_buttons_layout.count()):
            widget = self.builder_buttons_layout.itemAt(i).widget()
            if widget:
                widget.setVisible(show)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("clash_icon.jpg"))
    gui = BotGUI()
    gui.show()
    sys.exit(app.exec_())