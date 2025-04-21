from database import create_connection

class Doctor:
    def __init__(self, id, name, specialization, available_days):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.available_days = available_days

class DoctorDAO:
    def insert(self, doctor):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO doctors (name, specialization, available_days) VALUES (?, ?, ?)',
                           (doctor.name, doctor.specialization, doctor.available_days))
            conn.commit()

    def get_all(self):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM doctors')
            return cursor.fetchall()

    def delete(self, doctor_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM doctors WHERE id=?', (doctor_id,))
            conn.commit()

    def update(self, doctor):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE doctors SET name=?, specialization=?, available_days=? WHERE id=?',
                           (doctor.name, doctor.specialization, doctor.available_days, doctor.id))
            conn.commit()
