num=1
while num<=10:
    def factorial(n):
        return 1 if (n==1 or n==0) else n * factorial(n - 1);
    print("Factorial of",num,"is",
    factorial(num))
    num=num+1