import subprocess

scripts = ["color_converter.py", "direction_check.py"]

for script in scripts:
    result = subprocess.run(["python", script])
