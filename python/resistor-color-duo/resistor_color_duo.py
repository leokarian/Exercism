COLOR_LIST = ["black", "brown", "red", "orange",
              "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    return int(str(COLOR_LIST.index(colors[0])) + str(COLOR_LIST.index(colors[1])))
