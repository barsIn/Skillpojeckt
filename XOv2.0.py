import random


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


def not_lose(field):
    counter = 0
    checkin = []
    indexi = 0
    indexj = 0
    checkindex = 0
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
        indexi += 1
        for j in i:
            if j == "X":
                counter += 1
            elif j == "O":
                counter -= 1
        if counter == 2:
            checkin = i
            break
    if counter != 2:
        return False
    for i in checkin:
        indexj += 1
        if i == "-":
            break
    checkindex = int(str(indexi) + str(indexj))
    print(checkindex)
    if checkindex == 11:
        return "00"
    elif checkindex == 12:
        return "10"
    elif checkindex == 13:
        return "20"
    elif checkindex == 21:
        return "01"
    elif checkindex == 22:
        return "11"
    elif checkindex == 23:
        return "21"
    elif checkindex == 31:
        return "02"
    elif checkindex == 32:
        return "12"
    elif checkindex == 33:
        return "22"
    elif checkindex == 41:
        return "00"
    elif checkindex == 42:
        return "01"
    elif checkindex == 43:
        return "02"
    elif checkindex == 51:
        return "10"
    elif checkindex == 52:
        return "11"
    elif checkindex == 53:
        return "12"
    elif checkindex == 61:
        return "10"
    elif checkindex == 62:
        return "11"
    elif checkindex == 63:
        return "12"


def move0(moves):
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        cpu_move0 = str(x) + str(y)
        print(cpu_move0)
        if cpu_move0 in moves:
            break
    return cpu_move0


def move1(field, moves):
    print(bool(not_lose(field)))
    if not_lose(field):
        cpu_moove1 = not_lose(field)
        return cpu_moove1
    else:
        return move0(moves)


def cpu_moove(field, moves, dif):
    if dif == "0":
        return move0(moves)
    elif dif == "1":
        return move1(field, moves)
    elif dif == "2":
        return move2
    else:
        return move3


game = True
winer = False
cpu = False
field = [[" ", "0", "1", "2"], ["0", "-", "-", "-"], ["1", "-", "-", "-"], ["2", "-", "-", "-"]]
moves = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
dif = ["0", "1", "2", "3"]
while True:
    num_of_players = input("введи колличество игроков\n")
    if num_of_players != "1" and num_of_players != "2":
        print("Не верно указано количество")
    else:
        break
if num_of_players == "1":
    cpu = True

player1 = input("Введите имя первого игрока\n")
if not cpu:
    player2 = input("Введите имя второго игрока\n")
else:
    player2 = "Компьютер"
    while True:
        difficulty = input("Выбери сложность от 0 до 3")
        if difficulty in dif:
            break
        else:
            print("Неверно указана сложность, попробуй еще раз")
player = True

while game:
    if player:
        print(f"ходит игрок {player1}")
    else:
        print(f"ходит игрок {player2}")
    field_print(field)
    if not cpu or player:
        while True:
            move = input("Ваш ход:")
            if len(move) != 2 or move not in moves:
                print("Неверный ход, либо клетка уже занята")
            else:
                break
    else:
        move = cpu_moove(field, moves, difficulty)
    print(moves)
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
