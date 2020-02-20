#!/usr/bin/env python3

# ----------------------------------------------------------------------
# AreaCodes.py
# Alex Harris
# 08/22/2019
# ----------------------------------------------------------------------

import sys
import csv

class AreaCodes:

    # ------------------------------------------------------------------

    def __init__(self, filename="areacodes.csv"):
        """
        reads data from specified file and stores data for area codes and region
        :param filename: the name of the file containing area code data
        """

        file = open(filename, "r")
        #Create an empty dictionary
        self.areaCodeDic = {}
        #for every time in the file
        for line in file:
            #strip white space and split at the comma
            codeInRegion = line.strip().split(",")
            #make the key the area code and the location the content
            self.areaCodeDic[codeInRegion[0]] = codeInRegion[1]
        file.close()
    # ------------------------------------------------------------------

    def regionForAreaCode(self, areaCode: str) -> str:
        """
        returns the region for the specified area code
        :param areaCode: string containing the digits of the area code
        :return: the region for the area code or the empty string if area code does not exist
        """

        #return the value at the key of the area code
        try:
            return self.areaCodeDic[areaCode]
        except KeyError:
             print("Invalid area code.")

    # ------------------------------------------------------------------

    def areaCodesForRegion(self, region: str) -> ():
        """
        returns a tuple of area code strings for the the specified region
        :param region: name of the region
        :return: tuple of area code strings for the specified region; returns an empty tuple if the region is invalid
        """

        #create an empty list
        listAreaCodes = []
        #go through the list and check if the region is the wanted region
        for areaCode in self.areaCodeDic:
            if self.areaCodeDic[areaCode] == region:
                #add area code to the region if it's the correct region
                listAreaCodes.append(areaCode)
        #turn the list into a tuple and return
        return tuple(listAreaCodes)

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------