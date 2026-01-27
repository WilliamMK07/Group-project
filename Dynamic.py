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
    time_table = []
    for i in range(len(activities)):
        if any( time_table_row [2] == activities[i][1] for time_table_row in time_table) :
            for item in range(len(time_table)):
                if activities[i][1] == time_table[item][2]:
                    if activities[i][3] > time_table[item][3]:
                        time_table[item] == activities[i]
                        break
        else:
            time_table.append([activities[i][1]]+activities[i])
    print(time_table)
    f.close() # closes the file
    find(activities,budget,time,time_table) 
 
def find(activities,budget,time,time_table):
    if any( time_table_row [0] == str(time) for time_table_row in time_table) :
        print(time)
        for i in time_table:
            if i[2] == str(time) :
                return i[0:]
    else:
        #print(time)
        return find(activities,budget,time-1,time_table)

def max(activities,time,time_table):
    


dynamic("Lists/input_10 (1).txt")