class Course(object):

    DAYS = {'M': 0, 'T': 1, 'W': 2, 'TH': 3, 'F': 4, 'S': 5}

    def __init__(self, unique, days, hours, room, instructor):
        self.unique = unique
        self.days = days
        self.hours = hours
        self.room = room
        self.instructor = instructor

    def __hash__(self):
        return hash(self.unique)

    def __eq__(self, other):
        return self.unique == other.unique

    def parse_days(self):
        result = []
        for section in self.days:
            group = []
            for i in range(len(section)):
                if (section[i] == 'T' and i < len(section) - 1
                   and section[i + 1] == 'H'):
                    group.append(self.DAYS['TH'])
                elif not section[i] == 'H':
                    group.append(self.DAYS[section[i]])
            result.append(group)
        return result

    def parse_hours(self):
        pass
