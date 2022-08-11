# a = int(input('Введите год: '))
# def year():
#     i = 0
#     while i < a:
#         if a == 2000 - 12*i or a == 2000 + 12*i:
#             print('Дракон')
#             break
#         elif a == 2001 - 12*1 or a == 2001 + 12*i:
#             print('Змея')
#             break
#         elif a == 2002 - 12*i or a == 2002 + 12*i:
#             print('Лошадь')
#             break
#         elif a == 2003 - 12*i or a == 2003 + 12*i:
#             print('Коза')
#             break
#         elif a == 2004 - 12*i or a == 2004 + 12*i:
#             print('Обезьяна')
#             break
#         elif a == 2005 - 12*i or a == 2005 + 12*i:
#             print('Петуx')
#             break
#         elif a == 2006 - 12*i or a == 2006 + 12*i:
#             print('Собака')
#             break
#         elif a == 2007 - 12*i or a == 2007 + 12*i:
#             print('Свинья')
#             break
#         elif a == 2008 - 12*i or a == 2008 + 12*i:
#             print('Крыса')
#             break
#         elif a == 2009 - 12*i or a == 2009 + 12*i:
#             print('Бык')
#             break
#         elif a == 2010 - 12*i or a == 2010 + 12*i:
#             print('Тигр')
#             break
#         elif a == 2011 - 12*i or a == 2011 + 12*i:
#             print('Кролик')
#             break
#         else:
#             i += 1
#     return i
# a = year()

data = input('Введите координаты: ')

if data[0] == 'a' or data[0] == 'c' or data[0] == 'e' or data[0] == 'g':
    if int(data[1]) % 2 == 0:
        print('белая')
    else:
        print('Черная')
elif data[0] == 'b' or data[0] == 'd' or data[0] == 'f' or data[0] == 'h':
    if int(data[1]) % 2 == 0:
        print('черная')
    else:
        print('Белая')