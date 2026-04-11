import os
import subprocess
import sys

ASSETS_DIR = "assets"
OUTPUT_DIR = "resources_rc"  # Output to project root as icons_rc.py


def find_pyside6_rcc():
    """Find pyside6-rcc executable"""
    venv_rcc = os.path.join(sys.prefix, 'Scripts', 'pyside6-rcc.exe')
    if os.path.exists(venv_rcc):
        return venv_rcc

    import shutil
    rcc_path = shutil.which('pyside6-rcc')
    if rcc_path:
        return rcc_path

    return None


def compile_qrc_files():
    """Compile .qrc files to _rc.py"""
    rcc_cmd = find_pyside6_rcc()

    if not rcc_cmd:
        print("ERROR: pyside6-rcc not found!")
        print("Install: pip install PySide6")
        return

    if not os.path.exists(ASSETS_DIR):
        print(f"ERROR: Directory '{ASSETS_DIR}' not found!")
        return

    qrc_files = []
    for root, dirs, files in os.walk(ASSETS_DIR):
        for file in files:
            if file.endswith(".qrc"):
                qrc_files.append(os.path.join(root, file))

    if not qrc_files:
        print(f"No .qrc files found in '{ASSETS_DIR}' directory.")
        return

    for qrc_path in sorted(qrc_files):
        qrc_file = os.path.basename(qrc_path)
        py_file = qrc_file.replace(".qrc", "_rc.py")
        py_path = os.path.join(OUTPUT_DIR, py_file)

        print(f"Compiling: {qrc_path} -> {py_file}")
        result = subprocess.run([rcc_cmd, qrc_path, "-o", py_path])

        if result.returncode == 0:
            print(f"  ✓ Success")
        else:
            print(f"  ✗ Failed")

    print(f"\nDone! Compiled {len(qrc_files)} file(s).")


if __name__ == "__main__":
    compile_qrc_files()