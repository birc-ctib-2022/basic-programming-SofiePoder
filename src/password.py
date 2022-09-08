import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
for character in password:
    if character.isupper() is True:
        is_valid = True
    if character.islower() is True:
        is_valid = True
    if character.isnumeric() is True:
        is_valid = True
    if character in "$#@":
        is_valid = True
    else: is_valid = False
print(is_valid)
