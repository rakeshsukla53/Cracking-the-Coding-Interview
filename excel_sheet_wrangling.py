__author__ = 'rakesh'

import xlrd

file_location = "/home/rakesh/Downloads/Ontodia Data/IBM Watson /CROL 2014 Dec - Oct - Data/" \
                "procPublicationRequest Oct-Dec 2014 (Updated).xlsx"

workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

'''
for i in range(0, 450):
    print sheet.cell_value(i, 13)  #printing out the row and column number here. Row is 1 and column is 13
'''

print sheet.nrows  #number of rows in the sheet

print sheet.ncols  #number of cols in the sheet

'''
for col in range(sheet.ncols):
    print sheet.cell_value(0, col)   #printing out the headings in a row here
'''

#use of list comprehension

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

print data[2]  #print out the list of all the values











