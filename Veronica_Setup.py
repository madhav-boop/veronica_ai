import os
import subprocess
import sys

# Ensure Python version is 3.10 or higher
if sys.version_info < (3, 10):
    sys.exit("[ERROR] Python 3.10 or higher is required.")

# Create a virtual environment for isolation
VENV_DIR = "veronica_venv"
if not os.path.exists(VENV_DIR):
    print("[INFO] Creating a virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)

# Define the pip executable within the virtual environment
PIP_EXEC = os.path.join(VENV_DIR, "Scripts", "pip") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")

# Auto-install required dependencies
REQUIRED_PACKAGES = [
    "torch", "transformers", "speechrecognition", "sounddevice", "numpy",
    "opencv-python", "scipy", "pyttsx3", "requests", "beautifulsoup4", "pynput"
]

print("[INFO] Upgrading pip...")
subprocess.run([PIP_EXEC, "install", "--upgrade", "pip"], check=True)

print("[INFO] Installing necessary dependencies...")
subprocess.run([PIP_EXEC, "install"] + REQUIRED_PACKAGES, check=True)

print("[INFO] Veronica AI Setup Completed Successfully!")
