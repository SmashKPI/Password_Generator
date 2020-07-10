#!/usr/bin/env python3
'''
Name:   psswd_gen
Author: DTsebrii
Description: Library allows user to use a functions to 
                create a random passwords
'''
import random 
import string
import os

# Global Variables
list_low_case = list(string.ascii_lowercase)  # List of uppercase alphabet
list_up_case = list(string.ascii_uppercase)  # List of lower case of an alphabet
list_symbols = list("~!@#$%^&*()_+><?")
# Password lenght 
HIGH_HIGH = 20
HIGH_LOW = 16
LOW_HIGH = 15
LOW_LOW = 10

'''
Author:         DTsebrii
Description:    Generate list of random symbols
Input:          password - the list of password;
                low_lim/high_lim - low and high 
                limit of pssword lenght
Output:         None
'''
def password_creation(password,low_lim,high_lim):
    
    for index in range(random.randint(low_lim,high_lim)):
        index = random.randint(0,3)
        if index == 1:
            password.append(random.randint(0,9))
        elif index == 2:
            password.append(list_low_case[random.randint(0,(len(list_low_case)-1))])
        elif index == 3:
            password.append(list_up_case[random.randint(0,(len(list_up_case)-1))])
        elif index == 0:
            password.append(list_symbols[random.randint(0,(len(list_symbols)-1))])

'''
Author:         DTsebrii
Description:    Convert a password list to a string
Input:          list1 - password list;
                string1 - result string
Output:         string1 - final password
'''
def clear_string(list1):
    
    string1 = ""
    for elem in list1:
        string1 += str(elem)
    return string1     

'''
Author:         DTsebrii
Description:    Collect a decision about the strenght of a password
Input:          string_inp - Level of password difficulty
Output:         string_inp 
'''    
def difficulty_pick():

    string_inp = ""
    print("Type \"strong\" if you want to generate a strong password,")
    print("or type \"easy\" if you want to have an easy one.")
    while(string_inp != "strong" and string_inp != "easy"):
        string_inp = input("Desicion:\t")
        if (string_inp != "strong" and string_inp != "easy"):
            print("Invalid value, try again.")
            
    return string_inp  

'''
Author:         DTsebrii
Description:    Ask user about password level and generate 
                an appropriate password
Input:          None
Output:         password_list - the list with passwords'
                elements
'''  
def password_output():

    password_list = []
    dif_lvl = difficulty_pick()
    if dif_lvl.lower() == "strong":
        password_creation(password_list, HIGH_LOW, HIGH_HIGH)
    elif dif_lvl.lower() == "easy":
        password_creation(password_list, LOW_LOW, LOW_HIGH)
    else:
        print("Wrong difficulty level")
    return password_list

'''
Author:         DTsebrii
Description:    Ask user about password level and generate 
                an appropriate password
Input:          None
Output:         password_list - the list with passwords'
                elements
''' 
def store_password(password_string,login):

    if os.path.exists(f"Users\\{login}\\passwords.csv"):
        print("Idk why, but you r here")
        psswd_file = open(f"Users\\{login}\\passwords.csv", "a+")
    else:
        print("I am here")
        psswd_file = open(f"Users\\{login}\\passwords.csv", "w+")
    psswd_file.write(password_string+"\n")
    psswd_file.close()


    
if __name__ == "__main__":

    pass
