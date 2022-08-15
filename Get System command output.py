import subprocess
text=subprocess.check_output("dir", shell=True)
print("dir command to list file and directory")
print(text)