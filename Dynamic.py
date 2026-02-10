import time
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
def dp_table(activities,n,time):
    #storing  maximum enjoyment and time 
    dp = [[0 for  i in range (time+1)]for  k in range(n+1)] # creates a 2d table with 0s 
           
    for i  in range (1,n+1):  # decide best enjoyement deepending on time 
           for t  in range(time+1):
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
    activities_list = []
    current = [dp[n][time],n,time]
    #print(current)
    #print(dp[current[1]][time], dp[current[1]-1][time])
    activities_list = []
    while current[0] != 0  and current[1]>0:
        #print(current)
        #print(dp[current[1]][current[2]], dp[current[1]-1][current[2]])
        if dp[current[1]][current[2]] > dp[current[1]-1][current[2]]:
            #print(activities[current[1]-1],"sdfghjk")
            activities_list.append(activities[current[1]-1])
            current = [dp[current[1]-1][current[2]-int(activities[current[1]-1][1])],current[1]-1,current[2]-int(activities[current[1]-1][1])]
        else:
            current[1] = current[1]-1
        
    #print(activities_list,"GHJK")
    time_used = 0
    cost = 0
    enjoyment = 0
    for i in range(len(activities_list)):
        time_used += int(activities_list[i][1]) 
        cost += int(activities_list[i][2])
        enjoyment += int(activities_list[i][3])
    return activities_list, enjoyment, cost, time_used, budget,time

def final_output_d(file): # this is the function that creates the final output of the functions. 
    
    start = time.time() # starts the time
    brute_force = dynamic(file) # runs the function and saves the value to a variable 
    end = time.time() # ends the time
    speed = end - start # calculates the time taken for the function to run

    # space to add the dynamic approach:

    start2 = time.time()
    # add the dynamic function here
    end2 = time.time()
    speed2 = end2-start2


    # formatting the output from the brute force algorithm, as it returns an array the indexes of the array can be accessed
    # and they contain all of the necessary information for the final output

    print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    for i in range(len(brute_force[0])):
        print(f" - {brute_force[0][i][0]} ({brute_force[0][i][1]} hours, £{brute_force[0][i][2]}, enjoyment {brute_force[0][i][3]})")
    print('')
    print(f"Total Enjoyment: {brute_force[1]}")
    print(f"Total Time Used: {brute_force[3]} hours")
    print(f"Total Cost: £{brute_force[2]}\n")
    print(f"Execution time: {speed:.4f} seconds")

final_output_d("Lists/input_small.txt")
    
           
           
     
     
