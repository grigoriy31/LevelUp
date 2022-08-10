import json
victorina_avers = {}
# victorina = {'Какой сейчас год?' : 2022,
#              'Природный спутник земли?': 'Луна',
#              'Почему черепашки ниндзя нападают в 4м?': 'Их учитель крыса',
#              'Самая большая страна по площади': 'Россия'}
# with open('questions.json', 'w') as json_file:
#     json.dump(victorina, json_file)

with open('questions.json') as json_file:
    victorina = json.load(json_file)
k, g = 0, 0
for i in victorina.keys():
    a = input(f'{i}')
    victorina_avers[i] = a
    if str(a) == str(victorina[i]):
        print('Ответ верный')
        k += 1
        g += 1
    else:
        print('Ответ не верный')
        g += 1
print(f'Вы набрали {k} балов из {g} возможных')

with open('victorina_avers.json', 'w') as json_file:
    json.dump(victorina_avers, json_file)

