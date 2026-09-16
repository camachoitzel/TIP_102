#P1
# 
#  Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".

# def welcome():
# 	pass
# Example Usage:

# welcome()
# Example Output:

# Welcome to The Hundred Acre Wood!

# SOLUTION:

# def welcome():
#     print("Welcome to The Hundred Acre Wood!")


# welcome()



#P2

# Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

# def greeting(name):
# 	pass
# Example Usage:

# greeting("Michael")
# greeting("Winnie the Pooh")
# Example Output:

# Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
# Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.


# SOLUTION:

# def greeting(name):

#     print(f'Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.')

# greeting("Michael")
# greeting("Winnie the Pooh")



#P3

# Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

# Character	Catchphrase
# "Pooh"	"Oh bother!"
# "Tigger"	"TTFN: Ta-ta for now!"
# "Eeyore"	"Thanks for noticing me."
# "Christopher Robin"	"Silly old bear."
# If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"

# def print_catchphrase(character):
# 	pass
# Example Usage

# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)
# Example Output:

# "Oh bother!"
# "Sorry! I don't know Piglet's catchphrase!"


# understand:
# input = string of character name
# output = Pooh, tigger, eeyore, christopher catchphrase (strings)

# plan:

# edgecase = if empty, 




# SOLUTION:

# def print_catchphrase(character):

#     character = character.lower()


#     if(character == 'pooh'):
#         print("Oh bother!")

#     elif(character == 'tigger'):
#         print("TTFN: Ta-ta for now!")


#     elif(character == 'eeyore'):
#         print("Thanks for noticing me.")


#     elif(character== 'Christopher Robin'):
#         print("Silly old bear.")


#     else:
#         print("Sorry! I don't know" +  ' ' + character + "'s catchphrase!")



# character = "Pooh"
# print_catchphrase(character)

# character_2 = "Sonic"
# print_catchphrase(character_2)






#P4


# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

# def get_item(items, x):
# 	pass
# Example Usage

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# get_item(items, x)

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# get_item(items, x)
# Example Output:

# "roo"
# None

# SOLUTION:

# def get_item(items, x):

#     size = len(items)

#     if x > size - 1:
#         return None

#     return items[x] 

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))





# P5


# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

# def sum_honey(hunny_jars):
# 	pass
# Example Usage

# hunny_jars = [2, 3, 4, 5]
# sum_honey(hunny_jars)

# hunny_jars = []
# sum_honey(hunny_jars)
# Example Output:

# 14
# 0


# SOLUTION:

# def sum_honey(hunny_jars):

#     sum = 0

#     for num in hunny_jars:
#         sum += num

#     return sum

# hunny_jars = [2, 3, 4, 5]

# print(sum_honey(hunny_jars))

# hunny_jars_2 = [12,7,31,5]
# print(sum_honey(hunny_jars_2))








#P6

# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

# def doubled(hunny_jars):
# 	pass
# Example Usage

# hunny_jars = [1, 2, 3]
# doubled(hunny_jars)
# Example Output:

# [2, 4, 6]

# SOLUTION:

# def doubled(hunny__jars):

#     doubled_hunny = []

#     for num in hunny__jars:
#         doubled_hunny.append(num *2)

#     return doubled_hunny

# hunny__jars = [1,2,3]
# print(doubled(hunny__jars))



# P7

# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.

# def count_less_than(race_times, threshold):
# 	pass
# Example Usage

# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# count_less_than(race_times, threshold)

# race_times = []
# threshold = 4
# count_less_than(race_times, threshold)
# Example Output:

# 3
# 0

# SOLUTION:

def count_less_than(race_times, threshold):
    count = 0

    if not race_times:
        return 0

    for num in race_times:
        if num < threshold:
            count += 1

    return count