APPS_SUBFOLDER = "apps"
MONEY_TYPE = "€"

def getAppName(title):
    return APPS_SUBFOLDER + "." + title

def showPrice(amount):
    return MONEY_TYPE + " " + str(amount)