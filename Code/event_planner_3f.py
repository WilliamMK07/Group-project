import time
import sys
from itertools import chain, combinations

# this is the main function that calculates the best combination using the brute-force method
def brute_combo(file):
    # This part of the function is responsible for reading the file.
    f = open(file,"r") # file is opened in read mode
    n = int(f.readline()) # first line is read and this value is the number of activities
    b_t = f.readline() # second line is read which is the budget and the time
    b_t=b_t.split(" ",2) # the budget and time are split into an array
    budget = int(b_t[1]) # The budget is in the array at index 1, currently stored as a string so switched to an int 
    time = int(b_t[0]) # The time is in the array at index 0, currently stored as a string so switched to an int 

    activities = [] # Creates an empty array for all of the activities
    for i in range(n): # loops through the array and adds the activities to the activities array
        activity = f.readline()
        activity = activity.split(" ",4) # splits the line into an array
        activity[3] = activity[3].replace("\n",'') # removes the newline character
        activities.append(activity) # appends it to the activities array

    f.close() # closes the file

    options = powerset(activities) # uses the powerset function to get the powerset of the activities
    # sets the inital conditions for the loop.
    result = '' 
    max_happiness = 0
    max_budget = 0
    max_time = 0
    
    # loop to iterate through the powerset and find the best possible combination
    for i in range(len(options)):
        # Sets the inital conditions inside the loop
        h = False
        t = False
        b = False
        total_h = 0
        total_b = 0
        total_t = 0
        for j in range(len(options[i])): # this loop is used to add up the happiness, budget and time of each subset in the array
            total_h += int(options[i][j][3])
            total_b += int(options[i][j][2])
            total_t += int(options[i][j][1])
        if total_h > max_happiness: # evaulates if the happiness is greater than the previous happiness
            h = True
        if total_t <= time: # checks if the time is less than the time limit
            t = True
        if total_b <= budget:
            b = True
        if h and t: # checks if all 3 conditions are true then changes the max_happiness and updates the budget and time
            result = options[i] # stores the subset of the activities as the result
            max_happiness = total_h
            max_budget = total_b
            max_time = total_t
    # return the best subset which is the result, the happiness,budget and time of this result. and the time and budget limits from the file
    return result, max_happiness, max_budget, max_time, budget,time

def powerset(array): # this is the function that is used to create the powerset of the array
    s = list(array) # makes sure the array is a list
    # returns the list of activities by making every subset combination of the list. It starts from 1 instead of 0
    # as the value at index 0 will be the empty set. This would cause errors when indexing later. 
    return list(chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1)))


def read_input(filename):

    #gives the name f for easier recall
    with open(filename, "r") as f:
        n = int(f.readline())

        #splits the first line into two integer values
        time_budget = f.readline().split()
        max_time = int(time_budget[0])
        max_budget = int(time_budget[1])

        #creates a tuple for each activiy and adds time, cost and enjoyment
        activities = []
        for _ in range(n):
            name, tme, cst, enj = f.readline().split()
            activities.append((name, int(tme), int(cst), int(enj)))

    return activities, max_time, max_budget


def dynamic_programming(filename):
    activities, max_time, max_budget = read_input(filename)

    #for each budget amount a row is created 
    #for each time amount a column is created
    #the possibility of 0 budget and 0 time is included hence +1
    dp = [[0 for _ in range(max_budget + 1)]
          for _ in range(max_time + 1)]

    #combination of activites and their data stored
    chosen = [[[] for _ in range(max_budget + 1)]
              for _ in range(max_time + 1)]

    #new value is calculated to decide what to do with remaining time and budget
    for name, tme, cst, enj in activities:
        for time_left in range(max_time, tme - 1, -1):
            for budget_left in range(max_budget, cst - 1, -1):
                new_value = dp[time_left - tme][budget_left - cst] + enj

                #if new value has more enjoyment than selected value, then add. If not, nothing
                if new_value > dp[time_left][budget_left]:
                    dp[time_left][budget_left] = new_value
                    chosen[time_left][budget_left] = (
                        chosen[time_left - tme][budget_left - cst]
                        + [(name, tme, cst, enj)]
                    )

    #find best result
    best_happiness = 0
    best_time = 0
    best_budget = 0

    for t in range(max_time + 1):
        for b in range(max_budget + 1):
            if dp[t][b] > best_happiness:
                best_happiness = dp[t][b]
                best_time = t
                best_budget = b

    return (
        chosen[best_time][best_budget],
        best_happiness,
        best_time,
        best_budget,
        max_time,
        max_budget
    )

#runs the code and times the execution
def final_output(file): # this is the function that creates the final output of the functions. 
    
    start = time.time() # starts the time
    brute_force = brute_combo(file) # runs the function and saves the value to a variable 
    end = time.time() # ends the time
    speed = end - start # calculates the time taken for the function to run

    # space to add the dynamic approach:

    start_time = time.time()
    activities, happiness, time_used, budget_used, max_time, max_budget = dynamic_programming(file)
    end_time = time.time()
    execution_time = end_time - start_time


    # formatting the output from the brute force algorithm, as it returns an array the indexes of the array can be accessed
    # and they contain all of the necessary information for the final output
    print('======================================== \nEVENT PLANNER - RESULTS \n========================================\n')
    print(f"Input File: {file}")
    print(f"Available Time: {brute_force[5]}")
    print(f"Available Budget: {brute_force[4]}\n")

    print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    for a in activities:
        print(f" - {a[0]} ({a[1]} hours, £{a[2]}, enjoyment {a[3]})")

    print("\nTotals:")
    print(f"Total Enjoyment: {happiness}")
    print(f"Total Time Used: {time_used} hours")
    print(f"Total Cost: £{budget_used}")
    
    print(f"\nExecution Time: {execution_time:.6f} seconds")
    

    print("--- BRUTE FORCE ALGORITHM ---")
    print("Selected Activities:")
    for i in range(len(brute_force[0])):
        print(f" - {brute_force[0][i][0]} ({brute_force[0][i][1]} hours, £{brute_force[0][i][2]}, enjoyment {brute_force[0][i][3]})")
    print('')
    print(f"Total Enjoyment: {brute_force[1]}")
    print(f"Total Time Used: {brute_force[3]} hours")
    print(f"Total Cost: £{brute_force[2]}\n")
    print(f"Execution time: {speed:.4f} seconds")


#/workspaces/Group-project/Lists/input_10 (1).txt

if __name__ == "__main__":
    final_output(sys.argv[1])    
