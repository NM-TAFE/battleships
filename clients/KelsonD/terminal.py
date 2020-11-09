



class GameBoard:
    def __init__(self, moves_dictionary):
        for num in range(1,11):
            moves_dictionary = dict(x="A", y=num, status="clear")
        for num in range(1,11):
            moves_dictionary = dict(x="B", y=num, status="clear")
        for num in range(1,11):
            moves_dictionary = dict(x="C", y=num, status="clear")


if __name__=='__main__':
    for num in range(1, 11):
        moves_dictionary = dict(x="A", y=num, status="clear")
    for num in range(1, 11):
        moves_dictionary = dict(x="B", y=num, status="clear")
    for num in range(1, 11):
        moves_dictionary = dict(x="C", y=num, status="clear")
    for item,y in moves_dictionary:
        print(item)