import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        y = []
        for letter in x: 
            y.append(hex(ord(letter)))
        encoding = ''.join(y)
        print(encoding)

    case "decode":
        # Implement the decoding here
        for letter in x:
            new = x.split('0x')
            string = ''.join(new[1:])
            integer = int(string, base = 16)
        decoding = chr(integer)
        print(decoding)

