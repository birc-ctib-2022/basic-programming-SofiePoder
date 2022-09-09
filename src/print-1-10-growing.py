
# Print the numbers described in the exercise

numbers = ''

for i in range(1,11):
    if i == 1:
        numbers += str(i)
        print(numbers)
    else:
        numbers += " "
        numbers += str(i)
        print(numbers)


j = []
for i in range(1,11):
    j.append(i)
    print(*j) 
    # the star removes the list [,], 
    # because it prints the aguments within the list instead of printing the list. 
    