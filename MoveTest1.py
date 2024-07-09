import pandas as pd
from openpyxl import load_workbook
import xlwings as xw
from numpy import array

import turtle


xl_dir = "C:/" ... some ref to data ..."/DATA/"
xl_file = xl_dir + "Test tag 30_meters.xlsx"
sheet_name = "Sheet"

wb = xw.Book(xl_file)
ws = wb.sheets[0]
#sht = xw.Book(sheetname = 0)
LNTH = 507
Lat_List = ws.range('A1:A507').value
Long_List = ws.range('B1:B507').value


Lat_Arr = array(Lat_List)
#print(Lat_List.shape())
print(Lat_Arr)
#for num in Lat_List:
#    print(round(num))
#for num in Long_List:
#    print(round(num))



df = pd.read_excel(xl_file, sheet_name) # can also index sheet by name or fetch all sheets
#mylist = df['column name'].tolist()



mallard = turtle.Turtle()
mallard.pencolor("blue")
for i in range(LNTH - 1):
    x = Lat_List[i] * 1
    y = Long_List[i] * 1
    mallard.goto(x, y)
    mallard.dot()
    
    pass
print("DONE")
turtle.done()


"""
mallard = turtle.Turtle()
for x, y in Lat_List, Long_List:
    mallard.goto(x, y)
    mallard.dot()
    
    pass
mallard.done()



star = turtle.Turtle()
for i in range(4):
   star.forward(100)
   star.dot()
   star.right(144)
turtle.done()


"""

