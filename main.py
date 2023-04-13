import lSystems as ls
import lSystems_turtle as lst
import Make_history as hist

if __name__ == "__main__":
    file_location = input("Location of the configuration file:\n")
    amount_of_iters = int(input("Amount of iterations: \n"))

    hist.make_history_file(file_location, amount_of_iters)
    lst.draw_turtle(amount_of_iters, file_location, 0)


