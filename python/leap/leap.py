def leap_year(year):
    by_four = (year % 4 == 0)
    by_hundred = (year % 100 == 0)
    by_4hun = (year % 400 == 0)
    return (by_four and (not by_hundred)) or (by_hundred and by_4hun)
