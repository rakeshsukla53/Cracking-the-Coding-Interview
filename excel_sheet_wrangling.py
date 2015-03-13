__author__ = 'rakesh'

import xlrd
from datetime import datetime


file_location = "/home/rakesh/Downloads/Ontodia Data/IBM Watson /CROL 2014 Dec - Oct - Data/" \
                "procPublicationRequest Oct-Dec 2014 (Updated).xlsx"

workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

'''
for i in range(0, 450):
    print sheet.cell_value(i, 13)  #printing out the row and column number here. Row is 1 and column is 13
'''

#print sheet.nrows  #number of rows in the sheet

#print sheet.ncols  #number of cols in the sheet

'''
for col in range(sheet.ncols):
    print sheet.cell_value(0, col)   #printing out the headings in a row here
'''

#use of list comprehension
'''
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

print data[1]  #print out the list of all the values
'''

'''
end_date = sheet.cell_value(1, 2)
datetime_value = datetime(*xlrd.xldate_as_tuple(end_date, 0))   #converting my timedate field here

print datetime_value
'''

request_id = str(int(sheet.cell_value(2, 0)))
year = request_id[0:4]
print request_id, year

head = '''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
'''

requestID = '<RequestID> Request ID :' + 20130621104 + '</RequestID></br>'
publicDate = '<public> Publication Date :' + 20130621104 + '</Public></br>'
startDate = '<startDate> Start Date :' + 1/2/2014 0:00:00 + '</startDate></br>'
endDate = '<EndDate>   End Date   : ' + 12/31/2014 00:00:00 + '</EndDate></br>'
agencyCode = '<AgencyCode> Agency Code :' + 56 + '</AgencyCode></br>'
agencyName = '<AgencyName> Agency Name :' + Police + '</AgencyName></br>'
agencyDivision = '<AgencyDivision> Agency Divison :' +  + '</AgencyDivision></br>'
noticeCode = '<TypeOfNoticeCode> Type of Notice Code :' + + '</TypeOfNoticeCode></br>'
noticeDe = '<TypeOfNoticeDescription> Type of Notice Description :' +  + '</TypeOfNoticeDescription></br>'
shortTitle = '<ShortTitle> Short Title :' + +  '</ShortTitle></br>'
sectionID = '<SectionID> SectionID :' + +  '</SectionID></br>'
sectionName = '<SectionName> SectionName :' + + '</SectionName></br>'
dueDate = '<DueDate> Due Date :' + + '</DueDate></br>'
confirmNum = '<ConfirmationNumber> ConfirmationNumber :' + + '</ConfirmationNumber></br>'

head1 = '''
</head>
<body>
<h1>Additional Description</h1>
'''
<p> <strong><strong><strong><strong><strong><strong>OWNERS ARE WANTED BY THE PROPERTY CLERK DIVISION OF THE NEW YORK CITY POLICE DEPARTMENT.</strong></strong></strong></strong></strong></strong></p> <p> &nbsp;</p> <p> The following listed property is in the custody, of the Property Clerk Division without claimants. Recovered, lost, abandoned property, obtained from prisoners, emotionally disturbed, intoxicated and deceased persons; and property obtained from persons incapable of caring for themselves.</p> <p> &nbsp;</p> <p> Motor vehicles, boats, bicycles, business machines, cameras, calculating machines, electrical and optical property, furniture, furs, handbags, hardware, jewelry, photographic equipment, radios, robes, sound systems, surgical and musical instruments, tools, wearing apparel, communications equipment, computers, and other miscellaneous articles.</p> <p> &nbsp;</p> <p> <strong><strong><strong>INQUIRIES</strong></strong></strong></p> <p> Inquiries relating to such property should be made in the Borough concerned, at the following office of the Property Clerk.</p> <p> &nbsp;</p> <p> <strong><strong><strong>FOR MOTOR VEHICLES&nbsp;</strong></strong></strong>(All Boroughs):</p> <ul> <li> Springfield Gardens Auto Pound, 174-20 North Boundary Road, Queens, NY 11430, (718) 553-9555</li> <li> Erie Basin Auto Pound, 700 Columbia Street, Brooklyn, NY 11231, (718) 246-2030</li> </ul> <p> <strong><strong><strong>FOR ALL OTHER PROPERTY</strong></strong></strong></p> <ul> <li> Manhattan - 1 Police Plaza, New York, NY 10038, (646) 610-5906</li> </ul> <ul> <li> Brooklyn - 84th Precinct, 301 Gold Street, Brooklyn, NY 11201, (718) 875-6675</li> </ul> <ul> <li> Bronx Property Clerk - 215 East 161 Street, Bronx, NY 10451, (718) 590-2806</li> </ul> <ul> <li> Queens Property Clerk - 47-07 Pearson Place, Long Island City, NY 11101, (718) 433-2678</li> </ul> <ul> <li> Staten Island Property Clerk - 1 Edgewater Plaza, Staten Island, NY 10301, (718) 876-8484</li> </ul>

head2 = '''
</body>
</html>
'''














