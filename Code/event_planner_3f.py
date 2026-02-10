import time
import sys


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
def print_results(filename):
    start_time = time.time()
    activities, happiness, time_used, budget_used, max_time, max_budget = dynamic_programming(filename)
    end_time = time.time()
    execution_time = end_time - start_time


    print("========================================")
    print("EVENT PLANNER - DYNAMIC PROGRAMMING")
    print("========================================\n")

    print(f"Available Time: {max_time}")
    print(f"Available Budget: £{max_budget}\n")

    print("Selected Activities:")
    for a in activities:
        print(f" - {a[0]} ({a[1]} hours, £{a[2]}, enjoyment {a[3]})")

    print("\nTotals:")
    print(f"Total Enjoyment: {happiness}")
    print(f"Total Time Used: {time_used} hours")
    print(f"Total Cost: £{budget_used}")
    
    print(f"\nExecution Time: {execution_time:.6f} seconds")

#runs the program
if __name__ == "__main__":
    final_output(sys.argv[1]) 
