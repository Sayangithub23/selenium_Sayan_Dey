import subprocess
import sys


def main():
    command = [
        sys.executable,
        "-m",
        "behave",
        "-f",
        "allure_behave.formatter:AllureFormatter",
        "-o",
        "allure-results",
    ]

    result = subprocess.run(command)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()