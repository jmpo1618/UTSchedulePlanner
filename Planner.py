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

        self.grid = [[None] * 6] * 48
        self.course_set = set()

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
            days = [d.text for d in columns[1].findAll('span')]
            hour = [d.text for d in columns[2].findAll('span')]
            room = [d.text for d in columns[3].findAll('span')]
            instructor = columns[4].span.text
            new_course = Course(unique, days, hour, room, instructor)
            self.course_set.add(new_course)
            print new_course.parse_hours()
