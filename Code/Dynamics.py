import time
import sys
def read_input(filename):

    with open(filename, "r") as f:
        n = int(f.readline())

        time_budget = f.readline().split()
        max_time = int(time_budget[0])
        max_budget = int(time_budget[1])

        activities = []
        for _ in range(n):
            name, t, c, h = f.readline().split()
            activities.append((name, int(t), int(c), int(h)))

    return activities, max_time, max_budget


def dynamic_programming(filename):
    activities, max_time, max_budget = read_input(filename)

    # DP table: dp[time][budget] = max enjoyment
    dp = [[0 for _ in range(max_budget + 1)]
          for _ in range(max_time + 1)]

    # To reconstruct chosen activities
    chosen = [[[] for _ in range(max_budget + 1)]
              for _ in range(max_time + 1)]

    for name, t, c, h in activities:
        for time_left in range(max_time, t - 1, -1):
            for budget_left in range(max_budget, c - 1, -1):
                new_value = dp[time_left - t][budget_left - c] + h

                if new_value > dp[time_left][budget_left]:
                    dp[time_left][budget_left] = new_value
                    chosen[time_left][budget_left] = (
                        chosen[time_left - t][budget_left - c]
                        + [(name, t, c, h)]
                    )

    # Find best result
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

# RUN THE PROGRAM
if __name__ == "__main__":
    print_results(sys.argv[1]) 
