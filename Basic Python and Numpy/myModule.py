print("Hello ! Welcome to my Module")
a =10
b = "Hello"

class A:
    pass

def fn():
    a,b = 10,20
    c =a+b
    return c

print("Bye Execution")
# print(__name__)

if __name__ == '__main__':
    print(fn())