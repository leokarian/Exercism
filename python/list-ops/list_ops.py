def append(list1, list2):
    return list1 + list2


def concat(lists):
    nlist = []
    for list in lists:
        nlist += list
    return nlist


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum([1 for x in list])


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    result = initial
    for i in list:
        result = function(result, i)
    return result


def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)


def reverse(list):
    return [list[index] for index in range(length(list)-1, -1, -1)]
