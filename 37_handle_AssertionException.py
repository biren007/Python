x=int(input("Enter Num:"))
try:
    assert x>0
    print("You entered : ",x)
except AssertionError:
    print("Invalid input")