from random import randint

def lot() -> int:                    # random from 1 to 2
    x = randint(1, 50)
    if x % 2 == 0:
        return 1
    else:
        return 2