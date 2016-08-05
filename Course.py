class Course(object):

    DAYS = {'M': 0, 'T': 1, 'W': 2, 'TH': 3, 'F': 4, 'S': 5}

    def __init__(self, unique, days, hours, room, instructor):
        self.unique = unique
        self.days = days
        self.hours = hours
        self.room = room
        self.instructor = instructor

    def parse_days(self):
        result = []
        for i in range(len(self.days)):
            if (self.days[i] == 'T' and i < len(self.days) - 1
               and self.days[i + 1] == 'H'):
                result.append(self.DAYS['TH'])
            else:
                result.append(self.DAYS[self.days[i]])
        return result
