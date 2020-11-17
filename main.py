def field_print(field):
    for i in field:
        print()
        for j in i:
            print(j, end=' ')
    print()


def check_the_winner(field):

    check1 = [field[1][1], field[2][1], field[3][1]]
    check2 = [field[1][2], field[2][2], field[3][2]]
    check3 = [field[1][3], field[2][3], field[3][3]]
    check4 = [field[1][1], field[1][2], field[1][3]]
    check5 = [field[2][1], field[2][2], field[2][3]]
    check6 = [field[3][1], field[3][2], field[3][3]]
    check7 = [field[1][1], field[2][2], field[3][3]]
    check8 = [field[1][3], field[2][2], field[3][1]]
    checks = [check1, check2, check3, check4, check5, check6, check7, check8]

    for i in checks:
        if i == ["X", "X", "X"] or i == ["O", "O", "O"]:
            return True

    return False


game = True
winer = False
field = [[" ", "0", "1", "2"], ["0", "-", "-", "-"], ["1", "-", "-", "-"], ["2", "-", "-", "-"]]
moves = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
player1 = input("Введите имя первого игрока\n")
player2 = input("Введите имя второго игрока\n")
player = True

while game:
    if player:
        print(f"ходит игрок {player1}")
    else:
        print(f"ходит игрок {player2}")
    field_print(field)
    while True:
        move = input("Ваш ход:")
        if len(move) != 2 or move not in moves:
            print("Неверный ход, либо клетка уже занята")
        else:
            break
    moves.pop(moves.index(move))
    index1 = int(move[0])
    index2 = int(move[1])
    if player:
        field[index1 + 1][index2 + 1] = "X"
    else:
        field[index1 + 1][index2 + 1] = "O"
    field_print(field)
    if not moves:
        game = False
    if check_the_winner(field):
        game = False
        winer = True
        if player:
            winer_name = player1
        else:
            winer_name = player2
    else:
        player = not player
if winer:
    print(f"Игра закончена, победил {winer_name}, поздравляем!")
else:
    print("В этот раз ничья")
