import lSystems as ls
import lSystems_turtle as lst

if __name__ == "__main__":
    file_location = input("Location of the configuration file:\n")
    amount_of_iters = int(input("Amount of iterations: \n"))

    lst.draw_turtle(amount_of_iters, file_location, 0)


