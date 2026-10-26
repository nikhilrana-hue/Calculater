# Python GUI Calculator

A simple desktop calculator built with **Python** and **Tkinter**. The application provides a graphical interface for performing basic arithmetic operations, with a dark background, a numeric display, and clickable buttons styled using the **Times New Roman** font.

## Features

- **Addition (`+`)**
- **Subtraction (`−`)**
- **Multiplication (`×`)**
- **Division (`/`)**
- **Percentage (`%`)** — converts the displayed value to a percentage by dividing it by 100
- **Decimal point (`.`)** — allows decimal-number input
- **Clear (`C`)** — clears the display
- **Backspace (`⌫`)** — removes the last character
- **Equals (`=`)** — calculates and displays the result
- **Custom interface** — fixed-size `400 × 470` window, dark background, right-aligned display, and Times New Roman text

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Programming language used to implement the calculator |
| **Tkinter** | Python's standard GUI library for creating the window and interface |
| **`tkinter.Entry`** | Displays the numbers entered and calculation results |
| **`tkinter.Button`** | Creates clickable number and operation buttons |
| **`place()` geometry manager** | Positions the display and buttons at specific coordinates |
| **Callback functions and `lambda`** | Connect button clicks to the calculator's operations |
| **Python functions and conditional statements** | Handle input, arithmetic operations, clearing, backspace, and percentage calculations |

> **Note:** The code imports `tkinter.ttk`, but the current interface uses `tk.Entry` and `tk.Button` rather than themed `ttk` widgets.

## Requirements

- Python **3.x**
- Tkinter, which is included with most standard Python installations

No third-party Python packages are required.

## Getting Started

### 1. Download or clone the project

Place `calc.py` in your project folder.

### 2. Check Python

Open a terminal or command prompt and run:

```bash
python --version
```

On some systems, you may need to use:

```bash
python3 --version
```

### 3. Run the calculator

Navigate to the folder containing `calc.py`, then run:

```bash
python calc.py
```

If your system uses `python3`, run:

```bash
python3 calc.py
```

The calculator window should open on your desktop.

## How to Use

1. Click the number buttons to enter the first number.
2. Click an arithmetic operator (`+`, `-`, `X`, or `/`).
3. Enter the second number.
4. Press `=` to display the result.
5. Use `%` to divide the current displayed value by 100.
6. Use `.` to enter a decimal point.
7. Press `C` to clear the display or `⌫` to remove the last character.

## Project Structure

```text
python-gui-calculator/
├── calc.py       # Calculator application
└── README.md     # Project documentation
```

## Learning Outcomes

This project is useful for practising:

- Python functions and variables
- GUI development with Tkinter
- Creating and positioning widgets
- Handling button events and callbacks
- Reading and updating entry-field text
- Using conditional statements to select arithmetic operations
- Converting text input to numeric values with `float()`

## Current Limitations

This is a beginner-friendly calculator project. The current code does not yet include input validation or error handling for cases such as dividing by zero, pressing an operator when the display is empty, or entering invalid numeric input. These cases may cause a runtime error. The calculator also uses a fixed window size and does not support keyboard-based input.

## Possible Improvements

- Add error handling for empty input and division by zero.
- Add keyboard support.
- Improve the layout using `grid()` so the buttons resize more naturally.
- Add a consistent colour theme and hover effects.
- Format whole-number results without unnecessary decimal zeros.
- Refactor the arithmetic logic to reduce repeated code.

## License

No license has been specified for this project. Add a license file if you plan to distribute or reuse the code publicly.

---

**Author:** Add your name here  
**Project:** Python GUI Calculator  
**Language:** Python
