
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
    brute_combo('Input_Files/input_10.txt')
    end2 = time.time()
    btime2 = end2 - start2

    start3 = time.time()
    brute_combo('Input_Files/input_15.txt')
    end3 = time.time()
    btime3 = end3 - start3

    start4 = time.time()
    brute_combo('Input_Files/input_20.txt')
    end4 = time.time()
    btime4 = end4 - start4

    return btime1, btime2, btime3, btime4

def time_taken_d():
    # finds the time taken for the brute force algorithm to execute on each file size
    start1 = time.time()
    dynamic('Input_Files/input_small.txt')
    end1 = time.time()
    dtime1 = end1 - start1

    start2 = time.time()
    dynamic('Input_Files/input_10.txt')
    end2 = time.time()
    dtime2 = end2 - start2

    start3 = time.time()
    dynamic('Input_Files/input_15.txt')
    end3 = time.time()
    dtime3 = end3 - start3

    start4 = time.time()
    dynamic('Input_Files/input_20.txt')
    end4 = time.time()
    dtime4 = end4 - start4


    # returns both times as an array
    return dtime1, dtime2, dtime3, dtime4

def main():
    #runs the time_taken file and saves the results
    resb = time_taken_b()
    resd = time_taken_d()
    spf = []
    for i in range(len(resb)):
        spf.append(resb[i] / resd[i])

    files = [5,10,15,20]
    # sets the names
    names = ["Brute Force", "Dynamic"]
    
    # matplotlib function to plot the graphs with the time taken
    plt.semilogy(files,resb)
    plt.semilogy(files,resd)
    plt.plot(files,resb, label = names[0])
    plt.plot(files,resd, label = names[1])
    plt.title("Time taken for each algorithm")
    plt.xlabel("File Size")
    plt.ylabel("Log of Time taken")
    plt.legend()
    plt.autoscale()
    plt.savefig("LineGraph.png")
    plt.close()

    # matplotlib to plot the speedup factor

    plt.bar(files,spf, color = ("Blue","Orange","Green","Purple"), log = True)
    plt.title("Speedup factor for the algorithms")
    plt.xlabel("File Size")
    plt.ylabel("Log of the speedup factor")
    
    plt.autoscale()
    plt.savefig("BarChart.png")






if __name__ == "__main__":
    main() 




