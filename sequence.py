n = int(input("Enter the length of the sequence: ")) # Do not change this line
sum = 0 
first = 1
second = 2
third = 3
for i in range(1, n+1):    
    if i == 1:
        print(i)
    elif i == 2:
        print(i)
    elif i == 3:
        print(i)
    else:
        sum = first + second + third
        first = second
        second = third
        third = sum
        print(sum)



