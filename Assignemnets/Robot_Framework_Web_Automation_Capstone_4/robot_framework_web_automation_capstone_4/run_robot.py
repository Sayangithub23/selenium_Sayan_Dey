import os
import subprocess
import sys

os.makedirs("results", exist_ok=True)

command = [
    sys.executable,
    "-m",
    "robot",
    "--outputdir",
    "results",
    "tests",
]

result = subprocess.run(command)
sys.exit(result.returncode)
