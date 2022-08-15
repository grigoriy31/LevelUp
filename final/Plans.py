import openpyxl
from imp_statistic import sim_card
resultat_sim = sim_card()

def plans():
    stat = openpyxl.load_workbook('Statistic_Spb_2022.xlsx')
    for name_m in resultat_sim.keys():
        sheet = stat[name_m]
        i = 3
        data_plans_ipm = {}
        data_plans_fact = {}
        data_name_m = {}
        while True:
            data_null = sheet.cell(row=3, column=i).value
            if data_null == None:
                column_imp = i - 3
                column_fact = i - 1
                gsm = sheet.cell(row=3, column=column_imp).value
                aks = sheet.cell(row=4, column=column_imp).value
                serv = sheet.cell(row=7, column=column_imp).value
                data_sim = sheet.cell(row=5, column=column_imp).value
                smart_sim = sheet.cell(row=6, column=column_imp).value
                data_name_m[gsm], data_name_m[aks], data_name_m[smart_sim], data_name_m[data_sim], data_name_m[serv] = int(gsm), int(aks), int(smart_sim), int(data_sim), int(serv)
                data_plans_ipm[name_m] = data_name_m
                gsm = sheet.cell(row=3, column=column_fact).value
                aks = sheet.cell(row=4, column=column_fact).value
                serv = sheet.cell(row=7, column=column_fact).value
                data_sim = sheet.cell(row=5, column=column_fact).value
                smart_sim = sheet.cell(row=6, column=column_fact).value
                data_name_m[gsm], data_name_m[aks], data_name_m[smart_sim], data_name_m[data_sim], data_name_m[serv]= int(gsm), int(aks), int(smart_sim), int(data_sim), int(serv)
                data_plans_fact[name_m] = data_name_m
                continue
            else:
                i += 1

        return data_plans_ipm, data_plans_fact


print(plans())

