# Program to check if a number is prime or not

# flag = 0
# n = int(input('Enter whole number to check : '))
# i = 2
# while i <= (n/2):
#     if (n%i) == 0:
#         flag = 1
#         break
#     else:
#         i += 1
    
# if flag == 0:
#     print(n,' is a prime number.')
# elif flag == 1:
#     print(n,' is not a prime number.')


#armstrong number2
# num = int(input("Enter a number: "))

# sum = 0
# n1 = len(str(num))
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** n1
#    temp //= 10

# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


#factorial num

# n = int(input("Enter a number: "))
# num = 1
# while n >= 1:
#     num = num * n
#     n = n - 1
# print(num)



#fibonacci

# n = int(input("enter size: "))
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci series is: ", end = " ")
# while(count <= n):
#   count += 1
#   print(a, end=" ")
#   a = b
#   b = sum
#   sum = a + b

#pelindrome

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")