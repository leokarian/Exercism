TXT_NUMS = ["no", 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten']
NUM_BOTTLES = ["bottles", "bottle"] + (9 * ["bottles"])


def recite(start: int, take: int = 1) -> list[str]:
    lines = ["ACTUAL green N_BOT hanging on the wall,",
             "ACTUAL green N_BOT hanging on the wall,",
             "And if one green bottle should accidentally fall,",
             "There'll be ONE-LESS green NA_BOT hanging on the wall."]
    song = []
    for x in range(start, start - take, -1):
        for i in lines:
            song.append(i.replace("ACTUAL", TXT_NUMS[x].title()).
                        replace("ONE-LESS", TXT_NUMS[x-1]).
                        replace("N_BOT", NUM_BOTTLES[x]).
                        replace("NA_BOT", NUM_BOTTLES[x-1]))
        if x > (start - take + 1):
            song.append("")

    return song
