

import sys

def command_quest():
    if sys.argv.__len__() < 2:
        print("Script name: " + sys.argv[0][2:])
        print("No arguments provided!")
        return(print("Total arguments: " + str(sys.argv.__len__()-1)))
    for i in range(sys.argv.__len__()):
        if i == 0:
            print("Script name: " + sys.argv[i][2:])
        else:
            print("Argument " + str(i) + ": " + sys.argv[i])
    return(print("Total arguments: " + str(sys.argv.__len__()-1)))
       
command_quest()