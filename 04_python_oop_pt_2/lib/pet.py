#!/usr/bin/env python3
# Class Attributes and Methods

# import ipdb
from decorator_profiler import measure_performance

class Pet:
    # ✅ Define a class attribute (total_pets) and set it to 0
    # __slots__= ('_name', '_age', '_temperament', '_breed', '_owner')
    all = []
    # What happens with our instances when we add a class attribute?

    def __init__(self, *args, **kwargs):
        # In the following lines, by simply typing 'self.name = '
        # python will check if on the instance there are any setter properties
        # why setters? because there is an = after the word 'name'
        # if not, it will set the attribute manually and call it 'name'
        for k, v in kwargs.items():
            setattr(self, k, v)
        type(self).all.append(self)

    # Using Property to control the behavior of attributes
    @property
    def name(self):
        print("Inside the name property getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Inside the name property setter")
        if not isinstance(new_name, str):
            raise TypeError("Value must be a string")
        elif len(new_name) <= 2:
            raise ValueError("Value must be a string with more than 2 chars")
        else:
            self._name = new_name

    # @name.deleter
    # def name(self):
    #     del self._name

    # name = property(None, set_name)
    @property
    def breed(self):
        print("Inside the breed property getter")
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        print("Inside the breed property setter")
        if not isinstance(new_breed, str):
            raise TypeError("Value must be a string")
        elif len(new_breed) <=2:
            raise ValueError("Value must be an int greater than 0")
        else:
            self._breed = new_breed

    # breed = property(get_breed, set_breed)
    @property
    def age(self):
        print("Inside the age property getter")
        return self._age

    @age.setter
    def age(self, new_age):
        print("Inside the age property setter")
        if not isinstance(new_age, int):
            raise TypeError("Value must be an int")
        elif new_age < 0:
            raise ValueError("Value must be an int greater or equal to 0")
        else:
            self._age = new_age

    # age = property(get_age, set_age)
    @property
    def owner(self):
        print("Inside the owner property getter")
        raise AttributeError('Privacy concern, you cannot see me!')
    @owner.setter
    def owner(self, new_owner):
        print("Inside the owner property setter")
        if not isinstance(new_owner, str):
            raise TypeError("Value must be an string")
        elif len(new_owner) <= 2:
            raise ValueError("Value must be an string greater than 2")
        else:
            self._owner = new_owner

    # owner = property(get_owner, set_owner)
    @property
    def temperament(self):
        print("Inside the temperament property getter")
        raise AttributeError('Privacy concern, you cannot see me!')

    @temperament.setter
    def temperament(self, new_temperament):
        print("Inside the temperament property setter")
        if not isinstance(new_temperament, str):
            raise TypeError("Value must be a string")
        elif len(new_temperament) < 2:
            raise ValueError("Value must be an string greater or equal to 2")
        else:
            self._temperament = new_temperament

    # temperament = property(get_temperament, set_temperament)

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')

    @classmethod
    @measure_performance
    def find_by_name(cls, name_to_find):
        matches = [pet for pet in cls.all if pet.name.lower() == name_to_find.lower()]
        return matches[0] if matches else None

    @classmethod
    @measure_performance
    def find_by_name_2(cls, name_to_find):
        for pet in cls.all:
            if pet.name.lower() == name_to_find.lower():
                return pet
        return False

    @classmethod
    @measure_performance
    def find_by_name_3(cls, name_to_find):
        return next((pet for pet in cls.all if pet.name.lower() == name_to_find.lower()), None)
    
    @classmethod
    def find_by(cls, attr_name, attr_value):
        pass

fido = Pet(name="Fido", age=2, breed="pug", temperament="docile", owner="Matteo")
milo = Pet(name="Milo", age=2, breed="pug", temperament="docile", owner="Matteo")
print('done')
