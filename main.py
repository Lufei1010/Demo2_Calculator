# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont


class CalcApp(QWidget):
# Add Settings
    def __init__(self):
        super().__init__()  # Call the __init__ method of the superclass (QWidget) to initialize the base window
        self.setWindowTitle("Calculator")
        self.resize(250, 300)

    # All objects
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.text_box.setStyleSheet("QLineEdit { color: black; }")

        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
        ]
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)  # Connect the button to the event handler method
            button.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; color: black; padding: 10px}") #similar to CSS
            self.grid.addWidget(button, row, col) # Add the button to the grid at the current row and column
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; color: black; padding: 10px}")
        self.delete.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; color: black; padding: 10px}")
        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

#function  # Define the event handler for button clicks
    def button_click(self):
        button = app.sender() # Retrieves the button that triggered the event.
        text = button.text()

        if text == "=":
            symbol = self.text_box.text() #gets the current text from the QLineEdit widget. If the user has typed 3+5, symbol will contain the string "3+5".
            try:
                res = eval(symbol)  # eval() in the button_click() function allows evaluate the mathematical expression
                self.text_box.setText(str(res))  # widget expects a string as its input.
            except Exception as e:
                print("Error", e)

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

if __name__ == "__main__":
    app = QApplication([]) # Create a PyQt5 application
    main_window = CalcApp() # Create an instance of the CalcApp class
    main_window.setStyleSheet("QWidget { background-color: #f0f0f8 } ")
    main_window.show()
    app.exec_()