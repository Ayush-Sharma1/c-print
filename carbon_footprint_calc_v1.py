# carbon footprint calculator
import time
total_household_footprint = 0
total_travel_footprint = 0
total_newspaper_footprint = 0
total_tin_and_can_footprint = 0
total_carbon_footprint = 0

time.sleep(2)
print("RUNNING CARBON FOOTPRINT CALCULATOR...")
# this function validates float input number
def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            if float_input > 0:
                return float_input
            elif float_input <= 0:
                print("An input must be a positive integer, try again please.")
        except ValueError:
            print("Please input a floating point number")


# household footprint
def get_household_footprint():
    time.sleep(2)
    print(" ")
    print("HOUSEHOLD FOOTPRINT")
    household_list = ["Electricity in kWh", "Gas in m^3", "oil in L"]
    e = validate_float("How much do you use monthly on {}\n".format(household_list[0]))
    g = validate_float("How much do you use monthly on {}\n".format(household_list[1]))
    o = validate_float("How much do you use monthly on {}\n".format(household_list[2]))
    global total_household_footprint
    total_household_footprint = e * 105 + g * 105 + o * 113
    print("Your total household footprint is {}".format(total_household_footprint))
    return total_household_footprint


# CAR/TRAVEL FOOTPRINT
def get_travel_footprint():
    print(" ")
    print("CAR/TRAVEL FOOTPRINT")
    travel_list = ["What is your yearly kilometers on your car? ",
                   "Number of flights you’ve taken in the past year (4 hours or less)",
                   "Number of flights you’ve taken in the past year (4 hours or more)"]
    m = validate_float("{}\n".format(travel_list[0]))
    f1 = validate_float("{}\n".format(travel_list[1]))
    f2 = validate_float("{}\n".format(travel_list[2]))
    global total_travel_footprint
    total_travel_footprint = (m * 0.79) + (f1 * 1140) + (f2 * 4100)
    print("Your total Car/Travel footprint is {}".format(total_travel_footprint))
    return total_travel_footprint


# MISC footprint

def get_misc_newspaper_footprint():
    while True:
        print("MISC FOOTPRINT")
        print("Please enter y for YES and n for NO")
        newspaper = input("Do you recycle newspaper?")
        if newspaper == "y":
            print("Great!")
            break
        elif newspaper == "n":
            global total_newspaper_footprint
            total_newspaper_footprint += 184
            break


def get_tin_and_can_footprint():
    while True:
        print("Please enter y for YES and n for NO")
        newspaper = input("Do you recycle Tins and cans ?")
        if newspaper == "y":
            print("Great!")
            break
        if newspaper == "n":
            global total_tin_and_can_footprint
            total_tin_and_can_footprint += 166
            break
    return


def get_total_carbon_footprint():
    print("TOTAL CARBON FOOTPRINT")
    global total_carbon_footprint
    total_carbon_footprint = (total_household_footprint + total_travel_footprint + total_newspaper_footprint +
                              total_tin_and_can_footprint)
    print("YOUR TOTAL CARBON FOOTPRINT IS {}".format(total_carbon_footprint))
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


get_household_footprint()
get_travel_footprint()
get_misc_newspaper_footprint()
get_tin_and_can_footprint()
get_total_carbon_footprint()
---------------------
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
    while True:
        try:
            float_input = float(input(prompt))
            if float_input > 0:  # this code makes sure the value is >0, so no -ve values are entered
                return float_input
            elif float_input <= 0:  # if users enters a -ve or 0 value, they need to try again as that's not +ve integer
                print("An input must be a positive integer, try again please.")
        except ValueError:
            print("Please input a floating point number")


# this function asks user for their household info and then calculates their household footprint
def get_household_footprint():
    print("\033[33m")  # changes colour to blue
    time.sleep(1)
    print(" ")
    print("HOUSEHOLD FOOTPRINT")
    print("\033[36m")
    time.sleep(.7)
    household_list = ["Electricity in kWh", "Gas in m^3", "oil in L"]
    time.sleep(.5)
    e = validate_float("How much do you use monthly on {}\n".format(household_list[0]))
    time.sleep(.5)
    g = validate_float("How much do you use monthly on {}\n".format(household_list[1]))
    time.sleep(.5)
    o = validate_float("How much do you use monthly on {}\n".format(household_list[2]))
    global total_household_footprint
    total_household_footprint = e * 105 + g * 105 + o * 113
    time.sleep(.5)
    print("Calculating your household footprint...")
    time.sleep(.5)
    print("Your total household footprint is {}".format(total_household_footprint))
    return total_household_footprint


# this function asks user for their travel info and then calculates their travel footprint
def get_travel_footprint():
    time.sleep(1)
    print(" ")
    print("CAR/TRAVEL FOOTPRINT")
    time.sleep(.7)
    travel_list = ["What is your yearly kilometers on your car? ",
                   "Number of flights you’ve taken in the past year (4 hours or less)",
                   "Number of flights you’ve taken in the past year (4 hours or more)"]
    time.sleep(.4)
    yearly_km = validate_float("{}\n".format(travel_list[0]))
    time.sleep(.4)
    flights_1 = validate_float("{}\n".format(travel_list[1]))
    time.sleep(.4)
    flights_2 = validate_float("{}\n".format(travel_list[2]))
    global total_travel_footprint
    total_travel_footprint = (yearly_km * 0.79) + (flights_1 * 1140) + (flights_2 * 4100)
    time.sleep(.5)
    print("Calculating your car/travel footprint...")
    time.sleep(.5)
    print("Your total Car/Travel footprint is {}".format(total_travel_footprint))
    return total_travel_footprint


# this function asks user if they recycle paper and then calculates their misc footprint
def get_misc_newspaper_footprint():
    while True:
        time.sleep(1)
        print(" ")
        print("MISC FOOTPRINT")
        time.sleep(.7)
        print("Please enter y for YES and n for NO")
        time.sleep(.3)
        newspaper = input("Do you recycle newspaper or any other sort of paper?")
        if newspaper == "y":
            break
        elif newspaper == "n":
            global total_newspaper_footprint
            total_newspaper_footprint += 184
            break


# this function asks user if they recycle tins and cans and then calculates their misc footprint
def get_tin_and_can_footprint():
    while True:
        time.sleep(1)
        print(" ")
        print("Please enter y for YES and n for NO")
        time.sleep(.3)
        newspaper = input("Do you recycle Tins and cans ?")
        if newspaper == "y":
            break
        if newspaper == "n":
            global total_tin_and_can_footprint
            total_tin_and_can_footprint += 166
            break
    return


# this function adds all the values together to get the users total C footprint, it also prints further info
def get_total_carbon_footprint():
    time.sleep(1)
    print(" ")
    print("TOTAL CARBON FOOTPRINT")
    time.sleep(.3)
    global total_carbon_footprint
    total_carbon_footprint = (total_household_footprint + total_travel_footprint + total_newspaper_footprint +
                              total_tin_and_can_footprint)
    print("YOUR TOTAL CARBON FOOTPRINT IS {}".format(total_carbon_footprint))
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

