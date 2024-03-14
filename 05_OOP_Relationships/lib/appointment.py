from datetime import datetime


class Appointment:
    all = []

    def __init__(self, reason_for_visit, date, doctor, patient):
        self.reason_for_visit = reason_for_visit
        self.date = date
        self.doctor = doctor
        self.patient = patient
        type(self).all.append(self)

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, doctor_instance):
        from lib.doctor import Doctor

        if isinstance(doctor_instance, Doctor):
            self._doctor = doctor_instance
        else:
            raise TypeError("Doctors must be instances of the class Doctor")

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient_instance):
        from lib.patient import Patient

        if isinstance(patient_instance, Patient):
            self._patient = patient_instance
        else:
            raise TypeError("Patients must be instances of the class Patient")

    def __repr__(self):
        return f"""
        Appointment:
            Reason: {self.reason_for_visit}
            Date: {self.date}
        """

    @classmethod
    def next_three_appts_by_date_asc(cls):
        try:
            return sorted(
                cls.all,
                key=lambda appt: datetime.strptime(appt.date, "%m/%d/%y"),
                reverse=True,
            )[0:3]
        except Exception as e:
            return e
