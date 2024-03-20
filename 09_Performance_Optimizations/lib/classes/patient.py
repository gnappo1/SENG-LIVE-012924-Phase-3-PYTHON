from classes.__init__ import CURSOR, CONN
import re

class Patient:
    all = {}

    def __init__(self, full_name, email, phone, id=None):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.id = id

    def __repr__(self):
        return f"<Patient {self.id}: {self.full_name}, {self.email}, {self.phone}>"

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        elif not re.match(r"^\w+@\w+\.\w+$", email):
            raise ValueError("Email must be in format: yourcompany@domain.com")
        else:
            self._email = email

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

    #! Association Methods

    def appointments(self):
        from classes.appointment import Appointment

        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM appointments
                    WHERE patient_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                return [
                    Appointment(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows
                ]
        except Exception as e:
            print("Error fetching appointments:", e)

    def doctors(self):
        try:
            with CONN:
                return list({appt.doctor for appt in self.appointments()})
        except Exception as e:
            print("Error fetching doctors:", e)

    #! Helper Methods

    #! Utility ORM Class Methods

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        email TEXT,
                        phone_number TEXT
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
                    DROP TABLE IF EXISTS patients;
                    """
                )
        except Exception as e:
            print("Error dropping table:", e)

    @classmethod
    def create(cls, full_name, email, phone):
        try:
            with CONN:
                # Initialize a new obj with the info provided
                new_patient = cls(full_name, email, phone)
                # save the obj to make sure it's in the db
                new_patient.save()
                return new_patient
        except Exception as e:
            print("Error creating patient:", e)

    @classmethod
    def new_from_db(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM patients
                    ORDER BY id DESC
                    LIMIT 1;
                    """
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error fetching patient from db:", e)

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM patients;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1], row[2], row[3], row[0]) for row in rows]
        except Exception as e:
            print("Error fetching all patients:", e)

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM patients
                    WHERE full_name is ?;
                    """,
                    (name,),
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error finding patient by name:", e)

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM patients
                    WHERE id is ?;
                    """,
                    (id,),
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error finding patient by ID:", e)

    @classmethod
    def find_by(cls, attr, val):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                    SELECT * FROM patients
                    WHERE {attr} is ?;
                    """,
                    (val,),
                )
                row = CURSOR.fetchone()
                return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print("Error finding patient by attribute:", e)

    @classmethod
    def find_or_create_by(cls, full_name, email, phone):
        try:
            with CONN:
                return cls.find_by_name(full_name) or cls.create(full_name, email, phone)
        except Exception as e:
            print("Error finding or creating patient:", e)

    #! Utility ORM Instance Methods

    def save(self):
        try:
            with CONN:
                # self is only instantiated so it has no id
                CURSOR.execute(
                    """
                    INSERT INTO patients (full_name, email, phone_number)
                    VALUES (?, ?, ?);
                    """,
                    (self.full_name, self.email, self.phone),
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
                return self
        except Exception as e:
            print("Error saving patient:", e)

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE patients
                    SET full_name = ?, email = ?, phone_number = ?
                    WHERE id = ?
                    """,
                    (self.full_name, self.email, self.phone, self.id),
                )
                CONN.commit()
                type(self).all[self] = self
                return self
        except Exception as e:
            print("Error updating patient:", e)

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM patients
                    WHERE id = ?
                    """,
                    (self.id,),
                )
                CONN.commit()
                #! Remove memoized object
                del type(self).all[self.id]
                #! Nullify id
                self.id = None
                return self
        except Exception as e:
            print("Error deleting patient:", e)

    #! Exercises
    
    def total_appointments_for_patient(self):
        pass

    @classmethod
    def all_minors_sorted_by_age_ascending(cls):
        pass