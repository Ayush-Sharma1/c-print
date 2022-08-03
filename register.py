# registering
import random
import string


def register():
    print('WE WILL PROVIDE YOU A RANDOMLY GENERATED PASSWORD FOR YOUR ACCOUNT TO MAKE IT THE MORE SECURE')
    username = input("Please enter a valid username.\n")

    digits = string.digits
    letter_digit_list = list(string.digits + string.ascii_letters)
    # shuffle random source of letters and digits
    random.shuffle(letter_digit_list)

    # first generate 4 random digits
    sample_str = ''.join((random.choice(digits) for i in range(4)))

    # Now create random string of length 6 which is a combination of letters and digits
    # Next, concatenate it with sample_str
    sample_str += ''.join((random.choice(letter_digit_list) for i in range(6)))
    aList = list(sample_str)
    random.shuffle(aList)
    final_str = ''.join(aList)
    # Open a file with access mode 'a'
    file_object = open('database.txt', 'a')
    # Append 'hello' at the end of file
    file_object.write("Username:{}\n".format(username))
    file_object.write("Password:{}\n".format(final_str))
    file_object.write("______________________\n")
    # Close the file
    file_object.close()
    print("Random Generated Password For Your Account:", final_str)


register()