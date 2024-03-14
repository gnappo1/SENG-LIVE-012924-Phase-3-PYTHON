class Pet:
    all = [] #! caching/memoizing

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Names must be at least one char long")
        else:
            self._name = new_name

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be of type string")
        elif not new_breed:
            raise ValueError("Breeds must be at least one char long")
        else:
            self._breed = new_breed

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner_instance):
        from lib.owner import Owner
        if isinstance(owner_instance, Owner):
            self._owner = owner_instance
        else:
            raise TypeError("Owners must be instances of the class Owner")
