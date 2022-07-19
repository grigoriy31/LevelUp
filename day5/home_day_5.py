from statistics import mean

data = []
diari = {}
def diari_1():
    command = input("Введите желаемое действие: ")
    while command != 'exit':
        if command == 'add':
            data = input("Введите данные ученика в формате Иванов_Иван ")
            if data in diari:
                print("Ученик уже есть в журнале!")
                command = input("Введите желаемое действие: ")
            else:
                diari[data] = []
                diari[data].append(None)
                command = input("Введите желаемое действие: ")
        elif command == 'all':
            for i in diari.keys():
                print(i)
            command = input("Введите желаемое действие: ")
        elif command == 'mark':
            evaluations = []
            users = input("Введите данные ученика в формате Иванов_Иван: ")
            a = [int(x) for x in input("Введите оценки ученика: ").split()]
            evaluations.append(a)
            diari[users].append(evaluations)
            command = input("Введите желаемое действие: ")
        elif command == 'edit':
            users_old = input('Введите ФМ необходимые для замены в формате Иванов_Иван: ')
            users_new = input("Введите новые данные ученика в формате Иванов_Иван")
            diari[users_new] = diari.pop(users_old)
            command = input("Введите желаемое действие: ")
        elif command== 'delete':
            users_del = input("Введите данные ученика для удаления в формате Иванов_Иван: ")
            del diari[users_del]
            command = input("Введите желаемое действие: ")
        elif command == 'average':
            for i in diari:
                evaluations = diari[i]
                evaluations_avg = mean(evaluations)
                print(str(i) + "Средний бал" + round(evaluations_avg, 2))
                command = input("Введите желаемое действие: ")
        elif command == 'exit':
            continue
        else:
            print("Неверно введена команда")
            command = input("Введите желаемое действие: ")
    return diari

print(diari_1())

