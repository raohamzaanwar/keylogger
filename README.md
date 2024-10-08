Here’s a more polished and professional version of the README for better presentation in GitHub:

---

# Python Keylogger

## Overview

This repository contains Python code for a simple **keylogger** that captures and logs keystrokes on both **Windows** and **Linux** platforms. A keylogger is a tool that records (logs) the keys pressed on a keyboard, which can be used for troubleshooting, monitoring, or educational purposes.

⚠️ **Disclaimer**: This keylogger is created for **educational purposes only**. Unauthorized use of keyloggers to capture user input can violate privacy laws. Ensure you have explicit permission before using it on any system.

---

## Features

### Windows Keylogger:
- Logs all key presses.
- Hides the console window for silent execution.
- Saves key logs to a hidden `C:\output.txt` file.
- Stops keylogging when **Ctrl + E** is pressed.

### Linux Keylogger:
- Logs all key presses.
- Saves key logs to `~/Desktop/file.log`.
- Stops keylogging by pressing the **backtick (`)** key.
- Option to clear the log file on startup using environment variables.

---

## Prerequisites

### For Windows:
- Install `pywin32` to access the Windows API:
    ```bash
    pip install pywin32
    ```
- Install `pyHook` to hook keyboard events:
    ```bash
    pip install pyHook
    ```

### For Linux:
- Install `python-Xlib` to hook into X11 keyboard events:
    ```bash
    sudo apt-get install python-xlib
    ```
- Install `pyxhook` to capture keyboard events:
    ```bash
    pip install pyxhook
    ```

---

## Installation

### Clone the Repository:
```bash
git clone https://github.com/raohamzaanwar/keylogger
```

### Install Dependencies:
Follow the steps in the **Prerequisites** section to install the necessary libraries based on your platform.

---

## Usage

### Running the Keylogger on **Windows**:
1. Save the code in the repository as `Keylogger.py` in the `C:\` directory.
2. Run the keylogger using:
    ```bash
    python Keylogger.py
    ```
3. The keylogger will run in the background, and keystrokes will be logged to `C:\output.txt`.
4. To stop the keylogger, press **Ctrl + E**.

### Running the Keylogger on **Linux**:
1. Save the Linux keylogger code as `keylogger.py`.
2. Run the keylogger using:
    ```bash
    python keylogger.py
    ```
3. The keylogger will log all key presses to `~/Desktop/file.log`.
4. Press the **backtick (`)** key to stop the keylogger.

---

## Code Explanation

### Windows Keylogger
- **Hides Console Window**: The console window is hidden using `win32gui.ShowWindow(win, 0)` to ensure the keylogger runs silently.
- **Keystroke Logging**: The `pyHook` library captures and logs keystrokes, which are saved to `C:\output.txt`.
- **Exit Mechanism**: The script stops when **Ctrl + E** (ASCII 5) is pressed.

### Linux Keylogger
- **Keystroke Logging**: The `pyxhook` library captures keystrokes, which are saved to `~/Desktop/file.log`.
- **Exit Mechanism**: The keylogger stops when the **backtick (`)** key is pressed.
- **Clear Logs on Startup**: The log file can be cleared on startup by setting the `pylogger_clean` environment variable.

---

## Contributions

Feel free to open issues or submit pull requests if you find bugs or want to enhance the features. Please ensure your contributions align with the ethical use of this software.

---

## License
This project is licensed under the **MIT License**. 
---

## Disclaimer

This tool is for **educational purposes only**. Misuse of this tool for illegal purposes is strictly prohibited. Always ensure you have explicit permission from the system owner before using a keylogger. The author is **not responsible** for any misuse or damages caused by this tool.

---

This version is cleaner and more structured, making it easier to read and understand in a GitHub repository.
