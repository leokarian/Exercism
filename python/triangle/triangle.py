def is_valid(sides):
    non_zeros = 0 not in sides
    a, b, c = sides
    return non_zeros and a + b >= c and b + c >= a and a + c >= b
        
    
def equilateral(sides):
    a, b, c = sides
    return is_valid(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides
    return is_valid(sides) and (a == b or a == c or b == c)

    
def scalene(sides):
    a, b, c = sides
    return is_valid(sides) and (a != b and a != c and b != c)