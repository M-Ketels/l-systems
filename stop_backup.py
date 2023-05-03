from subprocess import check_output
import os
pid_loop = check_output(["pidof", "python3 loop.py"])

os.kill(pid_loop)
