import sys


def printProgressBar(step, totalSteps, title=""):
    """
    putting this function in a loop with a known amount of iterations will print a working
    progressbar in the console of the form:
    'title' |██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 07.31%
    :param step: current iteration
    :param totalSteps: total amount of iterations
    :param title: optional text that will be shown next to the progress bar
    :return: void
    """
    loaded = "█"
    notLoaded = "░"

    progressBarLength = 40
    loaded = progressBarLength*loaded
    notLoaded = progressBarLength*notLoaded

    percentage = (step/totalSteps)
    amountLoaded = int(percentage*progressBarLength)



    strPercentage = f" {percentage*100:05.2f}%"
    outputString ="\r" + title + " |" + loaded[:amountLoaded] + notLoaded[amountLoaded:] + "|" + strPercentage
    sys.stdout.flush()
    sys.stdout.write(outputString)
