import os
import subprocess
import sys

UI_DIR = "ui"


def find_pyuic6():
    """Find pyuic6 executable"""
    # Check virtual environment Scripts folder
    venv_pyuic6 = os.path.join(sys.prefix, 'Scripts', 'pyuic6.exe')
    if os.path.exists(venv_pyuic6):
        return venv_pyuic6

    # Check if it's in PATH
    import shutil
    pyuic6_path = shutil.which('pyuic6')
    if pyuic6_path:
        return pyuic6_path

    return None


def compile_ui_files():
    pyuic6_cmd = find_pyuic6()

    if not pyuic6_cmd:
        print("ERROR: pyuic6 not found!")
        print("Try reinstalling PyQt6: pip install --force-reinstall PyQt6")
        return

    if not os.path.exists(UI_DIR):
        print(f"ERROR: Directory '{UI_DIR}' not found!")
        return

    ui_files = [f for f in os.listdir(UI_DIR) if f.endswith(".ui")]

    if not ui_files:
        print(f"No .ui files found in '{UI_DIR}' directory.")
        return

    for ui_file in sorted(ui_files):
        ui_path = os.path.join(UI_DIR, ui_file)
        py_file = ui_file.replace(".ui", ".py")
        py_path = os.path.join(UI_DIR, py_file)

        print(f"Compiling: {ui_file} -> {py_file}")
        result = subprocess.run([pyuic6_cmd, ui_path, "-o", py_path])

        if result.returncode == 0:
            print(f"  ✓ Success")
        else:
            print(f"  ✗ Failed")

    print(f"\nDone! Compiled {len(ui_files)} file(s).")


if __name__ == "__main__":
    compile_ui_files()