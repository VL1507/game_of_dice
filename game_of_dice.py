from random import randint
from time import sleep

game_count = int(input("Сколько раундов вы хотите сыграть?\t"))

sum_player1, sum_player2 = 0, 0

for i in range(1, game_count + 1):
    print("\t\tРаунд {}".format(i))
    sleep(1)

    points1, points2 = randint(1, 6), randint(1, 6)
    sum_player1 += points1
    sum_player2 += points2

    print("Первый игрок кидает кости!", end=' ')
    sleep(1)
    print("Выпало {}".format(points1))

    sleep(2)

    print("Второй игрок кидает кости!", end=' ')
    sleep(1)
    print("Выпало {}".format(points2))

    sleep(1)

    print("Конец {} раунда! Общий счет {} : {}".format(i, sum_player1,
                                                       sum_player2))
    sleep(2)
sleep(1)
if sum_player1 > sum_player2:
    print("Победил первый игрок!", end=' ')
elif sum_player1 < sum_player2:
    print("Победил второй игрок!", end=' ')
else:
    print("Ничья!", end=' ')
print("Счет {} : {}".format(sum_player1, sum_player2))
