# fully working code

import time
import random
import string

# global variables for carbon footprint calc
total_household_footprint = 0
total_travel_footprint = 0
total_newspaper_footprint = 0
total_tin_and_can_footprint = 0
total_carbon_footprint = 0


# this function validates float input number
def validate_float(prompt):
    # this code makes sure the user can only input values that are number greater than or equal to 0
    valid = True
    while valid:
        try:
            float_input = float(input(prompt))
            if float_input >= 0:  # this code makes sure the value is >0, so no -ve values are entered
                return float_input
            elif float_input <= 0:  # if users enters a -ve or 0 value, they need to try again as that's not +ve integer
                print("An input must be a positive integer, try again please.")
        except ValueError:
            print("Please input a floating point number")


# this function asks user for their household info and then calculates their household footprint
def get_household_footprint():
    print("\033[33m")  # changes colour to orange
    time.sleep(1)
    print("HOUSEHOLD FOOTPRINT")
    print("\033[36m")  # changes colour to cyan
    time.sleep(.7)
    household_list = ["Electricity in kWh", "Gas in m^3", "oil in L"]
    time.sleep(.2)
    electricity = validate_float("How much do you use monthly on {}\n"
                                 " :".format(household_list[0]))
    time.sleep(.2)
    gas = validate_float("How much do you use monthly on {}\n"
                         " :".format(household_list[1]))
    time.sleep(.2)
    oil = validate_float("How much do you use monthly on {}\n"
                         " :".format(household_list[2]))
    global total_household_footprint
    total_household_footprint = electricity * 105 + gas * 105 + oil * 113
    time.sleep(.5)
    print("\033[35m")  # changes colour to magenta
    print("Calculating your household footprint...")
    time.sleep(.5)
    print("Your total household footprint is {}".format(total_household_footprint))
    return total_household_footprint


# this function asks user for their travel info and then calculates their travel footprint
def get_travel_footprint():
    print("\033[33m")  # changes colour to orange
    time.sleep(1)
    print(" ")
    print("CAR/TRAVEL FOOTPRINT")
    print("\033[36m")  # changes colour to cyan
    time.sleep(.7)
    travel_list = ["What is your yearly kilometers on your car?\n" + " :",
                   "Number of flights you’ve taken in the past year (4 hours or less)\n" + " :",
                   "Number of flights you’ve taken in the past year (4 hours or more)\n" + " :"]
    time.sleep(.2)
    yearly_km = validate_float("{}".format(travel_list[0]))
    time.sleep(.2)
    flights_1 = validate_float("{}".format(travel_list[1]))
    time.sleep(.2)
    flights_2 = validate_float("{}".format(travel_list[2]))
    global total_travel_footprint
    total_travel_footprint = (yearly_km * 0.79) + (flights_1 * 1140) + (flights_2 * 4100)
    time.sleep(.5)
    print("\033[35m")  # changes colour to magenta
    print("Calculating your car/travel footprint...")
    time.sleep(.5)
    print("Your total Car/Travel footprint is {}".format(total_travel_footprint))
    return total_travel_footprint


# this function asks user if they recycle paper and then calculates their misc footprint
def get_misc_newspaper_footprint():
    # runs the code until its broken (incase a typo has occurred or the input does not = if or elif (y & n)
    while True:
        print("\033[33m")  # changes colour to orange
        time.sleep(1)
        print(" ")
        print("MISC FOOTPRINT")
        time.sleep(.7)
        print("Please enter y for YES and n for NO")
        print("\033[36m")  # changes colour to cyan
        time.sleep(.2)
        newspaper = input("Do you recycle newspaper or any other sort of paper?\n" + " :")
        newspaper = newspaper.lower()
        if newspaper == "y":
            break  # breaks the while True loop
        elif newspaper == "n":
            global total_newspaper_footprint
            total_newspaper_footprint += 184
            break  # breaks the while True loop


# this function asks user if they recycle tins and cans and then calculates their misc footprint
def get_tin_and_can_footprint():
    # runs the code until its broken (incase a typo has occurred or the input does not = if or elif (y & n)
    valid = True
    while valid:
        time.sleep(.2)
        print(" ")
        tins_cans = input("Do you recycle Tins and cans ?\n" + " :")
        tins_cans = tins_cans.lower()
        if tins_cans == "y":
            break  # breaks the while True loop
        if tins_cans == "n":
            global total_tin_and_can_footprint
            total_tin_and_can_footprint += 166
            break  # breaks the while True loop
    return


# this function adds all the values together to get the users total C footprint, it also prints further info
def get_total_carbon_footprint():
    time.sleep(1)
    print(" ")
    print("\033[33m")  # changes colour to orange
    print("TOTAL CARBON FOOTPRINT")
    time.sleep(.3)
    global total_carbon_footprint
    total_carbon_footprint = (total_household_footprint + total_travel_footprint + total_newspaper_footprint +
                              total_tin_and_can_footprint)
    print("\033[35m")  # changes colour to magenta
    print("YOUR TOTAL CARBON FOOTPRINT IS {}".format(total_carbon_footprint))
    print("\033[32m")
    if total_carbon_footprint < 7257:
        print("You Have a Low Carbon Footprint, You do not Need To Make Changes, Good Job!")
    elif total_carbon_footprint < 10000:
        print("You Have an Average Carbon Footprint, You may wish to lower your Carbon Footprint")
        print("Here are some ways you can reduce it...")
        with open("reduce_average.txt", encoding="utf-8") as f:
            contents = f.read()
            print(contents)
    else:
        print("You Have a High Carbon Footprint, You should seriously reconsider making changes to your lifestyle "
              "in order to decrease your carbon footprint")
        print("Here are some ways you can reduce it...")
        with open("reduce_over_10000.txt", encoding="utf-8") as f:
            contents = f.read()
            print(contents)


# the user can log in or sign in
def login_or_register():
    time.sleep(1)
    print(" ")
    print("Please enter L for Login in and S sign up")
    time.sleep(.3)
    login_signup = input("Would you like to login or sign up?\n" + " :")
    login_signup = login_signup.upper()
    # runs the code until its broken, helps the user decide if they wanna login or signup
    valid = True
    while valid:
        if login_signup == "L":
            valid = True  # A endless loop since the user might input wrong login many times
            while valid:
                time.sleep(.3)
                search_login = input("Please enter your username, then a comma and your password, e.g. username,pass\n"
                                     + " :")
                if 2 < len(search_login):
                    if search_login in open("database.txt", "r").read():
                        print("\033[32m")
                        print("Found")
                        print("Hello, welcome back to C-PRINT")
                        return valid
                    else:
                        print("\033[31m")
                        print("Not Found\nTry again")
                        print("\033[96m")
                        return login_or_register()
                else:
                    print("Enter valid input")
        elif login_signup == "S":
            time.sleep(.3)
            print(" ")
            print('WE WILL PROVIDE YOU A RANDOMLY GENERATED PASSWORD FOR YOUR ACCOUNT TO MAKE IT THE SECURE')
            time.sleep(.3)
            username = input("Please choose a username:\n" + " :")
            digits = string.digits
            letter_digit_list = list(string.digits + string.ascii_letters)
            # shuffle random source of letters and digits
            random.shuffle(letter_digit_list)
            # generates 2 random digits
            password_str = ''.join((random.choice(digits) for i in range(2)))
            # generates 3 random letters
            password_str += ''.join((random.choice(letter_digit_list) for i in range(3)))
            password_list = list(password_str)
            random.shuffle(password_list)
            password: str = ''.join(password_list)
            # Open a file with access mode 'a'
            file_object = open('database.txt', 'a')
            # Append the username and pass at the end of file
            file_object.writelines("{},{}\n\n".format(username, password))
            # Close the file
            file_object.close()
            time.sleep(.3)
            print("Random Generated Password For Your Account:", password)
            print("Please screenshot your password to remember it")
            print("Hello {}!".format(username))
            time.sleep(.3)
            print(" ")
            return
        else:
            print("Invalid Input, Try again please")
            return login_or_register()


# after each option in the menu has run, this will print and ask the user whether they wanna go to menu or end program
def ask_menu_or_end():
    # runs the code until its broken (incase a typo has occurred or the input does not = if or elif
    valid = True
    while valid:
        try:
            print("\033[36m")
            ask = input("Type 'm' to go back to menu and type 'e' to end the program\n"
                        " :")  # if user type 'menu
            print("\033[36m")
            ask = ask.lower()
            if ask == 'm':
                menu()
            elif ask == 'e':
                print("Thanks for using C-PRINT, SEE YOU NEXT TIME!")
                break  # breaks the loop
        except TypeError:
            print("invalid input try again")


print("\033[96m")  # changes colour to blue
print("WELCOME TO C-print")  # greets the user and welcomes them to the app
login_or_register()  # runs the login/register code


# HOME PAGE, the user can select which page they wish to go to
def menu():
    print("\033[33m")  # changes colour
    print("Please select the corresponding number and press ENTER.")
    options = input("| 1. Calculate your Carbon Footprint\n"
                    "| 2. How to Reduce Your Carbon Emissions\n"
                    "| 3. About Us and Contact Us\n"
                    "| 4. Websites for further info\n"
                    "| 5. End App\n" + " :")

    # the user picked the carbon footprint calc, therefore this options runs that calculator
    if options == '1':
        print("CARBON FOOTPRINT CALCULATOR")
        get_household_footprint()
        get_travel_footprint()
        get_misc_newspaper_footprint()
        get_tin_and_can_footprint()
        get_total_carbon_footprint()
        ask_menu_or_end()

#  the user wanted to know how they can reduce their footprint, therefore this options opens a txt file to provide info
    elif options == '2':
        print(" ")
        print("HOW REDUCE YOUR CARBON FOOTPRINT?")
        print("\033[97m")
        with open("how_reduce_C_footprint", encoding="utf-8") as f:
            contents = f.read()
            print(contents)
            ask_menu_or_end()


    # the user wanted to know more about 'C-PRINT', therefore this options opens a txt file with all the info about us
    elif options == '3':
        with open("aboutus.txt", encoding="utf-8") as f:
            contents = f.read()
            print(contents)
            ask_menu_or_end()

    # the user wanted more websites they could visit, therefore this options opens a txt file which has more websites
    elif options == '4':
        with open("websites", encoding="utf-8") as f:
            contents = f.read()
            print(contents)
            ask_menu_or_end()

    # the user wanted to end the app, the app then prints a statement and ends the app
    elif options == '5':
        print("THANK YOU FOR USING C-PRINT!")
        pass

    # If the user enters a value that is NOT a no. between 1-6, an error will show up
    else:
        print("INVALID, TRY AGAIN PLEASE!")
        print(" ")
        time.sleep(.3)
        return menu()


menu()
