#!/usr/bin/env python3
'''
Name:       registration.py
Author:     DTsebrii
Description:Module to create an accounts system
'''

import os 
import psswd_encr as encr


done_flag = True

'''
Name:       create_user
Description:contain data from file in a list
            type variable
Input:      None
Output:     user_list - list with users data
'''
def create_user(login):

    if not os.path.exists(f"Users\\{login}"):
        os.makedirs(f"Users\\{login}")
    

'''
Name:       get_file
Description:contain data from file in a list
            type variable
Input:      None
Output:     user_list - list with users data
'''
def get_file():
    
    if not os.path.exists("Users\\user_list.csv"):
       user_file = open("Users\\user_list.csv", "w+")
    else:
        user_file = open("Users\\user_list.csv", "r")
    user_list = []
    for char in user_file:
        user_list.append(char)
    user_file.close()
    return user_list 

'''
Name:       make_passwd
Description:creates a pair of username and ciphered 
            password
Input:      user_list - string got from .csv file 
Output:     tulp_list - list of username and 
            password ciphered and stored in dictionary
'''
def make_passwd(user_list, login, passwd):
    global login_check
    login_check = False
    dict_list = []
    tulp_list = []
    cnt = 0
    #for elem in user_list:
    user_list = eval(user_list)
    user_list = list(user_list)
    user_list[1] = encr.clean_cipher(user_list[1])
    for part in user_list[1]:
        dict_list.append(encr.dict_convertion(part, cnt))
        if cnt < 3:
            cnt += 1
        else:
            cnt = 0
    for index in range(int(len(dict_list)/4)):
        for ind in range(3):
            dict_list[index].update(dict_list[index+1])
            del(dict_list[index+1])
    user_list[1] = dict_list[0]
    tulp_list = user_list
    if tulp_list[0] == login:
        temp_pass = encr.decrypt(tulp_list[1], encr.PASSWORD)
        if bytes.decode(temp_pass) == passwd:
            print(f"Welcome, {login}")
            login_check = True
            return
        else:
            print("Wrong password")
            return
    return 
'''
Name:       user_check
Description:check the entered user login among user
            list
'''
def user_check():
    
    tulp_list = []
    dict_store = {}
    # Getting the Login and Password data
    login = input("Enter your login:\t")
    passwd = input("Enter your password:\t")
    user_list = get_file()
    for elem in user_list:
        make_passwd(elem, login, passwd)
    return login

'''
Name:       registration
Description:Enter the new user data in the user list file
Input:      None
Output:     False if registration succeeded 
            True if registration failed
'''
def registration():
    user_tulp = ()
    user_list = get_file()
    login = input("Login:\t")
    passwd = input("Password:\t")
    conf_pass = input("Retype Password:\t")
    if passwd == conf_pass and login not in user_list:
        print(f"User {login} has been registered")
        create_user(login)
        user_file = open("Users\\user_list.csv", "a+")
        passwd = encr.encrypt(passwd, encr.PASSWORD)
        user_tulp = (login, passwd)
        user_file.write(str(user_tulp)+'\n')
        return False
    else:
        print("Login name has already existed or passwords did not match")
        return True

if __name__ == "__main__":
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    