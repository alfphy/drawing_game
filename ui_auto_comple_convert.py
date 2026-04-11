import os
import subprocess
import sys

UI_DIR = "ui"
RESOURCES_DIR = "resources_rc"


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


def get_rc_imports():
    """Get all *_rc.py files from resources directory"""
    rc_imports = []

    if not os.path.exists(RESOURCES_DIR):
        return rc_imports

    for file in os.listdir(RESOURCES_DIR):
        if file.endswith("_rc.py"):
            module_name = file.replace(".py", "")
            rc_imports.append(f"resources_rc.{module_name}")

    return rc_imports


def add_imports_to_py(py_path, rc_imports):
    """Add import statements for all rc modules"""
    if not rc_imports:
        return

    with open(py_path, 'r') as f:
        lines = f.readlines()

    # Check which imports are missing
    existing_imports = set()
    for line in lines:
        for rc in rc_imports:
            if f"import {rc}" in line:
                existing_imports.add(rc)

    missing_imports = [rc for rc in rc_imports if rc not in existing_imports]

    if not missing_imports:
        return

    # Find insertion point (after PyQt6 imports)
    insert_index = 0
    for i, line in enumerate(lines):
        if line.startswith('from PyQt6') or line.startswith('import PyQt6'):
            insert_index = i + 1

    # Add missing imports
    for rc in missing_imports:
        lines.insert(insert_index, f"import {rc}\n")
        insert_index += 1

    # Write back
    with open(py_path, 'w') as f:
        f.writelines(lines)

    print(f"  Added imports: {', '.join(missing_imports)}")


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

    rc_imports = get_rc_imports()
    if rc_imports:
        print(f"Found resource modules: {', '.join(rc_imports)}")
    else:
        print("No resource modules found in 'resources/' directory.")

    for ui_file in sorted(ui_files):
        ui_path = os.path.join(UI_DIR, ui_file)
        py_file = ui_file.replace(".ui", ".py")
        py_path = os.path.join(UI_DIR, py_file)

        print(f"Compiling: {ui_file} -> {py_file}")
        result = subprocess.run([pyuic6_cmd, ui_path, "-o", py_path])

        if result.returncode == 0:
            add_imports_to_py(py_path, rc_imports)
            print(f"  ✓ Success")
        else:
            print(f"  ✗ Failed")

    print(f"\nDone! Compiled {len(ui_files)} file(s).")


if __name__ == "__main__":
    compile_ui_files()