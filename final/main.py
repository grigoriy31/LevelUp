import openpyxl
plans = {}
def statistics():
    stat = openpyxl.workbook('Statistic_Spb_2022.xlsx')




def spb_part_1():
    data = openpyxl.workbook('spb_part_1.xlsx')
    sheet = data.active
    row = 2
    name_m = {}
    while True:
        name = sheet.cell(row=row, column = 1)
        if type(name) == str:
            name_m[name] = ['Qrow']
            row += 1
            return True
        elif name == '':
            return False


def spb_part_2():
    data = openpyxl.workbook('spb_part_1.xlsx')
    sheet = data.active
    row = 2
    name_m = {}
    while True:
        name = sheet.cell(row=row, column=1)
        if name == '':
            return False
        else:
            name_m[name] = ['']
            row += 1
            return True

def sim_card():
