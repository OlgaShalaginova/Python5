# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import os
os.system('cls')
import random

first_step = random.randint(0,2)
candy_all = 100
max_take = 28
print(f'Сейчас {candy_all} конфет')

if first_step == 0:
    print('Первый шаг за компьютером')
    while candy_all > 0:
        if candy_all > max_take:
            pc_take = random.randint(1, 29)
        else:
            pc_take = random.randint(1, candy_all)
        candy_all -= pc_take
        print(f'Компьютер взял {pc_take} конфет. Осталось {candy_all} конфет')
        if candy_all <= 0:
            break
        man_take = int(input('Бери конфеты (не больше 28): '))
        if man_take <= max_take:
            candy_all -= man_take
            print(f'Человек взял {man_take} конфет. Осталось {candy_all} конфет')
        else:
            candy_all -= max_take
            print(f'Еще раз, число конфет не больше 28. Тебе отдали максильное число конфет {max_take}. В следующий раз будь внимательнее. Осталось {candy_all} конфет')
        if candy_all <= 0:
            break
else:
    print('Первый шаг за человеком')
    while candy_all > 0:
        man_take = int(input('Бери конфеты (не больше 28): '))
        if man_take <= max_take:
            candy_all -= man_take
            print(f'Человек взял {man_take} конфет. Осталось {candy_all} конфет')
        else:
            candy_all -= max_take
            print(
                f'Еще раз, число конфет не больше 28. Тебе отдали максильное число конфет {max_take}. В следующий раз будь внимательнее. Осталось {candy_all} конфет')
        if candy_all <= 0:
            break
        if candy_all > max_take:
            pc_take = random.randint(1, 29)
        else:
            pc_take = random.randint(1, candy_all)
        candy_all -= pc_take
        print(f'Компьютер взял {pc_take} конфет. Осталось {candy_all} конфет')
        if candy_all <= 0:
            break
print('Победа!')