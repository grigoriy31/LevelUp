# Проверка с помощью функций

# def data_enter():
#     d = input('Введите дату формате dd.mm.gggg: ').split('.')
#     dd = int(d[0])
#     mm = int(d[1])
#     yyyy = int(d[2])
#     return dd, mm, yyyy
#
# def chek_data():
#     dd, mm, yyyy = data_enter()
#     a = str
#     if yyyy <= 2022:
#         if mm == 2:
#             if (yyyy % 4) != 0:
#                 if dd <= 28:
#                     a = 'ok'
#                 else:
#                     a = 'FAILED'
#             else:
#                 if dd <= 29:
#                     a = 'ok'
#                 else:
#                     a = 'FAILED'
#         else:
#             if 1 < mm <= 7:
#                 if (mm % 2) == 0:
#                     if dd <= 30:
#                         a = 'ok'
#                     else:
#                         a = 'FAILED'
#                 else:
#                     if dd <= 31:
#                         a = 'ok'
#                     else:
#                         a = 'FAILED'
#             elif 7 < mm <= 12:
#                 if (mm % 2) == 0:
#                     if dd <= 31:
#                         a = 'ok'
#                     else:
#                         a = 'FAILED'
#                 else:
#                     if dd <= 30:
#                         a = 'ok'
#                     else:
#                         a = 'FAILED'
#             else:
#                 a = 'FAILED'
#     else:
#         a = 'FAILED'
#     return a
#
# print(chek_data())
#

# Проверка с помощью библиотеки

# import time
#
#
# data = input('Date (mm/dd/yyyy): ')
# try:
#     valid_date = time.strptime(data, '%m/%d/%Y')
# except ValueError:
#     print('FAILED')
# else:
#     print('OK')

