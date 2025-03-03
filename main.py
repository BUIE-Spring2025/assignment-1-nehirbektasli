def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    if not 1 <= num <= 3999:
        print("Input must be an integer from 1 to 3999. Please enter a valid input.")
    roman_num = ""
    decimal = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    for i in [1000, 100, 10, 1]:
        if num // i == 0:
            continue
        elif num // i == 9:
            roman_num += decimal[i] + decimal[10*i]
        elif num // i == 4:
            roman_num += decimal[i] + decimal[5*i]
        else:
            roman_num += (num // i) * decimal[i]
        num = num % i
    return roman_num
