class Dog:
    info = "Dogs and some atributes"

    def __init__ (self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

dog1 = Dog("Capsi", "Mixed", 12)
dog2 = Dog("Pusia", "Mixed", 16)
dog3 = Dog("Burek", "Husky", 8)

print(dog1.name, "\n", dog1.breed, "\n", dog1.age)
print(dog2.name, dog2.breed, dog2.age)
print(dog3.name, dog3.breed, dog3.age)


