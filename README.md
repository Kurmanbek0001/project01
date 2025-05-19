Project Structure

hospital-system/
├── database.py              # Handles DB connection and table creation
├── patients.py              # Patient model and DAO
├── doctors.py               # Doctor model and DAO
├── appointments.py          # Appointment model and DAO
├── main.py                  # Main script to run the program
└── README.md                # Project documentation


=== All Patients ===
[1] Alia Akmatova, 28, Female, 555-1234

=== All Doctors ===
[1] Dr. Kalys, Cardiologist, Mon, Wed, Fri

=== All Appointments ===
(1, 'Alia Akmatova', 'Dr. Kalys', '2025-04-25', '10:30', 'Scheduled')


Why database.py is important
Your system (patients, doctors, appointments) all need a place to store and retrieve data — this is what the database does.
In your case, you're using SQLite, a lightweight file-based database that stores data in a .db file (e.g., hospital.db).

Instead of repeating connection code in every file, you create a separate module: database.py.

This module handles two main jobs:

