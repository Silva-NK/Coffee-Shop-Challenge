class Coffee:

    def __init__(self, name):
        if type(name) != str or len(name) < 3:
            raise ValueError("Name must be string of at least 3 characters.")
        
        self._name = name

    @property
    def name(self):
        return self._name