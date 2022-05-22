# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

task_group_words = ["разработка", "администрирование", "protocol", "standart"]

for word in task_group_words:
    word = word.encode(encoding="utf-8")
    print(word)
    word = word.decode(encoding="utf-8")
    print(word)
    print()
