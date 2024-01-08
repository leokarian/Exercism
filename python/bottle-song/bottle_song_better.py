TXT_NUMS = ["no", 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten']
NUM_BOTTLES = ["bottles", "bottle"] + (9 * ["bottles"])


def recite(start: int, take: int = 1) -> list[str]:
    song = []
    for x in range(start, start - take, -1):
        song.append(f"{TXT_NUMS[x].title()} green {NUM_BOTTLES[x]} hanging on the wall,")
        song.append(f"{TXT_NUMS[x].title()} green {NUM_BOTTLES[x]} hanging on the wall,")
        song.append(f"And if one green bottle should accidentally fall,")
        song.append(f"There'll be {TXT_NUMS[x - 1]} green {NUM_BOTTLES[x-1]} hanging on the wall.")
        song.append("")

    return song[:-1]
