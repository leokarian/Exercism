def is_armstrong_number(number):
    num_str = str(number)
    power = len(num_str)
    tot = 0
    for x in num_str:
        tot += pow(int(x),power)
    return number == tot
    
