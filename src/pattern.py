
# Print the pattern

stars = []
for i in range(1,11):
    if i <= 5:
        stars.append('*')
        print(*stars)
    elif i > 5:
        stars.pop()
        print(*stars)



