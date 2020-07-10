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

    diction_list = []
    authentication_flag = True
    main_flag = True
    try:
        # Authentation part of the code 
        while authentication_flag:
            what_to_do = input("Type 'registration' or 'authorization':\t")
            if  what_to_do.lower() == "registration":
                while reg.registration():
                    pass
                login = reg.user_check()
                authentication_flag = False
            elif what_to_do.lower() == "authorization":
                login = reg.user_check()
                authentication_flag = False
            
        # encode and decode part of the code
        if reg.login_check:
            while main_flag: 
                what_to_do = input("Type generate to generate password, watch to see them or end to done work.\n")
                if what_to_do.lower() == "generate":
                    psswdl = gen.password_output()
                    psswds = gen.clear_string(psswdl)
                    print(psswds)
                    if input("Type \"store\" if you want to store a new password:\t".lower()) == "store":
                        psswds = encr.encrypt(psswds, encr.PASSWORD)
                        gen.store_password(psswds,login)
                    main_flag = False
                elif what_to_do == "watch":
                    pass_list = encr.read_psswd(login)
                    for elem in pass_list:
                        diction_list.append(encr.dict_list(elem))
                    for elem in diction_list:
                        elem = encr.decrypt(elem[0], encr.PASSWORD)
                        print(bytes.decode(elem))
                    main_flag = False
                elif what_to_do.lower() == "end":
                    break
                else: print("Wrong input, try again")
        else:
            raise BaseException
    except KeyError or IndexError:
        print("Corupted password data...")
    except KeyboardInterrupt:
        print("Dangerous terminating...")
    except:
        print("Program is going to close.")
    print("Good Bye!")
        
