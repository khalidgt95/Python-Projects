def infinite_sequence():
    num: int = 0

    while True:
        yield num
        num += 1

def send_input_to_generator(bet, amount):
    while True:
        amount += bet
        bet = yield amount