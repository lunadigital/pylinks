class Parameter:
    def __init__(self, value):
        self.value = value
        self.link = None

    def __get__(self, instance, owner):
        return self.value

    def __str__(self):
        return str(self.value)

    def set_value(self, value):
        if type(value) == type(self.value):
            self.value = value