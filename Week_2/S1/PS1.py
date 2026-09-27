# P1

# Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

# def lineup(artists, set_times):
#     pass
# Example Usage:

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))
# Example Output:

# {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
# {}

"""
Understand-


Plan -
 


"""
# Implement:

# def lineup(artists , set_times):
#     lineup = {}

#     for i in range(len(artists)):
#         lineup[artists[i]] = set_times[i]

#     return lineup


# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))



# P2

# You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

# def get_artist_info(artist, festival_schedule):
#     pass
# Example Usage:

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  
# Example Output:

# {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
# {'message': 'Artist not found'}


# Understand - 
# input - artist dictionary w/ show time info dictionary
# output - artist festival schedule dictionary
# edge cases - artist does not exist, empty dictionary

# Plan -
# check if artist exists 
# if not then print  {"message": "Artist not found"}
# if artist exists
# print schedule of artist 

# Implement: 

# def get_artist_info(artist, festival_schedule):

#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {"message": "Artist not found"}

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  






# P3


# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

# def total_sales(ticket_sales):
#     pass
# Example Usage:

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))
# Example Output:

# 4500

""" 
Understand - 

Input - a dict of ticket sales
Output - an int of total num of tickets sold
Edge Cases - empty dict, tickets sold is not an int, # of tickets is a large number

Plan -

-check if dict empty
    -return empty dict {}
-check if ticket sales value is int
    -if not int return error
-create total var
-get values from ticket_sales dict and add them together

-return total

"""
# Implement: 


# def total_sales(ticket_sales):
#     if not ticket_sales:
#         return {}

#     for key, val in ticket_sales.items():
#         try:
#             ticket_sales[key] = int(val)
#         except(ValueError, TypeError):
#             ticket_sales[key] = 0

#     total = 0

#     for ticket_type in ticket_sales:
#         total += ticket_sales[ticket_type]

#     return total


# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

# P4

# Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
# Some artists will perform both venues, while others will perform at just one. 
# To ensure that there are no scheduling conflicts, 
# implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. 
# Return a dictionary containing the key-value pairs that are the same in each schedule.

# def identify_conflicts(venue1_schedule, venue2_schedule):
#     pass
# Example Usage:

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))
# Example Output:

# {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}

"""
# Understand - 
# input- 2 dicts w/ schedules
# output - 1 dict w/ scheduling conflicts
# edge cases - 1 or 2 empty dicts, 1 dict is longer than the other

# Plan -

- if venue 1 or venue 2 schedule is empty
    -return error 
- create empty dict to hold time conflicts

- check keys and values in venue 1 and 2 dict
    - if key and value is the same in both
        -add to time conflict dict
-return time conflict dict
"""


# Implement: 

# def identify_conflicts(venue1_schedule, venue2_schedule):

#     if not venue1_schedule or not venue2_schedule:
#         print("Incomplete Schedules")

    

#     schedule_conflict = {}

#     for artist in venue1_schedule:
#         if artist in venue2_schedule:
#             if venue1_schedule[artist] == venue2_schedule[artist]:
#                 schedule_conflict[artist] = venue1_schedule[artist]

#     return schedule_conflict


# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "5:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))




# P5
# As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the highest number of votes. 
# If there is a tie, return any artist with the top number of votes.

# def best_set(votes):
#     pass
# Example Usage:

# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))
# Example Output:

# SZA
# Ethel Cain
# Note: SZA and Ethel Cain would both be acceptable answers for the second example

"""
# Understand - 
input - A dict w/ attendee id # and artist they voted for as a String
output - string of highest voted artist 
edge cases - empty dict, artist name is not a string, attendee number is not an int 

# Plan -

"""


# Implement: 

