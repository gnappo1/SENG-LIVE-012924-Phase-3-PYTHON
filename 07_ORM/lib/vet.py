from helper import Helper
import sqlite3

CONN = sqlite3.connect("resources.db")

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Veterinarian(Helper):
    def __init__(self, name, specialization, location, id=None):
        self._name = name
        self._specialization = specialization
        self._location = location
        self._id = id

    #! Properties

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("names must be strings")
        elif not value:
            raise AttributeError("names must be strings with at least one character")
        self._name = value

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        if not isinstance(value, str):
            raise TypeError("specializations must be strings")
        elif not value:
            raise AttributeError("specializations must be strings with at least one character")
        self._specialization = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("locations must be strings")
        elif not value:
            raise AttributeError("locations must be strings with at least one character")
        self._location = value

    #! Class Methods

    @classmethod
    def create_table(cls):
        """creates the veterinarian table if it doesn't exist"""
        pass

    @classmethod
    def drop_table(cls):
        """drops the veterinarian table if it exists"""
        pass

    @classmethod
    def get_all(cls):
        """returns a list containing all the objects of this class by looking into the db table"""
        pass

    @classmethod
    def create(cls, name, specialization, location):
        """automatically adds a new record into the correspondent db table"""
        pass

    @classmethod
    def find_by(cls, attr, value):
        """finds an existing record via ANY attribute and value. If there are no matches return None"""
        pass
    
    @classmethod
    def find_or_create_by(cls, name, specialization, location):
        """finds an existing record via ANY of the attributes listed above. If there are no matches, then it will CREATE one."""
        pass

    @classmethod
    def vet_with_most_pets(cls):
        """retieve the entire veterinarian object with the most pets patients"""
        pass

    #! Instance Methods

    def save(self):
        """persist/save a vet creating a new row in the veterinarians table"""
        pass
    def update(self):
        """update a vet row in the veterinarians table"""
        pass

    def delete(self):
        """delete a vet row from the veterinarians table"""
        pass

    def add_pet(self, pet_id):
        """associates a vet with a pet given their id"""
        pass

    def remove_pet(self, pet_id):
        """disassociates a vet with a pet given their id"""
        pass