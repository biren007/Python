#1

# n=5
# i = 1
# while i <= n :
#     j = 1
#     while j <= i:
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1


#2

# n=5
# i = 1
# while i <= n :
#     j = n
#     while j >= i:
#         print("*", end = " ")
#         j -= 1
#     print()
#     i += 1


#3

# n = 5
# k = 1
# i = 1
# while i <= n :
#     j = 1
#     while j <= i:
#         print(k, end = " ")
#         j += 1
#         k += 1
#     print()
#     i += 1


#4

# num=5
# count=1
# while count<=num:
#     i=0
#     while i<=(num-count):
#         print(" ",end=" ")
#         i=i+1
#     i=0
#     while i<(2*count-1):
#         print("*",end=" ")  
#         i=i+1
#     print()
#     count=count+1


#5
n=5
asc=65
i = 1
while i <= n :
    j = 1
    while j <= i:
        print(chr(asc), end = " ")
        j += 1
    print()
    i += 1
    asc=asc+1
