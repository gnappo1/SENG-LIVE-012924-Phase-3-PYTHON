import datetime


class Appointment:
    all = []

    def __init__(self, reason_for_visit, date):
        self.reason_for_visit = reason_for_visit
        self.date = date
        type(self).all.append(self)