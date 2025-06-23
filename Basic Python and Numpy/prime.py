
# n = 2
# while n <= 100:
#     p = True
#     i = 2
#     while i*i <= n:
#         if n%i == 0:
#             p =False
#             break
#         i+=1
#     if p:
#         print(n, end=" ")
#     n += 1

# l = [10,20,30,40]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])


s = "The sky is blue"
print(" ".join(s.split()[::-1]))