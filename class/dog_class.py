class Dog:
    def __init__(self, name, age):
        """init name and age attributes"""
        self.name = name
        self.age = age

    
    def sit(self):
        print(f"{self.name} is now sitting")

    def rollover(self):
        print(f"{self.name} loves to roll over!")

my_dog = Dog('kelly', 3)
print(f"my dog name is {my_dog.name}")
print(f"my dog is {my_dog.age}")

my_dog.sit()
my_dog.rollover()


