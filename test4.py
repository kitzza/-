import openpyxl

def read_excel_file():
    work_book = openpyxl.load_workbook('D:\A线程组\data4.xlsx')
    # sheets = work_book.get_sheet_names()
    # print(sheets)
    sheet1 = work_book.get_sheet_by_name('成绩表')
    # cell = sheet1['A1']
    # print(cell.value)
    for r in sheet1.rows:                           
        print(r)




if __name__ == '__main__':
    read_excel_file()