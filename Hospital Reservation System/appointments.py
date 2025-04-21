from database import create_connection

class Appointment:
    def __init__(self, id, patient_id, doctor_id, date, time, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status

class AppointmentDAO:
    def insert(self, appointment):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time, appointment.status))
            conn.commit()

    def get_all(self):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT a.id, p.name, d.name, a.appointment_date, a.appointment_time, a.status
                FROM appointments a
                JOIN patients p ON a.patient_id = p.id
                JOIN doctors d ON a.doctor_id = d.id
            ''')
            return cursor.fetchall()

    def update_status(self, appointment_id, new_status):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE appointments SET status=? WHERE id=?', (new_status, appointment_id))
            conn.commit()

    def delete(self, appointment_id):
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM appointments WHERE id=?', (appointment_id,))
            conn.commit()
