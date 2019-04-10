import xlrd
import os
import json
 
base_dir=os.path.dirname(os.path.dirname(__file__))
# lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

excel_file_path = os.path.join(base_dir, 'data\TestData.xlsx')

def excel_to_lists(sheet_name):
    data_list=[]
    wb=xlrd.open_workbook(excel_file_path)
    sheet=wb.sheet_by_name(sheet_name)
    hearder=sheet.row_values(0)

    for i in range(1,sheet.nrows):
        data=dict(zip(hearder,sheet.row_values(i)))
        data_list.append(data)
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name==case_data['case_name']:
            return case_data
