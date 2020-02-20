# Alex Harris
# 08/24/19

from AreaCodes import *

def main():
    r = AreaCodes()
    #prime the loops
    userInput = str(input("enter area code or region: "))
    while userInput != "":
        #Check if it's an area code
        if userInput[0] == "0" or userInput[0] == "1" or userInput[0] == "2" or userInput[0] == "3" \
                or userInput[0] == "4" or userInput[0] == "5" or userInput[0] == "6"\
                or userInput[0] == "7" or userInput[0] == "8" or userInput[0] == "9":
            region = r.regionForAreaCode(userInput)
            #if the area code is valid, print it
            if region != None:
                print(r.regionForAreaCode(userInput))
        else:
            #else its a region
            regions = r.areaCodesForRegion(userInput)
            #if the region is valid print it
            if regions == ():
                print("Invalid area code")
            else:
                print(regions)
        userInput = str(input("enter area code or region: "))


if __name__ == '__main__':
    main()