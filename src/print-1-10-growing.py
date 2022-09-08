
# Print the numbers described in the exercise
numbers = " "
for i in range(10):
    if i != 10:
        numbers += str(i+1)
        numbers += " "
        print(numbers)
    else:
        numbers += str(i+1)
        