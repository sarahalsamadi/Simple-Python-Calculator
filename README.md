# 🔢 Simple-Python-Calculator

A lightweight and functional desktop calculator built using **Python** and the **PyQt6** framework. This project demonstrates the use of graphical layouts and event handling in a desktop environment.

## 🚀 Overview
The calculator provides a familiar interface for performing basic mathematical operations. It is designed with a responsive grid layout, making it easy to use and extend with more complex functions.

## 🛠️ Tech Stack
- **Language:** Python 🐍
- **GUI Framework:** `PyQt6` (Qt for Python).
- **Layout Logic:** `QGridLayout` for organized button placement.

## 📊 Project Workflow
1. **Window Initialization:** The app sets up a main window with a fixed geometry and title.
2. **UI Construction:** - A `QLineEdit` serves as the display screen (Read-only).
   - A list of tuples defines the buttons and their positions in the grid.
3. **Event Handling:** Each button is connected to a central `on_button_click` function.
4. **Calculation:** The system uses Python's `eval()` function to compute results safely from the display string.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sarahalsamadi/Simple-Python-Calculator.git](https://github.com/sarahalsamadi/Simple-Python-Calculator.git)

2. **Install required dependencies:**
   ```bash
   pip install PyQt6

3. **Run the Application:**
   ```bash
python calucater.py

## 📝 Key Features
- **Basic Arithmetic:** Supports +, -, *, and /.
- **Clear Function:** A "C" button to reset the display instantly.
- **Error Handling:** Built-in try-except block to catch division by zero or invalid expressions, displaying "Error" to the user.
- **Clean Design:** Simple styling via CSS-like strings (StyleSheets) for better button visibility.
