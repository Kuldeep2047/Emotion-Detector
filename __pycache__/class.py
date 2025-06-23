# class Person:
#     def introduce(s):
#         print(s)
#         print(f"Hi ! I am {s.name}")
        
# p1 = Person()
# # print(p1)

# p1.name = "Kuldeep"
# p1.age = 20
# print(p1.name)

# p1.introduce()

# class Dog:
#     def __init__(s,name,breed):
#         s.name = name
#         s.breed = breed
#     def bark(s):
#         print(f"Dog name is {s.name} and  says Hello!")

# d1=Dog("Sheru", "xyz")
# d1.bark()


class Car:
    def __init__(self, model, speed, milage):
        self.model = model
        self.speed = speed
        self.milage = milage

    def __len__(self):
        print('In length dunder')
        return self.milage

    def __add__(self, oth):
        return Car(self.model, oth.speed, self.milage + oth.milage)

    def __str__(self):
        return f"model: {self.model} speed: {self.speed} mileage: {self.milage}"
    
    def __gt__(self, other):
        return self.speed > other.speed


c1 = Car('Rolls Royce', 200, 30)
c2 = Car('defender', 350, 20)

# if c1 > c2:
#     print(f"{c1.model} is faster")
# else:
#     print(f"{c2.model} is faster")

print(c1>c2)