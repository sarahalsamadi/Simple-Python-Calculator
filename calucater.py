import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # إعداد النافذة
        self.setWindowTitle("آلة حاسبة")
        self.setGeometry(100, 100, 300, 400)

        # واجهة المستخدم
        self.init_ui()

    def init_ui(self):
        # الحاوية الرئيسية
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # التخطيط العام
        layout = QVBoxLayout()

        # شاشة الإدخال
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setPlaceholderText("0")
        layout.addWidget(self.display)

        # الشبكة للأزرار
        grid_layout = QGridLayout()

        # تعريف الأزرار
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4),
        ]

        # إضافة الأزرار إلى الشبكة
        for btn_text, row, col, *span in buttons:
            button = QPushButton(btn_text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            if span:
                grid_layout.addWidget(button, row, col, *span)
            else:
                grid_layout.addWidget(button, row, col)

            # ربط الأزرار بالدالة المناسبة
            button.clicked.connect(self.on_button_click)

        layout.addLayout(grid_layout)
        main_widget.setLayout(layout)

    def on_button_click(self):
        # الحصول على النص من الزر
        button = self.sender()
        text = button.text()

        if text == "C":
            # مسح الشاشة
            self.display.clear()
        elif text == "=":
            # تنفيذ العملية الحسابية
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            # إضافة النص إلى الشاشة
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
