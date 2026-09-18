import subprocess

scripts = ["color_converter.py", "ultra_points_functions.py"]

for script in scripts:
    result = subprocess.run(["python", script])
