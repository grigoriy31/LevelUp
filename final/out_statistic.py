from imp_statistic import spb_part_1, spb_part_2, sim_card
import openpyxl
def result_sim():
    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx.xls')
    result_sim = sim_card()
    for sim_name_n in result_sim:
        sheet = stat[sim_name_n]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column)
            if a == '':
                return False
                sheet.cell(row=5, column=column).append(int(len(result_sim[sim_name_n[sum_sim_smart]])))
                sheet.cell(row=6, column=column).append(int(len(result_sim[sim_name_n[sum_sim_data]])))
            else:
                return True
                column += 1
def result_1():
    name_m_1 = spb_part_1()
    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx.xls')
    for result in name_m_1:
        sheet = stat[result]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column)
            if a == '':
                return False
                sheet.cell(row=3, column=column).append(int(name_m_1[result[1]]))
                sheet.cell(row=4, column=column).append(int(name_m_1[result[2]]))
                sheet.cell(row=4, column=column).append(int(name_m_1[result[3]]))
            else:
                return True
                column += 1

def result_2():
    name_m_2 = spb_part_2()
    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx.xls')
    for result in name_m_2:
        sheet = stat[result]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column)
            if a == '':
                return False
                sheet.cell(row=3, column=column).append((name_m_1[result[1]]))
                sheet.cell(row=4, column=column).append((name_m_1[result[2]]))
                sheet.cell(row=4, column=column).append((name_m_1[result[3]]))
            else:
                return True
                column += 1






result_2()
result_1()
result_sim()