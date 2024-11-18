# Simple-Keylogger-Prodigy-task4
A keylogger should only be used with explicit consent and for legitimate purposes, such as personal testing or authorized monitoring in controlled environments.

*Requirements
   You need the pynput library for capturing keystrokes. Install it using:
           *pip install pynput


Explanation
1. Key Press Callback:

Captures keys when pressed.
Writes regular keys (key.char) to a file.
Logs special keys like Shift, Ctrl, etc., as [KeyName].

2. Key Release Callback:

Stops the keylogger when the Esc key is pressed.

3. File Logging:

All key presses are appended to keylog.txt.

4. Stopping:

Press Esc to exit the program safely.


Usage
*Save the code to a file, e.g., keylogger.py.
*Run the script:
      python keylogger.py
*All keystrokes will be logged to keylog.txt

