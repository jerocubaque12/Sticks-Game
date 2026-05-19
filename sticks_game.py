"""
This script simulates the sticks game In which you have to pick 
a random stick from a person's fist without seeing them, and if 
you pick the shorter stick, you lose.
"""
import random

#Create list
sticks_list = ["-", "--", "---", "----"]

#Mix previous list
def mix_list(list):
    random.shuffle(list)
    return list

#Ask the user to pick a number
def try_luck():
    attempt = ""
    while attempt not in ["1", "2", "3", "4"]:
        attempt = input("Type any number between 1 and 4: ")
    
    return int(attempt)

#Check the user attempt 
def check_try(list, attempt):
    selection = attempt - 1
    if list[selection] == "-":
        print("You lost!")
    
    else: print("This time you won!, hope you dont have better luck next time")

#Main
mixed_list = mix_list(sticks_list)
attempt = try_luck()

result = check_try(mixed_list, attempt)
