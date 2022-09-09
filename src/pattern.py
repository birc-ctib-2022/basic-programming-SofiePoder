
# Print the pattern

stars = " "
remove = ''
for i in range(1,11):
    if i <= 5:
        stars = ' '.join(['*']*i)
        print(stars)
    elif i > 5:
        stars = ' '.join(['*']*(i-1))
        print(stars)
