import sys


def printProgressBar(step, totalSteps, titel=""):
    loaded = "█"
    notLoaded = "░"

    progressBarLength = 40
    loaded = progressBarLength*loaded
    notLoaded = progressBarLength*notLoaded

    percentage = (step/totalSteps)
    amountLoaded = int(percentage*progressBarLength)



    strPercentage = f" {percentage*100:05.2f}%"
    outputString ="\r" + titel + " |" + loaded[:amountLoaded] + notLoaded[amountLoaded:] + "|" + strPercentage
    sys.stdout.flush()
    sys.stdout.write(outputString)
