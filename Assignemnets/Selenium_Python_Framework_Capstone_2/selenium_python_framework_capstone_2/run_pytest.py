import os
import subprocess
import sys

os.makedirs("reports", exist_ok=True)
sys.exit(subprocess.run([sys.executable, "-m", "pytest"]).returncode)
