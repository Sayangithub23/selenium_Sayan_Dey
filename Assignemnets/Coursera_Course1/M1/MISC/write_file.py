file = "example.txt"

with open(file, "r") as file:
    lines = file.readlines()

with open("passed.txt", "w") as passed:
    for line in lines:
        if "Passed" in line:
            passed.write(line)

with open("failed.txt", "w") as failed:
    for line in lines:
        if "Failed" in line:
            failed.write(line)