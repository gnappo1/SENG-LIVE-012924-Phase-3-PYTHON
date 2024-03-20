from classes.__init__ import CURSOR, CONN
import re

class Doctor:
    all = {}

    def __init__(self, full_name, phone_number, specialty, id=None):
        self.full_name = full_name
        self.phone_number = phone_number
        self.specialty = specialty
        self.id = id

    def __repr__(self):
        return f"<Doctor {self.id}: {self.full_name}, {self.phone_number}>"

    #! Attributes and Properties

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        if not isinstance(full_name, str):
            raise TypeError("Full name must be a string")
        elif not re.match(r"^[a-zA-Z]+ [a-zA-Z]+$", full_name):
            raise ValueError(
                "Full name cannot be empty and must contain two words separated by a space"
            )
        else:
            self._full_name = full_name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be a string")
        elif not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            raise ValueError("Phone must be in format: 123-456-7890")
        else:
            self._phone = phone

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        if not isinstance(specialty, str):
            raise TypeError("Specialty must be a string")
        elif not specialty.strip():
            raise ValueError("Specialty must be at least one character long")
        else:
            self._specialty = specialty

    #! Association Methods

    def appointments(self):
        from classes.appointment import Appointment

        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM appointments
                    WHERE doctor_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                return [Appointment(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        except Exception as e:
            print("Error fetching appointments:", e)

    def patients(self):
        try:
            with CONN:
                return list({appt.patient for appt in self.appointments()})
        except Exception as e:
            print("Error fetching patients:", e)

    #! Helper Methods

    #! Utility ORM Class Methods

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS doctors (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        phone_number TEXT,
                        specialty TEXT
                    );
                    """
                )
        except Exception as e:
            print("Error creating table:", e)

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DROP TABLE IF EXISTS doctors;
                    """
                )
        except Exception as e:
            print("Error dropping table:", e)

    @classmethod
    def create(cls, full_name, phone_number, specialty):
        try:
            with CONN:
                new_doctor = cls(full_name, phone_number, specialty)
                new_doctor.save()
                return new_doctor
        except Exception as e:
            print("Error creating doctor:", e)

    @classmethod
    def new_from_db(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM doctors
                    ORDER BY id DESC
                    LIMIT 1;
                    """
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0])
        except Exception as e:
            print("Error fetching doctor from db:", e)

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM doctors;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1], row[2], row[3], row[0]) for row in rows]
        except Exception as e:
            print("Error fetching all doctors:", e)

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM doctors
                    WHERE full_name is ?;
                    """,
                    (name,),
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error finding doctor by name:", e)

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM doctors
                    WHERE id is ?;
                    """,
                    (id,),
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error finding doctor by ID:", e)

    @classmethod
    def find_by(cls, attr, val):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM doctors
                WHERE {attr} is ?;
            """,
                (val,),
            )
            row = CURSOR.fetchone()
            return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            return e

    @classmethod
    def find_or_create_by(cls, full_name, phone_number, specialty):
        try:
            existing_doctor = cls.find_by_name(full_name)
            if existing_doctor:
                return existing_doctor
            else:
                return cls.create(full_name, phone_number, specialty)
        except Exception as e:
            print("Error finding or creating doctor:", e)

    #! Utility ORM Instance Methods
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO doctors (full_name, phone_number, specialty)
                    VALUES (?, ?, ?);
                    """,
                    (self.full_name, self.phone_number, self.specialty),
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
                return self
        except Exception as e:
            print("Error saving doctor:", e)

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE doctors
                    SET full_name = ?, phone_number = ?, specialty = ?
                    WHERE id = ?
                    """,
                    (self.full_name, self.phone_number, self.specialty, self.id),
                )
                CONN.commit()
                type(self).all[self] = self
                return self
        except Exception as e:
            print("Error updating doctor:", e)

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM doctors
                    WHERE id = ?
                    """,
                    (self.id,),
                )
                CONN.commit()
                # Remove memoized object
                del type(self).all[self.id]
                # Nullify id
                self.id = None
        except Exception as e:
            print("Error deleting doctor:", e)

    #! Exercises
    @classmethod
    def doctor_with_most_patients(cls):
        pass
    
    @classmethod
    def average_patient_count_per_doctor(cls):
        pass
    
    @classmethod
    def total_doctor_count(cls):
        pass
    
    @classmethod
    def doctor_with_most_patients(cls):
        pass