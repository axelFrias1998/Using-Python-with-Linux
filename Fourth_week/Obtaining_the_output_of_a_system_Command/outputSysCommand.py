import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

errorResult = subprocess.run(["rm", "fileForError"], capture_output=True)
print(errorResult.returncode)
print(errorResult.stderr)
print(errorResult.stderr.decode())