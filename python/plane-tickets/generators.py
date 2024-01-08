"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number: int) -> str:
    letters = ['A', 'B', 'C', 'D']
    for x in range(number):
        yield letters[x % 4]


def generate_seats(number: int) -> str:
    row_num = 1
    letters = generate_seat_letters(number)
    let_per_row = 1
    for x in range(number):
        if let_per_row == 5: let_per_row = 1; row_num += 1
        if row_num == 13: row_num += 1
        yield f"{row_num}{letters.__next__()}"
        let_per_row += 1
    

def assign_seats(passengers: list) -> dict:
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: list, flight_id: str) -> str:
    for seat in seat_numbers:
        yield "".join((seat,flight_id)).ljust(12, "0")
