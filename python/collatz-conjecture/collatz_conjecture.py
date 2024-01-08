def collatz(number):
    if number == 1: return 1
    if number % 2 == 0: return collatz(number / 2) + 1
    else: return collatz(number * 3 + 1) + 1
 

    
def steps(number):
    if number >= 1:
        return collatz(number) - 1
    else:
        raise ValueError("Only positive integers are allowed")