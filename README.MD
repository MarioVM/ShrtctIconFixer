# IconFXR

IconFXR is a Python script designed to check and fix broken icon paths in Windows shortcut files (.lnk) within the current directory. The script attempts to resolve broken icon paths by changing the drive letter to `W:` and, if still broken, to `F:`.

## Features

- Checks icon paths of all shortcut files in the current directory.
- Attempts to fix broken icon paths by changing the drive letter.
- Logs all actions and outcomes to a log file (`iconfxr.log`).
- Displays a progress bar for the processing of shortcut files.

## Requirements

- Windows 11
- Python 3.x
- `pywin32` package
- `tqdm` package

## Installation

1. **Install Python 3.x**:
   Download and install Python from [python.org](https://www.python.org/).

2. **Install required packages**:
   Open a command prompt and run the following commands:
   ```bash
   pip install pywin32 tqdm

Usage
Running the Python Script Directly
Save the script:
Save the script as iconfxr.py in the folder where you want to check the shortcuts.

Run the script:
Open a command prompt and navigate to the folder where you saved iconfxr.py. Run the script using Python:

python iconfxr.py

The script will process all .lnk files in the current directory, attempting to fix broken icon paths and logging the results.

Running the PowerShell Script
Run run_iconfxr.ps1 in the same folder as iconfxr.py:

Logging
All actions and outcomes are logged to a file named iconfxr.log in the current directory.

License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue on the GitHub repository.

Acknowledgments
This script uses the pywin32 package for handling Windows shortcuts and the tqdm package for displaying a progress bar.

Logging
All actions and outcomes are logged to a file named iconfxr.log in the current directory.

License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue on the GitHub repository.

Acknowledgments
This script uses the pywin32 package for handling Windows shortcuts and the tqdm package for displaying a progress bar.

© 2024 MarioVM