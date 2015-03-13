

import xlrd
from datetime import datetime

file_location = "/home/rakesh/Downloads/Ontodia Data/IBM Watson /CROL 2014 Dec - Oct - Data/" \
                "procPublicationRequest Oct-Dec 2014 (Updated).xlsx"

workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

def createHTML():

    for i in range(1, sheet.nrows):

        file_name = 'Record' + str(i) + '.html'
        print file_name

        file_location = open('/home/rakesh/Downloads/Ontodia Data/IBM Watson /Record_convert_to_html/' + file_name, 'a')

        head = '''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
'''
        file_location.write(head)
        requestID = '<RequestID>Request ID:' + " " + str(int(data[i][0])) + '</RequestID></br>'
        file_location.write(requestID)
        publicDate = '<public> Publication Date:' + " " + str(int(data[i][0]))[0:4] + '</Public></br>'
        file_location.write(publicDate)
        start_date = sheet.cell_value(i, 1)
        datetime_value = datetime(*xlrd.xldate_as_tuple(start_date, 0))   #converting my timedate field here
        startDate = '<startDate> Start Date:' + " " + str(datetime_value) + '</startDate></br>'
        file_location.write(startDate)
        end_date = sheet.cell_value(i, 2)
        datetime_value = datetime(*xlrd.xldate_as_tuple(end_date, 0))   #converting my timedate field here
        endDate = '<EndDate>End Date:' + " " + str(datetime_value) + '</EndDate></br>'
        file_location.write(endDate)
        agencyCode = '<AgencyCode>Agency Code:' + " " + str(data[i][3]).split('.')[0] + '</AgencyCode></br>'
        file_location.write(agencyCode)
        agencyName = '<AgencyName>Agency Name:' + " " + str(data[i][4]) + '</AgencyName></br>'
        file_location.write(agencyName)
        agencyDivision = '<AgencyDivision>Agency Divison:' + " " + str(data[i][5]) + '</AgencyDivision></br>'
        file_location.write(agencyDivision)
        noticeCode = '<TypeOfNoticeCode>Type of Notice Code:' + " " + str(int(data[i][6])) + '</TypeOfNoticeCode></br>'
        file_location.write(noticeCode)
        noticeDe = '<TypeOfNoticeDescription>Type of Notice Description:' + " " + str(data[i][7]) + \
                   '</TypeOfNoticeDescription></br>'
        file_location.write(noticeDe)
        shortTitle = '<ShortTitle>Short Title:' + " " + str(data[i][8]) + '</ShortTitle></br>'
        file_location.write(shortTitle)
        sectionID = '<SectionID>SectionID:' + " " + str(int(data[i][9])) + '</SectionID></br>'
        file_location.write(sectionID)
        sectionName = '<SectionName>SectionName:' + " " + str(data[i][10]) + '</SectionName></br>'
        file_location.write(sectionName)
        due_date = sheet.cell_value(i, 11)
        if due_date:
            due_date = datetime(*xlrd.xldate_as_tuple(due_date, 0))
        dueDate = '<DueDate>Due Date:' + " " + str(datetime_value) + '</DueDate></br>'
        file_location.write(dueDate)
        confirmNum = '<ConfirmationNumber>ConfirmationNumber:' + " " + str(int(data[i][12])) + \
                     '</ConfirmationNumber></br>'
        file_location.write(confirmNum)
        head1 = '''
</head>

<body>
<h1>Additional Description</h1>
'''
        file_location.write(head1)
        inf = str(data[i][13])
        file_location.write(inf)
        file_location.close()


createHTML()

