from datetime import datetime
class Patient:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def appointments(self):  #! giving me back JUST MY appointments
        from lib.appointment import Appointment

        return [appt for appt in Appointment.all if appt.patient == self]

    def doctors(self):
        # This association through method SHOULD ENFORCE UNIQUENESS
        return list({appt.doctor for appt in self.appointments()})

    def past_appointments(self):
        return [
            appt
            for appt in self.appointments()
            if datetime.strptime(appt.date, "%m/%d/%y") < datetime.now()
        ]

    def future_appointments(self):
        return list(set(self.appointments()) - set(self.past_appointments()))