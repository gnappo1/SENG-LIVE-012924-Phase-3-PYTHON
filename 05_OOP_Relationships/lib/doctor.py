from .appointment import *


class Doctor:
    all = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all.append(self)

    def appointments(self): #! giving me back JUST MY appointments
        from lib.appointment import Appointment 
        return [appt for appt in Appointment.all if appt.doctor == self]

    def patients(self):
        # This association through method SHOULD ENFORCE UNIQUENESS
        return list({appt.patient for appt in self.appointments()})
