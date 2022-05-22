# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
# «отчетный» файл в формате CSV. Для этого:
# a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
# данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
# каждого параметра поместить в соответствующий список. Должно получиться четыре
# списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
# функции создать главный список для хранения данных отчета — например, main_data
# — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
# системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
# © geekbrains.ru 16
# столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);
# b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
# функции реализовать получение данных через вызов функции get_data(), а также
# сохранение подготовленных данных в соответствующий CSV-файл;
# c. Проверить работу программы через вызов функции write_to_csv().

import re
import csv


def get_data(files):
    os_author_list = []
    os_name_list = []
    os_product_code_list = []
    os_type_list = []
    main_data = [["os_name", "os_type", "os_author", "os_product_code"]]
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            os_author = re.search(r"Изготовитель ОС:\s*(?P<os_author>[^\n]*)\n", text).group("os_author")
            os_name = re.search(r"Название ОС:\s*(?P<os_name>[^\n]*)\n", text).group("os_name")
            os_product_code = re.search(r"Код продукта:\s*(?P<os_product_code>[^\n]*)\n", text).group("os_product_code")
            os_type = re.search(r"Тип системы:\s*(?P<os_type>[^\n]*)\n", text).group("os_type")
            os_author_list.append(os_author)
            os_name_list.append(os_name)
            os_product_code_list.append(os_product_code)
            os_type_list.append(os_type)
            main_data.append([os_name, os_type, os_author, os_product_code])
    return main_data

def write_to_csv():
    files = ["info_1.txt", "info_2.txt", "info_3.txt"]
    data = get_data(files)
    with open("result.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    write_to_csv()
