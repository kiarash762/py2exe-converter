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
1. **Python 3.x** installed.
2. **PyInstaller** installed on your system.

To install PyInstaller, run:
```bash
pip install pyinstaller
