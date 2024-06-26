import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smartattendancesystem-27003-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "201047":
        {
            'name': "Santosh Patel",
            'major': "CS",
            'starting_year': 2020,
            'total_attendance': 0,
            'standing': "A",
            'year': 4,
            'last_attendance_time': "2024-05-23 00:17:47"
        },
    "201099":
        {
            'name': "Priyanshu Patel",
            'major': "Biotech",
            'starting_year': 2021,
            'total_attendance': 0,
            'standing': "A",
            'year': 3,
            'last_attendance_time': "2024-05-23 00:17:47"
        }
}

for key, value in data.items():
    ref.child(key).set(value)