# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit

# Add Settings
app = QApplication()
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(250, 300)

# All objects
text_box = QLineEdit()
grid = QGridLayout()

buttons = {
    "7", "8",  "9",  "/",
    "4",  "5",  "6",  "*",
    "1",  "2",  "3", "-",
    "8",  ".",  "=",  "+",
}

clear = QPushButton("Clear")
delete = QPushButton("<")

#function
def button_click():
    button = app.sender()
    text = button.text()

    if text == "=":
        symbol = text_box.text() #gets the current text from the QLineEdit widget. If the user has typed 3+5, symbol will contain the string "3+5".
        try:
            res = eval(symbol)  # eval() in the button_click() function allows evaluate the mathematical expression
            text_box.setText(str(res))  # widget expects a string as its input.
        except Exception as e:
            print("Error", e)

    elif text == "Clear":
        text_box.clear()

    elif text == "<":
        current_value = text_box.text()
        text_box.setText(current_value[:-1])

    else:
        current_value = text_box.text()
        text_box.setText(current_value + text)



row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1


# Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)
master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

# Show/Run
main_window.show()
app.exec_()