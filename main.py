'''
Name:       main.py
Author:     DTsebrii
Description:Password generator. Generates passwords according to 
            clients desire
'''
import psswd_gen as gen
import registration as reg
import psswd_encr as encr

if __name__ == "__main__":
    
    try:
        while True:
            what_to_do = input("Type auth to login or reg to create a new user:\n->")
            # Registration Part
            if what_to_do.lower() == "reg":
                My_user = False
                while not My_user:
                    ln = input("Type your login\n->")
                    pwd = input("Type your password\n->")
                    My_user = reg.registration(ln, pwd)
            # Authentification
            elif what_to_do.lower() == "auth":
                My_user = False
                while not My_user:
                    ln = input("Type your login\n->")
                    pwd = input("Type your password\n->")
                    My_user = reg.authentication(ln, pwd)
            what_to_do = input(f"{My_user.name}, what you want to do?\n->")
            # Password Generation
            if what_to_do.lower() == "gen":
                psswd_lst = gen.password_output()
                psswd = ''
                for ent in psswd_lst:
                    psswd += str(ent)
                print(f"Your password is:\n->{psswd}")
                psswd = encr.encrypt(psswd, encr.PASSWORD)
                what_to_do = input("Do you want to store it?\n->")
                if what_to_do.lower() == "yes":
                    gen.store_password(psswd, My_user.name)
                elif what_to_do.lower() == "no":
                    break
            # Old passwords monitoring
            elif what_to_do.lower() == "see":
                pass_list = encr.read_psswd(My_user.name)
                dict_lst = []
                for elem in pass_list:
                    dict_lst.append(encr.dict_list(elem))
                for elem in dict_lst:
                    elem = encr.decrypt(elem[0], encr.PASSWORD)
                    print(bytes.decode(elem))
    except Exception as e:
        print(e)
    finally:
        print("Good Bye!")
