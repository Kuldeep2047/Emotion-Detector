# i=1
# while i<=3:
#     try:
#         a = int(input("a : "))
#         b = int(input("b : "))
#         print(a/b)
#         print(i)
#     except:
#         print("Error")
    
    
#     i += 1






# i=1
# while i<=3:
#     try:
#         a = int(input("a : "))
#         b = int(input("b : "))
#         print(a/b)
#     except ZeroDivisionError:
#         print("Wrong input b")
#     except ValueError:
#         print("Wrong input value")
#     except Exception:
#         print("Error...")
#     i +=1




def fn(a,b):
    print("In fn")
    try:
        if b != 0:
            return a/b
        else:
            raise Exception("b should be non zero")
    except:
        print("b should be non-zero")    
    print("Out fn")

# fn(10,10)
# print("Bye Main")


print("Hi main")
try:
    a = fn(10,0)
    print("div :",a)
except Exception as e:
    print("Error !!", e)
print("Bye Main")
