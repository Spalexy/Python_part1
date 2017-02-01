# coding: utf-8

__author__ = 'Alexander Pridacha'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print("\n==Создание директорий dir_1 - dir_9==\n")

dir_path = os.path.join(os.getcwd(), 'dir_')

def mk_dirs():
    for i in range(9):
        d_name = 'dir_' + str(i + 1)
        try:
            os.mkdir(d_name)
        except FileExistsError:
            print(d_name + ' - такая директория уже существует')


def rm_dirs():
    for i in range(9):
        d_name = 'dir_' + str(i + 1)
        try:
            os.rmdir(d_name)
        except FileNotFoundError:
            print(d_name + ' - директория была удалена ранее')


mk_dirs()
rm_dirs()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("\n==Папки текущей директории==\n")


f_list = (os.listdir())
i = 0

while i < len(f_list):
    if not os.path.isfile(f_list[i]):
        print(f_list[i])
    i += 1


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


print("\n==Создание копии файла, из которого запущен данный скрипт ==\n")

from shutil import copy

f_name = __file__
copy(f_name, f_name + ".copy")