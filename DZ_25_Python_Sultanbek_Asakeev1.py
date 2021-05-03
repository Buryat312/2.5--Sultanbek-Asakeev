# Задание 1

example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def func(list_, dict_):
    for i in list_:
        try:
            a = 0
            for w in dict_[i]:
                try:
                    a += w
                except TypeError:
                    continue
            print(f'{i} - {a}')
        except KeyError:
            print(f'{i} Такого ключа в словаре не существует')
func(elements,example)  