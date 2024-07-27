def mod(lst):
    print(lst,id(lst))

    lst.append(9)
    
lst=[1,2,3,4,5]
mod(lst)
print(lst,id(lst))