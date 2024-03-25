class Dog:
    legs = 4

    def __init__(self):
        self.name = "Milo"
        self.color = "Brown"

    def get_dog_name(self): #instance method
        print(self.name)

    @classmethod  # decorator required to access class methods.
    def get_legs_count(cls):   # class method
        print(cls.legs)

    @staticmethod
    def general_information():
        print("Beware of Dogs")

d1=Dog()

d1.get_dog_name()

d1.get_legs_count()
Dog.get_legs_count()
Dog.general_information()


