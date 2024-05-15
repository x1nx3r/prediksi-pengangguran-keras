import os
import sys
import subprocess

# Define the required Python version
REQUIRED_PYTHON_VERSION = (3, 9, 19)
REQUIREMENTS_FILE = 'requirements.txt'

def get_python_version():
    """Get the current Python version."""
    return sys.version_info

def check_python_version():
    """Check if the current Python version matches the required version."""
    current_version = get_python_version()
    if current_version[:3] != REQUIRED_PYTHON_VERSION:
        print(f"Warning: The current Python version is {current_version[0]}.{current_version[1]}.{current_version[2]}")
        print(f"Expected Python version is {REQUIRED_PYTHON_VERSION[0]}.{REQUIRED_PYTHON_VERSION[1]}.{REQUIRED_PYTHON_VERSION[2]}")
        response = input("Please install the required python version (ok): ").strip().lower()
        print("Aborting.")
        sys.exit(1)

def is_venv():
    """Check if running in a virtual environment."""
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def install_requirements():
    """Install the required packages from requirements.txt."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', REQUIREMENTS_FILE])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")
        sys.exit(1)

def main():
    check_python_version()

    if not is_venv():
        print("Warning: It is recommended to use a virtual environment.")
        response = input("Do you want to proceed without a virtual environment? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Aborting.")
            sys.exit(1)

    install_requirements()
    print("Requirements installed successfully.")
    print('You can now run dependency_check.py to verify the module versions')

if __name__ == '__main__':
    main()
