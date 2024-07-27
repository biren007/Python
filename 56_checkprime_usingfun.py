
def prime(x, y):
	
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				print(i)
	

starting_range = 0
ending_range = int(input("enter range :"))
lst = prime(starting_range, ending_range)
print(lst)
