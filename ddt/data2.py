# import xlsxwriter module
import pandas as pd
import xlsxwriter



l = "'"
k = "'"
str1 = ", SqlType.text()"
dataframe1 = pd.read_excel('my.xlsx')

workbook = xlsxwriter.Workbook('ty.xlsx')

worksheet = workbook.add_worksheet()
print('(' + l + dataframe1 + k + str1 + '),')

workbook = xlsxwriter.Workbook('Example2.xlsx')

worksheet2 = workbook.add_worksheet()

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0

content = (dataframe1)

# iterating through content list
for item in content:
    # write operation perform
    worksheet2.write(row, column, item)

    # incrementing the value of row by one
    # with each iterations.
    row += 1

workbook.close()