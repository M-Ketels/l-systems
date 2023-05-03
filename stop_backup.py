from subprocess import check_output
import os
pid_loop = check_output(["pidof", "python3 loop.py"])

print(f"pid: {pid_loop}")
os.kill(pid_loop)
