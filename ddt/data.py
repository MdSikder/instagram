# import pandas lib as pd
import csv

import pandas as pd
import xlsxwriter

import openpyxl

# read by default 1st sheet of an excel file
l = "'"
k = "'"
str1 = ", SqlType.text()"
dataframe1 = pd.read_excel('my.xlsx')

workbook = xlsxwriter.Workbook('ty.xlsx')

worksheet = workbook.add_worksheet()
print('(' + l + dataframe1 + k + str1 + '),')