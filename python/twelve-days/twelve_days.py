ORDINAL = ["none", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
           "eleventh", "twelfth"]
PHRASE = ["-", "and a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ",
          "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ",
          "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
          "twelve Drummers Drumming, "]


def recite(start_verse, end_verse):
    full_text = []
    for i in range(start_verse, end_verse + 1):
        text = f"On the {ORDINAL[i]} day of Christmas my true love gave to me: "
        for p in range(i, 0, -1):
            if i == p == 1:
                text += PHRASE[p][4:]
            else:
                text += PHRASE[p]
        full_text.append(text)
    return full_text
