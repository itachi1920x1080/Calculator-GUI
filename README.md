# Python Calculator GUI 🧮

A simple and intuitive Graphical User Interface (GUI) calculator built using Python and the `tkinter` library.

## 🌟 Features

- **Basic Arithmetic Operations**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
- **Clear Functions**: 
  - `C`: Clear all input.
  - `CE`: Clear current entry.
  - `DEL`: Delete the last character entered.
- **Error Handling**: Gracefully displays "Error" on invalid operations (e.g., division by zero or incomplete expressions).
- **Clean Layout**: Designed with a simple grid layout and styled buttons using Tkinter's grid system.

## 🛠️ Requirements

- **Python 3.x**
- `tkinter` (This library is usually pre-installed with the standard Python distribution).

## 🚀 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/itachi1920x1080/Calculator-GUI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Calculator-GUI
   ```
   *(Note: The actual folder name depends on your local checkout, here it assumes the root of the project).*

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the calculator application:
   ```bash
   python Calculator/src/calculator.py
   ```
   *(Ensure you run the application from the project root so it can locate `assets/my_logo.png` relative to the script correctly, or run it directly from the `src` directory depending on your setup).*

## 📂 Project Structure

```text
.
├── Calculator/
│   └── src/
│       ├── assets/
│       │   └── my_logo.png    # App window icon
│       └── calculator.py      # Main calculator application code
├── requirements.txt
└── README.md
```

## 📝 About

This is a beginner-friendly desktop application demonstrating how to build a basic user interface and handle events in Python using Tkinter.
