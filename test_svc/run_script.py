import os
import subprocess
import sys


def main():
    if os.name == 'nt':
        python_executable = os.path.join(sys.exec_prefix, 'pythonw.exe')
    else:
        python_executable = os.path.join(sys.exec_prefix, 'bin', 'python3')
    
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))
    subprocess.Popen([python_executable, script_path])


if __name__ == "__main__":
    main()
