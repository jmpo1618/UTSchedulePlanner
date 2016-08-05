import twill
from twill.commands import *
from BeautifulSoup import BeautifulSoup
import StringIO

print "EID:"
eid = raw_input()
print "Password:"
password = raw_input()

url = 'http://utdirect.utexas.edu/apps/registrar/course_schedule/20169'
go(url)
fv('1', 'IDToken1', eid)
fv('1', 'IDToken2', password)
submit()
submit()
print "Logged in successfully."

url = url + '/51585/'
go(url)
html = StringIO.StringIO()
twill.set_output(html)
show()
soup = BeautifulSoup(html.getvalue())
table = soup.find('table')
for row in table.findAll('tr')[1:]:
    columns = row.findAll('td')
    unique = columns[0].string
    days = columns[1].span.text
    hour = columns[2].span.text
    room = columns[3].span.text
    instructor = columns[4].span.text
    print unique, days, hour, room, instructor
