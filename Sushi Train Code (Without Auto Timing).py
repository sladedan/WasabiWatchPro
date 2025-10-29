#allow python to acess time
#this is only accurate as of 1970 however as the sushi train runs off current time this is fine.
import time

# make a varialble (a way to store, label and reuse infomation) called 'sushi menu'
# create a list ('sushi_menu') that contains the names of different sushi dishes.
# the list wil hold the items in order
# each line is a new string (made up of letters, numbers symbols and spaces withing quotation marks)
# the '[]' start and end the list
sushi_menu = [
    "Salmon avocado roll",
    "Tuna cucumber roll",
    "California roll",
    "Tempura prawn roll",
    "Spicy tuna roll",
    "Chicken katsu roll",
    "Vegetarian roll",
    "Salmon nigiri",
    "Tuna nigiri",
    "Kingfish nigiri",
    "Eel (unagi) nigiri",
    "Prawn nigiri",
    "Tamago (sweet omelette) nigiri",
    "Salmon sashimi",
    "Tuna sashimi",
    "Kingfish sashimi",
    "Edamame",
    "Gyoza (dumplings)",
    "Karaage chicken",
    "Agedashi tofu",
    "Tempura (prawns, vegetables)",
    "Seaweed salad",
    "Miso soup",
    "Mochi ice cream",
    "Green tea cheesecake"
    ]

# create a empty dictionary that stores barcode numbers and times
# dictinary stores related data in pairs of a key (barcode number) and a value (time since reset)
plates = {}

# starting a loop that will run until the prgram is quit.
# this will ensure that the plate and time data is kept until the program is quit so the times can be reset and the sushi data can be retreived for the entirty of the session (for example the dinner service at the restraunt.
while True:

# ask for a data value. this will be the input. this would occur as a barcode goes under the scanner and there is a data input into the system (Plate Number).
# this will ensure that every time this data is entered (the barcode) it will bring up the assosiated information until it is reset. (The program is quit) 
    barcode = input("Scan a barcode: ")


# ask what to do with this barcode. ths gives a menu and allocates a response to a number so the user doesnt have to type out the message everytime they use it.
# function 1 and 2 does the same thing as it just resets the time for this barcode to 0 seconds. I have created two serpeate functions for this as from a user point of view they are different physical function of adding a plate to the train for the first time, or changing what type of dish the plate is assigned to.
# it then asks for another input. This inpud decides what to do with the previous input. (Whet the operator wants to know/do with the plate)
    print("What would you like to do?")
    print("1 - Add to train/reset plate")
    print("2 - See how long it has been on the train")
    choice = input("Enter 1 or 2: ")

#'==' meants equal to. (Check if the left side is equal to the right)
# Therefore "if this condition is true, do the following".
# for i, sushi in enumerate(sushi_menu, start=1): → Loops through the sushi list and gives each item a number starting at 1.
# i → The number of the item in the list.
#sushi → The name of the sushi.
#emulate means 'to copy the function or behavior of something else through software' which is a function I needed to further research when creating this code.
    if choice == "1":
        print("Choose the sushi type by number:")
        for i, sushi in enumerate(sushi_menu, start=1):
            print(i, "-", sushi)
#int() → Converts the user input (string) into a number so it can be used as an index.
#Checks if the number entered is valid.
#plates[barcode] = (sushi_type, time.time()) → Stores the sushi type and the current time in the dictionary using the barcode as the key.
#time.time() → Gives the current time in seconds.
        sushi_choice = int(input("Enter number: "))
        if 1 <= sushi_choice <= len(sushi_menu):
            sushi_type = sushi_menu[sushi_choice - 1]
            plates[barcode] = (sushi_type, time.time())
            print("Added", sushi_type, "to the train.\n")
        else:
            print("Invalid choice.\n")
            

#Calculates how long a plate has been on the train by subtracting the saved time from the current time.
#plates[barcode] → Returns the tuple (sushi_type, start_time), which we can unpack into two variables.
    elif choice == "2":
        if barcode in plates:
            sushi_type, start_time = plates[barcode]
            time_on_train = int(time.time() - start_time)
            print("This is a", sushi_type, "plate and has been on the train for", time_on_train, "seconds.\n")
        else:
            print("This barcode is not on the train yet.\n")
#else → If none of the above conditions are true, do this.
    else:
        print("Invalid option.\n")
