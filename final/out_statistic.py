from imp_statistic import spb_part_1, spb_part_2, sim_card
import openpyxl
from openpyxl.formula.translate import Translator
resultat_sim = sim_card()
name_m_1 = spb_part_1()
name_m_2 = spb_part_2()

def result_sim():
    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx')

    for sim_name_n in resultat_sim.keys():
        sheet = stat[sim_name_n]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column).value
            if a == None:
                b = resultat_sim[sim_name_n]
                sheet.cell(row=5, column=column-2, value=b['sum_sim_smart'])
                sheet.cell(row=6, column=column-2, value=b['sum_sim_data'])

                stat.save('Statistic_Spb_2022.xlsx')
                break
            else:
                column += 1
    stat.close()
def result_1():

    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx')
    for result in name_m_1.keys():
        sheet = stat[result]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column).value
            if a == None:
                b = name_m_1[result]
                sheet.cell(row=3, column=column, value=b[0])
                sheet.cell(row=4, column=column, value=b[1])
                sheet.cell(row=7, column=column, value=b[2])
                stat.save('Statistic_Spb_2022.xlsx')
                break
            else:
                column += 1
    stat.close()

def result_2():

    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx')
    for result in name_m_2.keys():
        sheet = stat[result]
        column = 2
        while True:
            a = sheet.cell(row=3, column=column).value
            if a == None:

                b = name_m_2[result]
                sheet.cell(row=3, column=column, value=b[0])
                sheet.cell(row=4, column=column, value=b[1])
                sheet.cell(row=7, column=column, value=b[2])
                stat.save('Statistic_Spb_2022.xlsx')
                break
            else:
                column += 1
    stat.close()



