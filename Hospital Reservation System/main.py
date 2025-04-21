from database import create_tables
from patients import Patient, PatientDAO
from doctors import Doctor, DoctorDAO
from appointments import Appointment, AppointmentDAO

def run():
    create_tables()

    # Add sample data
    p_dao = PatientDAO()
    d_dao = DoctorDAO()
    a_dao = AppointmentDAO()

    # Insert dummy patient
    p1 = Patient(None, "Alia Akmatova", 28, "Female", "555-1234")
    p_dao.insert(p1)

    # Insert dummy doctor
    d1 = Doctor(None, "Dr. Kalys", "Cardiologist", "Mon, Wed, Fri")
    d_dao.insert(d1)

    # Insert dummy appointment
    a1 = Appointment(None, 1, 1, "2025-04-25", "10:30", "Scheduled")
    a_dao.insert(a1)

    print("\n=== All Patients ===")
    for p in p_dao.get_all():
        print(p)

    print("\n=== All Doctors ===")
    for d in d_dao.get_all():
        print(d)

    print("\n=== All Appointments ===")
    for a in a_dao.get_all():
        print(a)

if __name__ == "__main__":
    run()
