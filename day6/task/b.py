import json
with open('json_data.json') as json_file:
    test = json.load(json_file)
print(test)
result = test['ruskan']

def resultat():
    i = 0
    k = 0
    while i <= 3:
        i += 1
        if i == 1:
            if result[i-1] == '12':
                k += 1
            else:
                print("ответ на вопрос 1: не верен")
                continue
        if i == 2:
            if result[i - 1] == '4':
                k += 1

            else:
                print("ответ на вопрос 2: не верен")
                continue
        if i == 3:
            if result[i - 1] == '26':
                k += 1

            else:
                print("ответ на вопрос 2: не верен")
                continue
    return k
print('Вы набрали ' + str(resultat()) + ' баллов')

