#armstrong between 1 to 300
# lower = 1  
# upper = 300 
  
# for num in range(lower,upper + 1):  
#    sum = 0  
#    temp = num  
#    while temp > 0:  
#        digit = temp % 10  
#        sum += digit ** 3  
#        temp //= 10  
#        if num == sum:  
#             print(num)  


#prime num

# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("num is not prime")
#         break
# else: 
#     print("num is prime")



# find the factorial 

# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1,num + 1):
#     factorial = factorial*i
# print(factorial)


#fibonacci
# first = 0
# second = 1
# print(first)
# print(second)
# for x in range(1,9):
#     third = first + second
#     print(third)
#     first,second=second,third


#find num from list

g=[10,20,30]

num=int(input("Enter a number :"))

for e in g:
    if(num==e):
        print("num found")
        break
    else:
        print("num not found")