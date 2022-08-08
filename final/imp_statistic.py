import openpyxl

def spb_part_1():
    data = openpyxl.load_workbook('spb_part_1.xlsx')
    sheet = data.active
    row = 3
    name_m_1 = {}
    while True:
        gsm = sheet.cell(row=row, column=7).value
        aks = sheet.cell(row=row, column=11).value
        serv = sheet.cell(row=row, column=3).value
        name = sheet.cell(row=row, column=1).value
        if type(name) == str:
            name_m_1[name] = [int(gsm), int(aks), int(serv)]
            row += 1
            return True
        elif name == '':
            return False
    return name_m_1


def spb_part_2():
    data = openpyxl.load_workbook('spb_part_2.xlsx')
    sheet = data.active
    row = 3
    name_m_2 = {}
    while True:
        gsm = sheet.cell(row=row, column=7).value
        aks = sheet.cell(row=row, column=11).value
        serv = sheet.cell(row=row, column=3).value
        name = sheet.cell(row=row, column=1).value
        if name == '':
            return False
        else:
            name_m_2[name] = [int(gsm), int(aks), int(serv)]
            row += 1
            return True
    return name_m_2
def sim_card():
    data = openpyxl.load_workbook('sim_cards.xlsx')
    sheet = data.active
    row = 3
    sum_sim_smart = []
    sum_sim_data = []
    result_sim = {}
    # Словарь будет иметь вид:{sim_name_m:{sum_sim_smart:[], sum_sim_data:[]}} и т.д.

    sim_smart = ['SIM YOTA смартфон МОНО 0 руб.', 'SIM Yota смартфон Интернет Магазин 0 руб']
    sim_data = ['SIM Yota модем МОНО 0 руб.', 'SIM Yota модем Интернет Магазин 0 руб', 'SIM Yota комплект к оборудованию']
    while True:
        sim_name_m = sheet.cell(row=row, column=3)

        if sim_name_m in result_sim:
            if sheet.cell(row=row, column=4) in sim_smart:
                a = int(sheet.cell(row=row, column=5).value)
                result_sim[sim_name_m[sum_sim_smart]].append(a)
                row += 1
                return True
            elif sheet.cell(row=row, column=4) in sim_data:
                a = int(sheet.cell(row=row, column=5).value)
                result_sim[sim_name_m[sum_sim_data]].append(a)
                row += 1
                return True

            else:
                row += 1
                return True
        elif sheet.cell(row=row, column=4) == "":
            return False
        else:
            result_sim[sim_name_m] = {sum_sim_smart:[], sum_sim_data:[]}
            if sheet.cell(row=row, column=4) in sim_smart:
                a = int(sheet.cell(row=row, column=5).value)
                result_sim[sim_name_m[sum_sim_smart]].append(a)
                row += 1
                return True
            elif sheet.cell(row=row, column=4) in sim_data:
                a = int(sheet.cell(row=row, column=5).value)
                result_sim[sim_name_m[sum_sim_data]].append(a)
                row += 1
                return True
            else:
                row += 1
                return True
    return result_sim
print(spb_part_1())
print(sim_card())
print(spb_part_2())