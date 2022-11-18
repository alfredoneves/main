# I created this program because I don't want to convert numeric bases manually neither use some site
# I'm learning English, so I need to practice somewhere


def base_validation():
            """
            function to receive the numeric base
            :return: int of the chosen base
            """
            while True:
                        try:
                                    integer = int(input('type the base for the number (2, 8, 10, 16): '))
                        except Exception as error:
                                    print(error)
                        else:
                                    if str(integer) in "281016":
                                                return integer
                                    else:
                                                continue


def number_validation():
            """
            receives the number and validates it based on the given numeric base
            :return: list if the user used dots and string if not
            """
            while True:
                        num = str(input("type the number to convert: "))
                        # symbol validation
                        for i in range(0, len(num)):
                                    # validation for base 16, letters and some symbols
                                    if (num[i] in "abcdef" and base != 16) or (num[i] in "ghijklmnopqrstuvwxyz,;:-/"):
                                                return "the input is not a number"
                                    # numeric validation
                                    if (num[i] in "23456789" and base == 2) or (num[i] in "89" and base == 8):
                                                return "the input is not a number"
                        # numeric number with dots
                        if "." in num:
                                    numbers = []
                                    temp = ""
                                    for i in range(0, len(num)):
                                                if num[i] != ".":
                                                            temp += num[i]
                                                if num[i] == "." or i == (len(num) - 1):
                                                            numbers.append(temp)
                                                            temp = ""
                                    return numbers
                        # integer number
                        else:
                                    return num


print("supported bases: 2, 8, 10, 16")
print("supported formats: integer numbers or addresses (like IP or MAC). Exp: 123 or 192.168.0.1")
# aHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2luL2FsZnJlZG8tbmV2ZXMtNTYzOThhMjE4Lw==

while True:
            base = base_validation()
            number = number_validation()
            # conversion for each element in the list
            if type(number) == list:
                        base10 = ""
                        base2 = ""
                        base8 = ""
                        base16 = ""
                        for i in number:
                                    temp10 = int(i, base)
                                    base10 += str(temp10) + "."
                                    base2 += str(bin(temp10))[2:] + "."
                                    base8 += str(oct(temp10))[2:] + "."
                                    base16 += str(hex(temp10))[2:] + "."
                        # removes the final dot
                        base10 = base10[0:-1]
                        base2 = base2[0:-1]
                        base8 = base8[0:-1]
                        base16 = base16[0:-1]
            # conversion for a simple number
            else:
                        # [2:] removes the 2 initials that identify the base
                        base10 = int(number, base)
                        base2 = str(bin(base10))[2:]
                        base8 = str(oct(base10))[2:]
                        base16 = str(hex(base10))[2:]
            print(f"base2 = {base2}")
            print(f"base8 = {base8}")
            print(f"base10 = {base10}")
            print(f"base16 = {base16}")
# https://www.linkedin.com/in/alfredo-neves-56398a218/
