import sys
args=sys.argv[1:]
print(args)

for a in args:
    x=int(a)
    if(x%2==0):
        sum+=x
print("sum of even = ",sum)