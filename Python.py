def welcome():
    print("Это игра крестики-нолики. Введите координаты для начала игры!")
    print("Левая часть поля - это Ось X")
    print("Верхняя часть поля - это Ось Y")

field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def game_board():
    for i in range(1):
        print("    0    1    2")
        print("0", field[0])
        print("1", field[1])
        print("2", field[2])

def ask_player():
    while True:
        answer = input("Введите сюда координаты для Вашей фигуры:")
        if len(answer) > 2:
            print("Вам нужно ввести две координаты")
            continue
        x, y = answer
        if not(x.isdigit()) or not(y.isdigit()):
            print("Пожалуйста, введите целые числа согласно координатам!")
            continue
        x, y = int(x), int(y)
        if 0 < x > 2 or 0 < y > 2:
            print("Вы ввели координаты не по схеме")
            continue
        if field[x][y] != " ":
            print("К сожалению, эта клетка уже занята!")
            continue
        return x, y

def check_win():
        win_cordinats = [((0, 0), (1, 0), (2, 0)), ((0, 0), (0, 1), (0, 2)), ((0, 1), (1, 1), (2, 1)), ((1, 0), (1, 1),
                        (1, 2)), ((2, 0), (2, 1), (2, 2)),((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)),((0, 2), (1, 2), (2, 2))]
        for cordinats in win_cordinats:
            figures = []
            for q in cordinats:
                figures.append(field[q[0]][q[1]])
            if figures == ["X", "X", "X"]:
                print("Победитель X! Поздравляю!")
                return True
            if figures == ["O", "O", "O"]:
                print("Победитель O! Поздравляю!")
                return True

welcome()
buttom = 0
while True:
    buttom += 1
    game_board()
    if buttom % 2 == 1:
        print("Сейчас ходит Х")
    else:
        print("Сейчас ходит O")
    x, y = ask_player()
    if buttom % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"
    if check_win():
        break
    if buttom == 9:
        print("У Вас ничья! Поздравляю!")
        break