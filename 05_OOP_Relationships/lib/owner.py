
class Owner:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all.append(self)

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) >= 2:
            self._first_name = first_name
        else:
            raise ValueError("First name must be a string of at lest 2 chars")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) >= 2:
            self._last_name = last_name
        else:
            raise ValueError("Last name must be a string of at lest 2 chars")
        
    def pets(self):
        from lib.pet import Pet
        #! filter pets by owner
        return [pet for pet in Pet.all if pet.owner == self]