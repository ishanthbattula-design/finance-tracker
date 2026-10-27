# finance-tracker
A simple Python command-line app to help you log your daily spending and keep an eye on your budget. It saves your data to a text file so your expenses are remembered even after you close the program.

## What it does
- Keeps running in a menu loop until you choose to exit.
- Saves what you bought and the cost into a local text file.
- Reads your saved history and prints it clearly in the terminal.
- Calculates your total spend and compares it to a budget limit to warn you if you spend too much.
- Safe from crashing if you type things wrong or haven't saved any files yet.

## Technical Details
- **File Persistence:** Uses Python's file handling to append data to a text file and read it back sequentially.
- **Data Parsing:** Uses `.strip()` and `.split()` methods to break text strings into separate variables for math processing.
- **Error Validation:** Includes `try` and `except` blocks to handle missing text files and incorrect inputs smoothly without crashing.

## How to run it
Run this command in your terminal:
```bash
python finance_tracker.py
```

