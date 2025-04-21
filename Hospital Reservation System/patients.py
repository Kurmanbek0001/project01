from database import create_connection

class Patient:
    def __init__(self, id, name, age, gender, phone):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

class PatientDAO:
    def insert(self, patient):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO patients (name, age, gender, phone) VALUES (?, ?, ?, ?)',
                           (patient.name, patient.age, patient.gender, patient.phone))
            conn.commit()

    def get_all(self):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM patients')
            return cursor.fetchall()

    def delete(self, patient_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM patients WHERE id=?', (patient_id,))
            conn.commit()

    def update(self, patient):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE patients SET name=?, age=?, gender=?, phone=? WHERE id=?',
                           (patient.name, patient.age, patient.gender, patient.phone, patient.id))
            conn.commit()
