# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("")


# rows = 5

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("")


# rows = 5
# x = 65
# for i in range(rows):
#     for j in range(i+1):
#         alphabet = chr(x)
#         print(alphabet, end=" ")
#     x += 1
#     print("")


# rows = 5

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
    
#     print("")


rows = 5
k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()