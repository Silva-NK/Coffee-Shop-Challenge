class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str or not (1 <= len(name) <= 15):
            raise ValueError("Name must be string between 1 and 15 characters.")
        
        self._name = name