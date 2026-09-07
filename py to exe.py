import subprocess
import os
import sys

def convert_to_exe():
    print("=======================================")
    print("      Python to EXE Converter         ")
    print("=======================================")

    # Get file path from user
    file_path = input("Enter the path or name of your .py file: ").strip()

    # Remove quotes if the user copied the path with them
    file_path = file_path.replace('"', '').replace("'", "")

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    try:
        print(f"\n[!] Starting conversion for: {file_path}")
        print("[!] This may take a minute depending on your script size...")

        # Run PyInstaller
        # --onefile: Bundles everything into a single .exe
        # --clean: Cleans PyInstaller cache before building
        subprocess.run(["pyinstaller", "--onefile", "--clean", file_path], check=True)

        print("\n" + "="*40)
        print("SUCCESS: Conversion complete!")
        print(f"Your executable is located in the 'dist' folder.")
        print("="*40)

    except FileNotFoundError:
        print("Error: PyInstaller is not installed. Please run 'pip install pyinstaller' first.")
    except subprocess.CalledProcessError:
        print("Error: PyInstaller encountered an error during the build process.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_to_exe()
    input("\nPress Enter to exit...")