### IMPORTS ###

from tkinter import simpledialog




### GLOBAL VARIABLES ###

props_dict = {}
DEBUG_MODE = True




### FUNCTIONS ###

def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save the properties (dictionary passed as parameter) in a global variable
    props_dict = props

    return 0


def executeChallenge():
    print("Python: starting executeChallenge()")

    # Ask the user for the password
    user_input = askUserForPassword()

    # Get the correct parental key from the properties dictionary (global variable)
    parental_key = props_dict["parental_key"]

    # Get the mode from the properties dictionary (global variable)
    mode = props_dict["mode"]

    # Depending on the mode use the input as key or compare it with the parental key in the properties
    if mode == "parental":
        for i in range (0,2): # Allow 3 tries
            if user_input == parental_key:
                str_key = "\0"
                break
            else:
                user_input = askUserForPassword()

        if user_input != parental_key:
            str_key = "\1"
        else:
            str_key = "\0"

    else:   # Non-parental mode
        str_key = user_input or "\0"

    # Convert the string key into bytes, get its size and put them together in a tuple: the result
    key = bytes(str_key,'utf-8')
    key_size = len(key)
    result = (key, key_size)
    print("Python: chpass result:", result)

    return result


def askUserForPassword():
    return simpledialog.askstring("chpass", "Enter the password:")




### MAIN ###

if __name__ == "__main__":
    midict = {"parental_key": "1234", "mode": "parental"}   # mode can be "parental" o "normal"
    init(midict)
    executeChallenge()
