import lSystems as ls
import lSystems_turtle as lst
import make_history as hist
import start_backup as sb
import argparse

if __name__ == "__main__":

    #########################################
    # starting backups
    #########################################
    if not sb.check_if_subprocess_backups_running():
        sb.start_subprocess_backups()

    #########################################
    # added argument for image export
    #########################################

    parser = argparse.ArgumentParser()

    parser.add_argument("--export",
                        help="exports the drawn l-system to a specified image file",
                        default="no_export")

    args = parser.parse_args()

    if args.export == "no_export":
        export = False
        file_name = ""
    else:
        export = True
        file_name = args.export

    ##########################################
    # inputs
    ##########################################

    file_location = input("Location of the configuration file:\n")
    amount_of_iters = int(input("Amount of iterations: \n"))

    ##########################################
    # actual drawing and history setting
    ##########################################

    hist.make_history_file(file_location, amount_of_iters)
    lst.draw_turtle(amount_of_iters, file_location, 0, show_progressbar=True, export=export, export_file_name=file_name)
