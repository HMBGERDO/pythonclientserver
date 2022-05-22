# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

import chardet


with open("test_file.txt", "rb") as f:
    print(chardet.detect(f.readline())['encoding'])

with open("test_file.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line)
