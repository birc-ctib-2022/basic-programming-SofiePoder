
# Print the pattern

stars = " "
stars2 = " "
for i in [1,2,3,4,5]:
    if i != 1:
        stars += " *"
    else:
        stars += "*"
    print(stars)
for i in [4,3,2,1]:
    if i != 1:
        stars2 += " *"
    else:
        stars2 += "*"
    print(stars2)
