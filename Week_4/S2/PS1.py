"""
Problem 1: Planning Your Daily Work Schedule
Your day consists of various tasks, each requiring a certain amount of time. 
To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. 
You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, 
write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, 
and False otherwise.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Example Output:
True
True
False

Understand:
Iterate through the list of integers.
Create For loop
In the for loop make an if statement
Return True if the tasks matches an available timeslot 
Create left and right
Left starts at begining of the list
Right starts at list -1

Plan:




"""
#Implement
def find_task_pair(task_times, available_time):
    left = 0
    right = len(task_times) - 1
    total = 0
    
    while left < right:
        total = task_times[left] + task_times[right]
        if total == available_time:
            return True
        elif total < available_time:
            left = left + 1
        elif total > available_time:
            right = right - 1
    
    return total == available_time
        

# Example Usage:

'''
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
'''

"""
Problem 2: Minimizing Workload Gaps
You work with clients across different time zones and often have gaps between your work sessions. 
You want to minimize these gaps to make your workday more efficient. 
You have a list of work sessions, each with a start time and an end time. 
Your task is to find the smallest gap between any two consecutive work sessions.

Given a list of tuples where each tuple represents a work session with a start and end time 
(both in 24-hour format as integers, e.g., 1300 for 1:00 PM), 
write a function to find the smallest gap between any two consecutive work sessions. 
The gap is measured in minutes.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
Example Output:

60
30
15

UNDERSTAND:
Input - tuple of start and end times for work sessions
Output - smallest gap between each session in minutes
Edge Cases - empty tuple, equal amount for the gap

PLAN:
-Create function to convert to minutes 
-variable for gap 
- loop through the tuple for start, end, in work_sessions
    - add start and end time variables
    - convert times to minutes by multiplying by 60
    - compare the start time of the next tuple with the end time of the last 
        - update the gap var to that difference 
    

"""
def convert_min(work_sessions):
    new_tuple = []
    for start, end, in work_sessions:
        start = start * 60 
        end = end * 60
        new_tuple.append((start, end))
    
    return new_tuple
        
    
def find_smallest_gap(work_sessions):
    gap = 0
    min_tuple = convert_min(work_sessions)
    
    for i in range(1, len(min_tuple)):
        
    


# Example Usage:

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
#print(find_smallest_gap(work_sessions))

print(convert_min(work_sessions))

#work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
#print(find_smallest_gap(work_sessions_2))

#work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
#print(find_smallest_gap(work_sessions_3))




"""
Problem 3: Expense Tracking and Categorization
You travel frequently and need to keep track of your expenses. 
You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. 
At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), 
write a function that returns the expense categories and the total expenses for each category. 
Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def calculate_expenses(expenses):
  pass
Example Usage:

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))
Example Output:

({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')

"""