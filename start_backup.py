import subprocess
import psutil


def start_subprocess_backups():
    p = subprocess.Popen('python3 loop.py', shell=True)


def check_if_subprocess_backups_running() -> bool:
    pid_loop_found = False
    for process in psutil.process_iter(['cmdline']):
        if process.name() == "python3":
            if process.info['cmdline'][-1] == "loop.py":
                pid_loop_found = True
    return pid_loop_found


def find_pid_subprocess_backups() -> int:
    pid_loop = "not yet found"
    for process in psutil.process_iter(['cmdline']):
        if process.name() == "python3":
            if process.info['cmdline'][-1] == "loop.py":
                pid_loop = process.pid
    return pid_loop
