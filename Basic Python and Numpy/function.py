lst = [i for i in range(1, 101)]
def fn(x):
    return x%2==0

for ele in filter(fn, lst):
    print(ele)
    
for el in filter(lambda x:x%2!=0, lst):
    print(el)
    
for ele in filter(lambda x: int(x*0.5)*2 == x, lst):
    print(ele)
    
for ele in map(lambda x: x**2, lst):
    print(ele)
    
for ele in map(lambda x,y: x+y, lst, range(100, 201)):
    print(ele)




# class Car:
#     def __init__(self, m, s, mi):
#         self.model = m
#         self.speed = s
#         self.milage = mi

#     def __repr__(self):
#         return f"{self.model}: Speed={self.speed}, Milage={self.milage}"

# a = Car("A", 150, 18)
# b = Car("B", 160, 15)
# c = Car("C", 150, 20)
# cars = [a, b, c]
# sor = sorted(cars, key=lambda x: (-x.speed, -x.milage))

# for x in sor:
#     print(x)

def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
