import random

def go(human_num: int, max_c: int) -> int:
    global memo
    if human_num == 0:
        return random.randint(1, 28)
    elif len(memo) < 10:
        memo.append(human_num)       
        return random.randint(0, 28)
    else:
        memo.append(human_num)
        return int(*random.choices(memo, k=1))
memo = []