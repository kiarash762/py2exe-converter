# Py2Exe CLI Tool 🚀

A lightweight, interactive command-line utility to convert Python scripts (`.py`) into standalone Windows executable files (`.exe`) using PyInstaller.

---

## ✨ Features

- **Interactive CLI:** Simply run the script and paste or type the path to your Python file.
- **Path Sanitization:** Automatically cleans up quotation marks from pasted file paths.
- **Single Executable Output:** Builds a single self-contained binary using `--onefile`.
- **Clean Builds:** Clears the PyInstaller cache before compilation via `--clean`.
- **Zero Configuration:** No complex command-line arguments needed.

---

## 📋 Prerequisites

Before using this tool, make sure you have:
1. **Python 3.x** installed and added to your system's `PATH`.
2. **PyInstaller** installed on your system.

To install PyInstaller, run:
```bash
pip install pyinstaller
```

---

## 🚀 Usage

Follow these steps to convert your Python script into an executable file:

### 1. Clone or download the repository
```bash
git clone https://github.com/<your-username>/py2exe-converter.git
cd py2exe-converter
```

### 2. Run the converter script
```bash
python "py to exe.py"
```

### 3. Provide the path to your Python script
Enter the full absolute path or relative path to the `.py` file you want to compile:

```plaintext
=======================================
      Python to EXE Converter         
=======================================
Enter the path or name of your .py file: script.py
```
> **Note:** If you copied the path with quotes, the script will automatically strip them for you.

### 4. Wait for PyInstaller to finish compilation
```plaintext
[!] Starting conversion for: script.py
[!] This may take a minute depending on your script size...
```

### 5. Locate your compiled executable
Once completed, PyInstaller outputs your standalone executable inside the newly created `dist/` directory:

```plaintext
dist/
└── script.exe
```

---

## 📂 Project Structure

```plaintext
.
├── py to exe.py        # Main conversion script
├── dist/               # Output folder containing generated .exe files
├── build/              # PyInstaller temporary compilation files
├── *.spec              # PyInstaller project specification file
└── README.md           # Project documentation
```

---

## ⚠️ Notes & Troubleshooting

Here are common issues and considerations when compiling Python scripts:

- **PyInstaller Command Not Found:**  
  If you encounter `PyInstaller is not installed` or command errors, ensure that Python and PyInstaller are added to your system's `PATH` environment variable.  
  Test PyInstaller directly by running:
  ```bash
  pyinstaller --version
  ```

- **Missing External Assets (Images, Icons, Config Files):**  
  PyInstaller packages Python bytecode and libraries into the binary, but does not bundle local assets (e.g. `.png`, `.json`, `.db`) by default.  
  To include assets, edit the generated `.spec` file and add them to the `datas` array, then build using:
  ```bash
  pyinstaller script.spec
  ```

- **Antivirus False Positives:**  
  Standalone binaries generated with PyInstaller without a commercial code-signing certificate may trigger heuristic warnings in Windows Defender or other antivirus software. Adding an exclusion or signing the binary will resolve this.

- **Hidden Imports:**  
  If your script uses dynamic module loading (e.g., `importlib`), PyInstaller might miss those dependencies. You can pass `--hidden-import <module_name>` or add them to the `.spec` file.

- **Cleaning Build Artifacts:**  
  The tool uses `--clean` by default. You can safely delete the `build/` folder and `.spec` files between builds to keep your directory tidy.

---

## 📄 License

This project is open source and available under the **MIT License**.

```plaintext
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
