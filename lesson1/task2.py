# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) 
# и определить тип, содержимое и длину соответствующих переменных.

task_group_words = [b"class", b"function", b"method"]

for word in task_group_words:
    print(f'{type(word)}\n{word}\n{len(word)}\n')
