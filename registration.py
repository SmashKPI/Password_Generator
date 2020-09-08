#!/usr/bin/env python3
'''
Name:       registration.py
Author:     DTsebrii
Description:Module to create control the 
    registration process. Module creates
    user object with unique UID and allows
    either to create new or authenticate 
    the old one
'''

import os 
import psswd_encr as encr

list_path = "Users\\User_List.csv"

class User:
    '''
    : Represents each user
    : Variables:
        name
    '''
    list_path = "Users\\User_List.csv"
    def __init__(self, nm):
        
        self.name = nm  # User name 
        
        self.ID = self.get_uid()  # User ID (to authentification)
        self.path = f"Users\\{self.name}"  # Users directory
        self.create_user()  # Create directory
        self.passwords = self.get_passwords()  # To show passwords
        
        
    def get_uid(self):
        '''
        : Moves through the file and checkes the UID
        : Output:
            False if User does not exist
            cnt if User does exist 
        '''
        cnt = 0 # ID value
        try:
            user_list = open(list_path, 'r')
            for entity in user_list.readlines():
                cnt += 1
                if entity == f"{self.name}\n":
                    user_list.close()
                    return cnt
            user_list.close()
            cnt == 0
            return cnt
        except Exception as e:
            print(e)
            user_list.close()
            return False
            
    def get_passwords(self):
        '''
        : Stores all saved passwords
        : Output:
            list of passwords 
        '''
        psswd_list = []
        if not os.path.exists(f'Users\\{self.name}\\Passwords.csv'):
            user_psswd = open(f'Users\\{self.name}\\Passwords.csv', 'w+')
        else:
            user_psswd = open(f'Users\\{self.name}\\Passwords.csv', 'r')
        for entity in user_psswd.readlines():
            entity = entity.replace("\n", "")
            psswd_list.append(entity)
        user_psswd.close()
        return psswd_list
    
    
    def create_user(self):
        '''
        Name:       create_user
        Description:contain data from file in a list
                    type variable
        Input:      None
        '''
        if not os.path.exists(self.path): os.makedirs(self.path)
        if not os.path.exists(self.list_path):
            user_nm = open(self.list_path, 'w+')
        else:
            user_nm = open(self.list_path, "a")
            user_nm.write(f"{self.name}\n")
        user_nm.close()
            
# EO class User::


def get_file():
    '''
    Name:       get_file
    Description:
        contain data from file in a list
        type variable
    Output:     user_list - list with users data
    '''
    if not os.path.exists(list_path):
       user_file = open(list_path, "w+")
    else:
        user_file = open(list_path, "r")
    user_list = []
    for char in user_file:
        user_list.append(char)
    user_file.close()
    return user_list 

def shadows(user, psswd):
    '''
    : Store user password in shadows file
    : Input:
        user class object
    '''
    if not os.path.exists("Data"): os.makedirs("Data") 
    if not os.path.exists("Data\\Shadows.csv"):
        sh_file = open("Data\\Shadows.csv", 'w+')
    else: sh_file = open("Data\\Shadows.csv", 'a')
    sh_file.write(f"{encr.encrypt(psswd, encr.PASSWORD)}\n")
    print("Credentials has been written")
    sh_file.close()

def registration(user_name, user_password):
    '''
    : Create an user class and type down required info
    : Output:
        My_user - user class object
    '''
    login_check = False
    while True:
        user_list = get_file()
        for entity in user_list:
            entity = entity.replace("\n", "")
            if entity == user_name:
                login_check = True
                break
        if not login_check:
            My_user = User(user_name)
            shadows(My_user, user_password)
            return My_user
        else:
            print("Wrong credentials. Try again")
            return False

def authentication(ln, pwd):
    '''
    : Cehckes whenever input credentials are valid
    : Input:
        user - user class variable 
        ln - login 
        pwd - password
    '''
    global list_path
    cnt = 0
    # Open password and login files
    sh_file = open("Data\\Shadows.csv", 'r')
    sh_list = [entity.replace("\n", "") for entity in sh_file.readlines()]
    sh_file.close()
    ln_file = get_file()
    for entity in ln_file:
        cnt += 1
        if ln == entity.replace("\n", ""):
            password = sh_list[cnt - 1]
            password = encr.clean_cipher(password)
            password = encr.dict_list(password)
            password = encr.decrypt(password[0], encr.PASSWORD)
            password = password.decode("utf-8")
            if pwd == password:
                My_user = User(ln)
                print(f"Welcome {ln}!")
                return My_user
            else:
                print("Wrong credentials")
                return False
           
    

if __name__ == "__main__":
    pass
    
