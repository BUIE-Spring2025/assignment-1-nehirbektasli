def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    roman_num = ""
    decimal = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    for i in [1000, 100, 10, 1]:
        if not 1 <= num <= 3999:
            print("Invalid input. Please enter an integer between 1 and 3999.")
            break
        x = num // i
        if x == 0:
            continue
        elif x == 9 or x == 4:
            roman_num += decimal[i] + decimal[(x + 1) * i]
        elif x < 4:
            roman_num += x * decimal[i]
        else:
            roman_num += decimal[5*i] + (x - 5) * decimal[i]
        num = num % i
    return roman_num
