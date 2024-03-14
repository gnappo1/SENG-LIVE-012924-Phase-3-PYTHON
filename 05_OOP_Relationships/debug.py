#!/usr/bin/env python3

from lib.pet import Pet
from lib.owner import Owner


# pat = Owner(
#     "Pat",
#     "Jones",
# )
# rose = Owner(
#     "Rose",
#     "Smith",
# )
# joe = Owner("Joe", "Jones")
# theresa = Owner("Theresa", "Jones")

# taco = Pet("Taco", "Cat", pat)
# fido = Pet("Fido", "Dog", rose)
# princess = Pet("Princess", "Fish", theresa)


from lib.appointment import Appointment
from lib.doctor import Doctor
from lib.patient import Patient

jimmy = Patient("Jimmy")
patty = Patient("Patty")
may = Patient("May")

rosenbaum = Doctor("Dr. Rosenbaum", "Gynocology")
williams = Doctor("Dr. Williams", "Oncology")


Appointment("Stomach issues.", "5/25/23", rosenbaum, may)
Appointment("Non-stop migrains", "5/26/23", rosenbaum, patty)
Appointment("Legs always sore in the mornings", "5/23/23", williams, jimmy, )
Appointment(
    "Feels light-headed when jogging",
    "5/12/23",
    williams,
    patty
)
Appointment(
    "Can't keep food down",
    "5/30/23",
    rosenbaum,
    may,
)
Appointment(
    "Can't keep food up",
    "5/31/23",
    rosenbaum,
    may,
)
Appointment(
    "Can't keep food up",
    "5/31/24",
    rosenbaum,
    may,
)


import ipdb

ipdb.set_trace()
