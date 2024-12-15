import sys
import random
import time
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox
)

class OfflineModeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dimin zakaz")
        self.setGeometry(200, 200, 400, 300)

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Checkbox for offline mode
        self.checkbox = QCheckBox("Включить автономный режим")
        self.checkbox.stateChanged.connect(self.toggle_offline_mode)
        layout.addWidget(self.checkbox, alignment=Qt.AlignCenter)

        # Label for displaying random number
        self.result_label = QLabel("\n")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 24px; color: green;")
        layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

        # Button for generating number (hidden initially)
        self.generate_button = QPushButton("Заработать")
        self.generate_button.setVisible(False)
        self.generate_button.clicked.connect(self.generate_random_number)
        layout.addWidget(self.generate_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def toggle_offline_mode(self, state):
        if state == Qt.Checked:
            self.generate_button.setVisible(True)
            self.result_label.setText("Нажмите 'Заработать'")
        else:
            self.generate_button.setVisible(False)
            self.result_label.setText("\n")

    def generate_random_number(self):
        self.result_label.setText("Сумма за сегодня...")
        self.result_label.repaint()

        # Timer for animating number generation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate_number_selection)
        self.animation_steps = 0
        self.timer.start(50)

    def animate_number_selection(self):
        self.animation_steps += 1
        random_value = random.randint(1000, 9999)
        self.result_label.setText(f"{random_value} рублей")
        self.result_label.repaint()

        # Stop animation after 20 steps
        if self.animation_steps > 20:
            self.timer.stop()
            final_value = random.randint(1000, 9999)
            self.result_label.setText(f"Итоговая сумма: {final_value} рублей")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OfflineModeApp()
    window.show()
    sys.exit(app.exec_())