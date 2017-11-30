import subprocess

listita = subprocess.call(["find . -name '*.sh\'"], shell=True)
print(listita)

