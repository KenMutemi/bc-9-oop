from datetime import date

class Student(object):

    map_ = {
            'KE': 'Kenya',
            'NG': 'Nigeria',
            'UG': 'Uganda',
            'TZ': 'Tanzania'
            }

    def __init__(self, first_name, last_name, cc='KE'):
        prev_id = 0
        if prev_id:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.country = map_['cc']

    def attend_class(self, **kwargs):
        self.date = date.today()

        for key, value in kwargs.iteritems():
            print key + value

