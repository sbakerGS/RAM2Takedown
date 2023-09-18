
import openpyxl


def get_excel():
    
    wbPath = "H:\Internal Innovation\RAM to Takedown\Run Python from VBA_20230402_save userform values.xlsm"
    # Get userform data from Excel
    wb = openpyxl.load_workbook(wbPath)
    print(wbPath)
    ws = wb["AutoTD"]

    data_list = [ws.cell(row=i,column=2).value for i in range(14,22)]

    start_level, end_level, loading_type, max_height, model_path, combo_dead, combo_live, combo_trib = [data_list[i] for i in range(0,len(data_list))]
    print("start: " + str(start_level))
    print("end: "+ str(end_level))
    print("loading type: "+ str(loading_type))
    print(data_list)

get_excel()