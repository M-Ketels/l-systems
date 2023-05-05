import start_backup as sb
import os

if sb.check_if_subprocess_backups_running():
    pid = sb.find_pid_subprocess_backups()
    os.system(f'kill {pid}')