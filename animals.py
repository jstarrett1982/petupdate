# Jackie Starrett
# Purpose:  creation and instantiation of a pets class.  Pet objects are created in main.py.
# The class only requires get and set functions, no methods really.


# Creation of our class and its private properties.
class Animals:
    __ID_number = int
    __pets_name = str
    __age = int
    __owners_name = str
    __animal_type = str

    # Instantiation of our class
    def __init__(self, ID_number, pets_name, age, owners_name, animal_type):
        self.setID_Number(ID_number)
        self.setPets_Name(pets_name)
        self.setAge(age)
        self.setOwners_Name(owners_name)
        self.setAnimal_Type(animal_type)

    # building the get and set functions, with exception handling built-in.
    def getID_Number(self):
        return self.__ID_number

    def setID_Number(self, ID_number: int) -> None:
        try:
            if int(ID_number):
                self.__ID_number = ID_number
        except Exception:
            raise TypeError(f"{ID_number} is not an integer")

    def getPets_Name(self):
        return self.__pets_name

    def setPets_Name(self, pets_name: str) -> None:
        try:
            if str(pets_name):
                self.__pets_name = pets_name
        except Exception:
            raise TypeError(f"{pets_name} is not a string")

    def getAge(self):
        return self.__age

    def setAge(self, age: int) -> None:
        try:
            if int(age):
                self.__age = age
        except Exception:
            raise TypeError(f"{age} is not an integer")

    def getOwners_Name(self):
        return self.__owners_name

    def setOwners_Name(self, owners_name: str) -> None:
        try:
            if str(owners_name):
                self.__owners_name = owners_name
        except Exception:
            raise TypeError(f"{owners_name} is not a string")

    def getAnimal_Type(self):
        return self.__animal_type

    def setAnimal_Type(self, animal_type: str) -> None:
        try:
            if str(animal_type):
                self.__animal_type = animal_type
        except Exception:
            raise TypeError(f"{animal_type} is not a string")
