from random import sample


def game_maker(number:int):
    value = str(sample(range(1, 60),number)).replace('[',"").replace(']',"")
    return value
