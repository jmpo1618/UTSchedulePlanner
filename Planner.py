from __future__ import print_function
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
        print("Logged in successfully.")

        self.grid = [[None for c in range(6)] for r in range(48)]
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
            if self._check_planner_to_add(new_course):
                self.course_set.add(new_course)
                days_to_add = new_course.parse_days()
                hours_to_add = new_course.parse_hours()
                for d in range(len(days_to_add)):
                    for h in range(hours_to_add[d][0], hours_to_add[d][1]):
                        for day in days_to_add[d]:
                            self.grid[h][day] = new_course
                print("Course successfully added.")

    def _check_planner_to_add(self, new_course):
        if new_course in self.course_set:
            print("Class already added.")
            return False
        else:
            days = new_course.parse_days()
            hours = new_course.parse_hours()
            for d in range(len(days)):
                for h in range(hours[d][0], hours[d][1]):
                    for day in days[d]:
                        currently_scheduled = self.grid[h][day]
                        if currently_scheduled is not None:
                            print("Conflicting with class:"
                                  + new_course.unique)
                            return False
            return True

    def print_schedule(self):
        print('-' * 7 * 7)
        print('|  H  ||  M  ||  T  ||  W  ||  T  ||  F  ||  S  |')
        for time in range(16, 37):
            print('-' * 7 * 7)
            current_time = time
            time_to_print = ''
            if time > 25:
                current_time -= 24
            time_to_print = str(time // 2)
            if not time % 2 == 0:
                time_to_print = time_to_print + ':30'
            else:
                time_to_print = time_to_print + ':00'
            print("|" + time_to_print + ' ' * (5 - len(time_to_print)), end='')
            for current_class in self.grid[time]:
                if current_class:
                    print('||' + current_class.unique, end='')
                else:
                    print('||     ', end='')
            print('|')
        print('-' * 7 * 7)
        self.print_course_info()

    def print_course_info(self):
        for course in self.course_set:
            print(course.unique + ':', course.hours, course.days, course.room,
                  course.instructor)
