# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

PASSWORD = 'sting' # for now


'''
Description: clean the password string from a junk data
Input: psswd_file - string to be cleaned
Output: psswd_list - list with dict values
'''
def clean_cipher(psswd_file):
    code_flag = False
    psswd_list = []
    splitted_elem = []
    # getting rid of junk 
    psswd_file = psswd_file.replace('{', '')
    psswd_file = psswd_file.replace('}', '')
    psswd_file = psswd_file.replace('\n', '')
    psswd_file = psswd_file.replace('\'','')
    psswd_file = psswd_file.replace(' ','')
    splitted_elem = psswd_file.split(',')
    # removing old keys 
    for part in splitted_elem:
        code_flag = False
        for particle in part:
            if code_flag == False:
                part = part[1:]
            if particle == ':': 
                code_flag = True        
        psswd_list.append(part)
    return psswd_list

'''
Description: reads the passwords data from .csv file
Input: login - username
Output: psswd_list - list with all data from .csv file
'''
def read_psswd(login):
    
    psswd_list = []
    psswd_file = open(f"Users\\{login}\\passwords.csv", "r+")
    for elem in psswd_file:
        psswd_list.append(clean_cipher(elem))  
    psswd_file.close()
    return psswd_list

'''
Description: attaches string to a required dict. key
Input: psswd_str - string with a password
        cnt - variable represents a position
Output: fin_dict - dictionary with input sting
'''
def dict_convertion(psswd_str, cnt):
    fin_dict = {}
    if cnt == 0:
        fin_dict['cipher_text'] = psswd_str
    elif cnt == 1:
        fin_dict['salt'] = psswd_str
    elif cnt == 2:
        fin_dict['nonce'] = psswd_str
    elif cnt == 3:
        fin_dict['tag'] = psswd_str           
    else:
        print("Decryption Error: password dictionary issue")
    return fin_dict

'''
Description: merges dict's in a suitable groups
Input: psswd_list - list with a password info
Output: dict_list - list with grouped dict's
'''
def dict_list(psswd_list):
    dict_list = []
    cnt = 0
    for elem in psswd_list:
        dict_list.append(dict_convertion(elem, cnt))
        if cnt < 3:
            cnt += 1
        else:
            cnt = 0
    for index in range(int(len(dict_list)/4)):
        for ind in range(3):
            dict_list[index].update(dict_list[index+1])
            del(dict_list[index+1])
    return dict_list

def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return str({
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    })


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted

    
if __name__ == "__main__":
    
    pass
        

    