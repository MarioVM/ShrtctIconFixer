import os
import logging
from tqdm import tqdm
import win32com.client

# Set up logging
logging.basicConfig(filename='iconfxr.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_and_update_shortcut_icon(shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    icon_path, icon_index = shortcut.IconLocation.split(',')

    if not os.path.exists(icon_path):
        # Try changing drive letter to W
        new_icon_path = 'W' + icon_path[1:]
        if not os.path.exists(new_icon_path):
            # Try changing drive letter to F
            new_icon_path = 'F' + icon_path[1:]
            if not os.path.exists(new_icon_path):
                logging.warning(f"Icon path still broken after changing drive letters: {shortcut_path}")
                return
        shortcut.IconLocation = f"{new_icon_path},{icon_index}"
        shortcut.Save()
        logging.info(f"Updated icon path for: {shortcut_path}")
    else:
        logging.info(f"Icon path is valid for: {shortcut_path}")

def main():
    current_folder = os.getcwd()
    shortcuts = [item for item in os.listdir(current_folder) if item.endswith('.lnk')]

    for shortcut in tqdm(shortcuts, desc="Checking shortcuts", unit="shortcut"):
        shortcut_path = os.path.join(current_folder, shortcut)
        check_and_update_shortcut_icon(shortcut_path)

if __name__ == "__main__":
    main()
