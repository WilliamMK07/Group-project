
import matplotlib.pyplot as plt 
from event_planner import brute_combo, dynamic 
import time
import sys
import numpy as np

# imports the necessary libraries as well as the required functions from the event planner graph

def time_taken_b():
    # finds the time taken for the brute force algorithm to execute on each file size
    start1 = time.time()
    brute_combo('Input_Files/input_small.txt')
    end1 = time.time()
    btime1 = end1 - start1

    start2 = time.time()
    brute_combo('Input_Files/input_medium.txt')
    end2 = time.time()
    btime2 = end2 - start2

    start3 = time.time()
    brute_combo('Input_Files/input_large.txt')
    end3 = time.time()
    btime3 = end3 - start3

def time_taken_d():
    # finds the time taken for the brute force algorithm to execute on each file size
    start1 = time.time()
    dynamic('Input_Files/input_small.txt')
    end1 = time.time()
    dtime1 = end1 - start1

    start2 = time.time()
    dynamic('Input_Files/input_medium.txt')
    end2 = time.time()
    dtime2 = end2 - start2

    start3 = time.time()
    dynamic('Input_Files/input_large.txt')
    end3 = time.time()
    dtime3 = end3 - start3


    # returns both times as an array
    return dtime1, dtime2, dtime3

def main():
    #runs the time_taken file and saves the results
    resb = time_taken_b()
    resd = time_taken_d()
    # takes a log of the times
    files = ["Small","Medium","Large"]
    # sets the names
    names = ["Brute Force", "Dynamic"]
    
    # runs the brute force algorithm approach 
    plt.bar(files,resb, label = names[0])
    plt.bar(files, resd, label = names[1])
    plt.xlabel("Algorithms")
    plt.ylabel("log of time taken")
    plt.legend()
    plt.autoscale()
    plt.savefig("plot.png")


if __name__ == "__main__":
    main() 




