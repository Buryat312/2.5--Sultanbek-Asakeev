#Задание 2

import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 'fhjhafhdfa.txt']

new_name = random.choice(names)
l = len(names)
with open(new_name, 'w') as f:
    f.write('Hallo stranger')
print(new_name)

def file_(text_file):
    for i in text_file:
        try:
            with open (i,'r') as w:
                w.read()
            # 
        except FileNotFoundError:
            print("Такого файла не существует")

file_(names)