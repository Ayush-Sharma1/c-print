import random
import string

def login_or_register():
    print("Please enter L for Login in and S sign up")
    login = input("Would you like to login or sign up?".upper())
    while True:
        if login == "L":
            while True:
                search_login = input("Please enter your username, then a comma and your password, e.g. username,pass:\n")
                if 2 < len(search_login):
                    if search_login in open("database.txt", "r").read():
                        print("Found")
                        return True
                    else:
                        print("Not Found\nTry again")
                        return login_or_register()
                else:
                    print("Enter valid input")

        elif login == "S":
            print('WE WILL PROVIDE YOU A RANDOMLY GENERATED PASSWORD FOR YOUR ACCOUNT TO MAKE IT THE MORE SECURE')
            username = input("Please choose a username:\n")
            digits = string.digits
            letter_digit_list = list(string.digits + string.ascii_letters)
            # shuffle random source of letters and digits
            random.shuffle(letter_digit_list)
            # first generate 4 random digits
            sample_str = ''.join((random.choice(digits) for i in range(2)))
            sample_str += ''.join((random.choice(letter_digit_list) for i in range(3)))
            aList = list(sample_str)
            random.shuffle(aList)
            password: str = ''.join(aList)
            # Open a file with access mode 'a'
            file_object = open('database.txt', 'a')
            # Append 'hello' at the end of file
            file_object.writelines("{},{}\n\n".format(username, password))
            # Close the file
            file_object.close()
            print("Random Generated Password For Your Account:", password)
            print("Please screenshot your password to remember it")
            return

        else:
            print("Invalid Input, Try again please")
            return login_or_register()


login_or_register()