
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
    