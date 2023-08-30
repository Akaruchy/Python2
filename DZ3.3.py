# Задача 3.
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

things = {"фляга с водой": 3000, 
          "спички": 10, 
          "фонарик": 50, 
          "аптечка": 1000, 
          "палатка": 2200, 
          "спальник": 500, 
          "нож": 100, 
          "пенка": 70,
          "котелок": 300,
          "туалетная бумага": 40,
          "походный паек": 5000,
          "веревка": 80,
          "мыло": 100}

max_weight = 10000

my_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))

backpack = {}
total_weight = 0
for key, value in my_dict.items():
    if total_weight + value <= max_weight:
        backpack[key] = value
        total_weight += value
        
print('Вещи по убыванию веса: ')
for k, v in backpack.items():
    print(k, ':', v)

new_dict = dict(sorted(things.items(), key=lambda x: x[1]))
itog = {}
total_weight = 0
for key, value in new_dict.items():
    if total_weight + value <= max_weight:
        itog[key] = value
        total_weight += value

print('Вещи по возрастанию веса: ')
for k, v in itog.items():
    print(k, ':', v)