import os


def listdir_not_hidden(path: str) -> list:
    res = []
    for file in os.listdir(path):
        if not file.startswith('.'):
            res.append(file)
    return res


def backup_dict(backup_path: str) -> dict:
    backup_format = {}
    tracker = 1
    all_backups = listdir_not_hidden(backup_path)

    for backup in all_backups:
        backup_format[tracker] = backup
        tracker += 1

    return backup_format


def restore(backup_path: str, backup_format: dict, history_path: str) -> None:
    for key in backup_format:
        print(key, backup_format[key])

    chosen_value = int(input("Choose a backup to restore. "))
    backup_chosen = open(backup_path + "/" + backup_format[chosen_value])
    current_history = open(history_path, "w")
    current_history.write(backup_chosen.read())
    backup_chosen.close()
    current_history.close()


if __name__ == "__main__":

    backup_location = f"""{os.getenv("HOME")}/.l-systems"""
    history_location = "History/history_lsystems.txt"
    restore(backup_location, backup_dict(backup_location), history_location)
