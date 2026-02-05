from itertools import chain, combinations
import time

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

def dynamic(file):
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
    #print(activities)
    f.close() # closes the file
    dp = (dp_table(activities,n,time) )
    #print(dp)
    return(dp_best(dp,activities,n,time,budget))

#dp Table   attempt 1 
#, how it works  creates a table  with enjoyment and time   and adds  activitys for best enjoyment  for every  number of activies  for every maxing time 
#  for example  0 activities the best enjoyement will be 0  for each ax time ,  1 activity the best enjoyment will be tdecided best on the  available time  and so forth 
def dp_table(activities,n,time):# creates table used to calculate best happiness in given time
    #storing  maximum enjoyment and time 
    dp = [[0 for  i in range (time+1)]for  k in range(n+1)] # creates a 2d table with 0s 
           
    for i in range (1,n+1):  # decide best enjoyement deepending on time 
           for t in range(time+1):
            activity_time = int(activities[i-1][1]) # gets time for current activity 
            activity_enjoyment =  int(activities[i-1][3]) # gets enjoyment for current  activity 

            if activity_time <= t: #  compares  activity time to  the  current time limit  and gives two options 
                #   option one takes the activity and  adds the enjoyment 
                dp[i][t] = max(dp[i-1][t],dp[i-1][t-activity_time] + activity_enjoyment)#  finds the highest 

                #store which activity 
                
            else:
                dp[i][t] = dp[i-1][t] #  option 2 skips  the activity and go to the next one 
    # for i in range(len(dp)-1,0,-1):
    #     print(i,dp[i])
    return dp

def dp_best(dp,activities,n,time,budget):
    activities_list = []# empty list to store activities used
    current = [dp[n][time],n,time] # current postion used in table stored as [enjoyment of square,row,column]
    #print(current)
    #print(dp[current[1]][time], dp[current[1]-1][time])
    while current[0] != 0: # if square on is empty stop
        #print(current)
        #print(dp[current[1]][current[2]], dp[current[1]-1][current[2]])
        #compares if square in current position has a higher enjoyment value than square in row above
        if dp[current[1]][current[2]] > dp[current[1]-1][current[2]]: 
            # if it does it means the activity was used
            activities_list.append(activities[current[1]-1]) #adds activity corresponding to row in table to list
            current = [dp[current[1]-1][current[2]-int(activities[current[1]-1][1])],current[1]-1,current[2]-int(activities[current[1]-1][1])]
            #changes value stored in current
        else:
            current[1] = current[1]-1
            #sets row in column to one less
        
    #print(activities_list,"GHJK")
    time_used = 0 # used to see how much time was usd in chosen path
    cost = 0 # used to calculate the total cost
    enjoyment = 0 # used to calculate totoal happiness
    for i in range(len(activities_list)): # loop through each activity used
        time_used += int(activities_list[i][1]) # add time on to total
        cost += int(activities_list[i][2]) # add cost on to total
        enjoyment += int(activities_list[i][3]) # add happiness on to total
    return activities_list, enjoyment, cost, time_used, budget,time

def final_output(file): # this is the function that creates the final output of the functions. 
    
    start = time.time() # starts the time
    brute_force = brute_combo(file) # runs the function and saves the value to a variable 
    end = time.time() # ends the time
    speed = end - start # calculates the time taken for the function to run

    # space to add the dynamic approach:

    start2 = time.time()
    dynamic_programming = dynamic(file)
    end2 = time.time()
    speed2 = end2-start2


    # formatting the output from the brute force algorithm, as it returns an array the indexes of the array can be accessed
    # and they contain all of the necessary information for the final output
    print('======================================== \nEVENT PLANNER - RESULTS \n========================================\n')
    print(f"Input File: {file}")
    print(f"Available Time: {brute_force[5]}")
    print(f"Available Budget: {brute_force[4]}\n")

    print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    for i in range(len(dynamic_programming[0])):
        print(f" - {dynamic_programming[0][i][0]} ({dynamic_programming[0][i][1]} hours, £{dynamic_programming[0][i][2]}, enjoyment {dynamic_programming[0][i][3]})")
    print('')
    print(f"Total Enjoyment: {dynamic_programming[1]}")
    print(f"Total Time Used: {dynamic_programming[3]} hours")
    print(f"Total Cost: £{dynamic_programming[2]}\n")
    print(f"Execution time: {speed2:.4f} seconds")

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

final_output("Lists/input_10.txt")