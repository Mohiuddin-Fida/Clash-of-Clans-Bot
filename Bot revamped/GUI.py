import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,
    QLabel, QHBoxLayout, QCheckBox, QMessageBox
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class BotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.current_base = "Main Base"
        self.hero_checkboxes = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Clash of Clans Bot")
        self.setGeometry(600, 300, 520, 310)  # reduced from 360 to 310
        self.setFixedSize(520, 310)
        self.setup_styling()
        self.create_widgets()

    def setup_styling(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.WindowText, QColor("#F9D923"))
        palette.setColor(QPalette.Base, QColor("#1e1e1e"))
        palette.setColor(QPalette.Text, QColor("#FFFFFF"))
        palette.setColor(QPalette.Button, QColor("#1e1e1e"))
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 11))

    def create_widgets(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)  # slightly tighter
        main_layout.setContentsMargins(12, 2, 12, 4)  # reduced top & bottom margins

        main_layout.addLayout(self.create_header())
        main_layout.addLayout(self.create_inputs())
        main_layout.addLayout(self.create_hero_selection())
        self.create_control_buttons(main_layout)

        self.setLayout(main_layout)

    def create_header(self):
        header_layout = QVBoxLayout()
        header_layout.setSpacing(0)

        title_label = QLabel("Clash of Clans Bot")
        title_label.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title_label.setStyleSheet("color: #F9D923; margin: 0px; padding: 0px;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label)

        header_layout.addSpacing(-20)  # pull base button closer

        self.base_button = QPushButton(self.current_base)
        self.base_button.setStyleSheet(
            "background-color: #1e1e1e; color: white; font-size: 15px; "
            "border: 2px solid white; border-radius: 15px; padding: 8px 18px;"
        )
        self.base_button.clicked.connect(self.toggle_base)

        base_layout = QHBoxLayout()
        base_layout.addStretch(1)
        base_layout.addWidget(self.base_button)
        base_layout.addStretch(1)
        header_layout.addLayout(base_layout)

        return header_layout

    def create_inputs(self):
        input_layout = QHBoxLayout()

        edrag_label = QLabel("E-Drags:")
        edrag_label.setStyleSheet("color: white; font-size: 15px;")
        input_layout.addWidget(edrag_label)

        self.edrag_input = self.create_number_input("e.g. 6", 11, "E-Drags")
        input_layout.addWidget(self.edrag_input)

        input_layout.addSpacing(20)

        bat_label = QLabel("Bat Spells:")
        bat_label.setStyleSheet("color: white; font-size: 15px;")
        input_layout.addWidget(bat_label)

        self.bat_input = self.create_number_input("e.g. 5", 11, "Bat Spells")
        input_layout.addWidget(self.bat_input)

        return input_layout

    def create_number_input(self, placeholder, max_val, label):
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedWidth(80)
        input_field.setStyleSheet(
            "color: white; background-color: #1e1e1e; font-size: 14px; padding: 6px;"
        )
        input_field.textChanged.connect(
            lambda: self.validate_input(input_field, max_val, label)
        )
        return input_field

    def create_hero_selection(self):
        hero_layout = QVBoxLayout()

        hero_label_row = QHBoxLayout()
        hero_label = QLabel("Select Heroes:")
        hero_label.setStyleSheet("color: white; font-size: 15px;")
        hero_label.setFixedWidth(120)
        hero_label_row.addWidget(hero_label)

        hero_names = [
            "Barbarian King", "Archer Queen", "Grand Warden",
            "Royal Champion", "Minion Prince"
        ]

        for hero in hero_names[:2]:
            cb = QCheckBox(hero)
            cb.setStyleSheet("color: white; font-size: 14px;")
            cb.stateChanged.connect(self.hero_checked)
            self.hero_checkboxes.append(cb)
            hero_label_row.addWidget(cb)
        hero_layout.addLayout(hero_label_row)

        hero_row2 = QHBoxLayout()
        for hero in hero_names[2:]:
            cb = QCheckBox(hero)
            cb.setStyleSheet("color: white; font-size: 14px;")
            cb.stateChanged.connect(self.hero_checked)
            self.hero_checkboxes.append(cb)
            hero_row2.addWidget(cb)
        hero_layout.addLayout(hero_row2)

        return hero_layout

    def create_control_buttons(self, main_layout):
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")

        button_style = (
            "background-color: #1e1e1e; color: white; font-size: 16px; "
            "border: 2px solid white; border-radius: 10px; padding: 10px 0;"
        )

        for btn in [self.start_btn, self.stop_btn]:
            btn.setStyleSheet(button_style)
            btn.setMinimumHeight(40)
            main_layout.addWidget(btn)

        self.stop_btn.setEnabled(False)

    def validate_input(self, input_field, max_val, label):
        text = input_field.text()
        if text and not text.isdigit():
            input_field.setText("")
        elif text and int(text) > max_val:
            input_field.setText(str(max_val))
            QMessageBox.warning(self, f"{label} Limit",
                                f"Maximum {label.lower()} allowed is {max_val}.")

    def hero_checked(self):
        if sum(cb.isChecked() for cb in self.hero_checkboxes) > 4:
            self.sender().setChecked(False)
            QMessageBox.warning(self, "Hero Limit", "You can only select 4 heroes.")

    def toggle_base(self):
        self.current_base = "Builder Base" if self.current_base == "Main Base" else "Main Base"
        self.base_button.setText(self.current_base)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BotGUI()
    gui.show()
    sys.exit(app.exec_())
