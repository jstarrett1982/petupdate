# Jackie Starrett
# Purpose: This program accesses information from my pets SQL database.
# It organizes my SQL data and reads it through cursor to create pet objects from my Animals class.
# As the database information is read through cursor, the pet objects are also stored in a list of dictionaries.

# I had done pip install on pymysql, so now I can import cursors to read through my sql pets database.
import pymysql.cursors

# This pulls the information my creds file and animals files.  Make sure to enter your true information into this file.
from creds import *
from animals import Animals

# creating my empty list of dictionaries variable.  I will add to this while reading through my database.
listOfDictionaries = []


# Ultimately, this function shows the list of our pet names and their ID numbers.


def connectPrint():
    # Creating a handle to connect to the database.  The variables come from the creds file.  Dummy variables are entered due to submitting in GitHub.
    # Please enter your actual user name, password, and host name into the creds file to run this program.
    try:
        myConnection = pymysql.connect(host=hostname,
                                       user=username,
                                       password=password,
                                       db=database,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)

    except AttributeError as e:
        print(f"make sure you filled in your information in creds file. {e}")
        print()
        exit()

    # Now that we are connected, execute a query
    #  and do something with the result set.
    try:
        with myConnection.cursor() as cursor:

            print("PET LIST")

            # This function below will read our database, merge the tables, create pet objects, and print off the pet menu
            try:
                # this statement below picks the data from the appropriate columns in the pets, owners, and types tables.
                # Certain column names are re-named with the "as" statement.  The selected columns are joined into a new table.
                sqlSelect = """
             select pets.id as ID_number, 
             pets.name as pets_name, pets
             .age, owners.name as owners_name, 
             types.animal_type from pets join
               owners on pets.owner_id=owners.id 
               join types on pets.animal_type_id = types.id
             """
                # cursor reads through our sql select statement
                cursor.execute(sqlSelect)

                # This reads through each row of the merged table and creates an Animal object for each row.
                # Each object (row) gets placed into our listOfDictionaries.
                # Lastly, the loop prints the ID_number and pet name from each animal object.  This is the pet list menu generated for the user.
                for row in cursor:
                    pet = Animals(row["ID_number"], row["pets_name"], row["age"], row["owners_name"],
                                  row["animal_type"])
                    listOfDictionaries.append(row)
                    print(pet.getID_Number(), pet.getPets_Name())
            except ImportError:
                print("looks like we couldn't access your modules")

            print()
            myConnection.close()

    # If there is an exception, show what that is
    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        print()


def options():
    status = 0
    while status == 0:

        menu = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet?   ")
        if menu.upper() == "Q":
            print()
            print("Thanks for stopping by.  Have a nice day!")
            status = 1
            quit()
        elif menu.upper() == "C":
            connectPrint()
            print()
            petLoop()
            break
        elif menu.upper() == "E":
            print()
            petEditLoop()
            break
        else:
            print()
            print("Please enter C, Q, or E")
            status = 0
            print()

def connectUpdateName():

    try:
        myConnection2 = pymysql.connect(host=hostname,
                                        user=username,
                                        password=password,
                                        db=database,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)

    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        print()
        exit()

    # Now that we are connected, execute a query
    #  and do something with the result set.
    # try:
    with myConnection2.cursor() as cursor:
    # ==================

    # NOTE: We are using placeholders in our SQL statement
    #  See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html

        sqlUpdateName = """
            update
              pets
            set
              pets.name = %s
            where
              id = %s  ; """

        cursor.execute(sqlUpdateName, ('newName', petChoice))

        myConnection2.commit()

        myConnection2.close()

def connectUpdateAge():
    try:
        myConnection3 = pymysql.connect(host=hostname,
                                        user=username,
                                        password=password,
                                        db=database,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)

    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        print()
        exit()

    # Now that we are connected, execute a query
    #  and do something with the result set.
    # try:
    with myConnection3.cursor() as cursor:
    # ==================

    # NOTE: We are using placeholders in our SQL statement
    #  See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html

    sqlUpdateAge = """
            update
              pets
            set
              pets.age = %s
            where
              id = %s  ;
            """

    # Execute update
    cursor.execute(sqlUpdateAge, ('newAge', petChoice))

    myConnection3.commit()
    myConnection3.close()

def petEditLoop():
    status = 0
    petChoice = 0
    connectPrint()
    while status == 0:
        petChoice = input("please enter a pet ID number to edit their name or age")

        if str.isnumeric(petChoice):
            for item in listOfDictionaries:
                if int(petChoice) != item["ID_number"]:
                    continue

                if int(petChoice) == item["ID_number"]:
                    print()
                    print("You have chosen to edit", item["pets_name"])
                    print()
                    newName = input("New name: [ENTER == no change]   ")
                    if newName != "":
                       connectUpdateName()
                    elif newName == "":
                        item["pets_name"] = newName
                        connectUpdateName()
                    newAge= input("New age:  [ENTER == no change]    ")
                    if str.isnumeric(newAge):
                        connectUpdateAge()

                    elif newAge == "":
                        item["age"] = newAge
                        connectUpdateAge()
                    else:
                        print("please enter a number")
                        print()
                        newAge= input ("New age:  [ENTER = no change   ")

                    print("here is the updated pet list:")
                    print()
                    connectPrint()

                # This catches any numbers input by the user that aren't pet ID numbers. It reposts the pet menu for the user to view again.
                else:
                    print()
                    print("try a different number please")
                    connectPrint()

            # This allows the user to quit if entering q or Q. It then prints a closing message.
        elif petChoice.upper() == "Q":
            print()
            print("looks like you are done")
            programStatus = 1
            quit()

            # This catches any user input that is a string other than Q or q, and gives an appropriate message.
            # Then, it re-posts the pet menu for the user to view.
        else:
            print()
            print("please enter a number, not a string")
            print()
            connectPrint()
            print()
            petChoice = input("please enter a pet ID number to edit their name or age")



# The loop below asks for user input in the form of the pet ID number from the printed menu.
def petLoop():
    programStatus = 0
    while programStatus == 0:
        try:
            choice = input("enter a pet's ID number to obtain their information, press Q to end the program:  ")

            # the first test checks to see if the user input an integer.
            if str.isnumeric(choice):

                # the loop below searches the list of dictionaries containing our pet info for the pet ID input by user.
                # It continues reading the list even if the number isn't found and prints the pet information only when the appropriate pet is reached.
                # then, it breaks out of the loop.
                for item in listOfDictionaries:
                    if int(choice) != item["ID_number"]:
                        continue

                    if int(choice) == item["ID_number"]:
                        print()
                        print("This pet is a", (item["animal_type"]), ".  The pet's name is",
                              (item["pets_name"]), "and", (item["owners_name"]), "is their owner. They are",
                              (item["age"]), "years old.")
                        print()
                        options()


                # This catches any numbers input by the user that aren't pet ID numbers. It reposts the pet menu for the user to view again.
                else:
                    print()
                    print("try a different number please")
                    connectPrint()


            # This allows the user to quit if entering q or Q. It then prints a closing message.
            elif choice.upper() == "Q":
                print()
                print("looks like you are done")
                programStatus = 1

            # This catches any user input that is a string other than Q or q, and gives an appropriate message.
            # Then, it re-posts the pet menu for the user to view.
            else:
                print()
                print("please enter a number, not a string")
                print()
                connectPrint()




        # Last chance to catch any problems.
        except Exception as e:
            print("looks like something happened")

    # print("the program has ended")


connectPrint()
petLoop()
