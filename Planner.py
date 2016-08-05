import twill
import twill.commands as tc
from BeautifulSoup import BeautifulSoup
import StringIO
from Course import Course

class Planner(object):

    def __init__(self, eid, pwd):
        self.url = 'http://utdirect.utexas.edu/' \
            'apps/registrar/course_schedule/20169'
        tc.go(self.url)
        tc.fv('1', 'IDToken1', eid)
        tc.fv('1', 'IDToken2', pwd)
        tc.submit()
        tc.submit()
        print "Logged in successfully."

    def add_class(self, unique_number):
        class_url = self.url + '/' + unique_number
        tc.go(class_url)
        html = StringIO.StringIO()
        twill.set_output(html)
        tc.show()
        soup = BeautifulSoup(html.getvalue())
        table = soup.find('table')
        for row in table.findAll('tr')[1:]:
            columns = row.findAll('td')
            unique = columns[0].string
            days = columns[1].span.text
            hour = columns[2].span.text
            room = columns[3].span.text
            instructor = columns[4].span.text
            new_course = Course(unique, days, hour, room, instructor)
            print new_course
