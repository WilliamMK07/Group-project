import matplotlib.pyplot as plt 
from event_planner import brute_combo, dynamic 
import time
import sys
import numpy as np

def time_taken(file):
    start1 = time.time()
    brute_combo(file)
    end1 = time.time()
    time1 = end1 - start1

    start2 = time.time()
    dynamic(file)
    end2 = time.time()
    time2 = end2 - start2

    return time1, time2

def main(file):
    
    res = time_taken(file)
    times = np.log(res)
    plt.bar(times[0],"Brute Force")
    plt.bar(times[1],"Dynamic programming")
    plt.xlabel("Algorithms")
    plt.ylabel("log of time taken")
    plt.show()



if __name__ == "__main__":
    main(sys.argv[1]) 




