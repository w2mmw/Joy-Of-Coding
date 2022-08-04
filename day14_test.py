#*************************************************
# Day 14 test project.
# Author: Michael Weller
# The program will take comma deliniated file (.csv) that has a student name, semester, and grade.
# It will split the file into 3 lists and compute the mean, median, standard deviation, for two
# semeters.

#****************************************************
# function: listOfLines()
# This function takes a file and creates a list which each item in a line in the file.
from logging.config import listen


def listOfLines(fileName):
    dataFile = open(fileName) # open the data file
    list = []
    for line in dataFile: # run for every line in the list
        list.append(line) # add the line to a list.
        #print(line)
    return list

#****************************************************
# function: computeStats()
# This function takes a lsit of grades and computes either the mean, medium, or STD.
def computeStats(list, stat):
    if stat == "Mean":
        return statistics.mean(list) #calculate the mean
        
    elif stat == "Median":
        return statistics.median(list) # calculate the median
    else:
        return statistics.stdev(list) # calculate the standard deviation

#****************************************************
# function: main()
# This function performs the main tasks of the program.
def main():
    springList = []
    fallList = []
    lineList = listOfLines("sample_grades.csv") # take a file and get a list of lines in file.
    for x in lineList:
        list = x.split(",") # split the line by commas into a list
        if list[1] == "Spring 2016":
            springList.append(eval(list[2].replace("\n", "")))
        else:
            fallList.append(eval(list[2].replace("\n", "")))
    
    meanSpring = computeStats(springList, "Mean")
    meanFall = computeStats(fallList, "Mean")
    medianSpring = computeStats(springList, "Median")
    medianFall = computeStats(fallList, "Median")
    STDSpring = computeStats(springList, "STD")
    STDFall = computeStats(fallList, "STD")
    # Print the results to the screen.
    print("                Fall 2016                Spring 2016")
    print("Mean:           " + str(meanFall) + "        " + str(meanSpring))
    print("Median:         " + str(medianFall) + "                     " + str(medianSpring))
    print("Standare Dev.   " + str(STDFall)+ "        " + str(STDSpring))


import statistics # Import the statistics library
main() # call the main function