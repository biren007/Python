def calc(a,b):
    x1=a+b
    x2=a-b
    x3=a*b
    x4=a/b
    return x1,x2,x3,x4
x=calc(10,20)

for i in x:
    print(i,end=",")