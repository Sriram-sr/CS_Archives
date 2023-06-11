import openpyxl

path = '/home/sriram/Selenium/empty_file.xlsx'
workbook = openpyxl.load_workbook(path)

sheet = workbook.active

row_list = [[],[[],'EMPID','FNAME','LNAME','SALARY'],[[],'001','Hanish','Kumar',30000],[[],'002','Veera','Mani',40000],[[],'003','Mohd','Naji',50000]]

for row in range(1,5):
    for col in range(1,5):
        sheet.cell(row=row,column=col).value = row_list[row][col]

workbook.save(path)        