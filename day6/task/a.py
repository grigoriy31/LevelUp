import datetime
import json
import pickle
answer0 = input('Как тебя зовут?: ')
answer1 = input('Сколько будет 4 +8 =  ')
answer2 = input('Сколько будет 12 / 3 =  ')
answer3 = input('Сколько будет 13 * 2 = ')
# data = datetime.now().strftime("%H:%M:%S")
test = {}
test[answer0] =[]
test[answer0].append(answer1)
test[answer0].append(answer2)
test[answer0].append(answer3)
# test[answer0].append(str(datetime.now().strftime("%H:%M:%S")))

# with open('json_data.json', 'w') as outfile:
#     json.dump(test, outfile)

with open('important.pickle', 'wb') as file:
    pickle.dump(test, file)