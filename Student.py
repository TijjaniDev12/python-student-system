# Python Student Record System
# Author: TijjaniDev12

students = [
    {
        "Name": "TijjaniDev12",
        "Age": 19,
        "Course": "Computer sci. & Cloud security engineer",
        "University": "SLU jigawa",
        "State": "Jigawa State",
        "Country": "Nigeria"
    },
    {
        "Name": "Ali",
        "Age": 20,
        "Course": "Medicine & surgery",
        "University": "ABU Zaria",
        "State": "Kaduna State",
        "Country": "Nigeria"
    },
    {
        "Name": "Musa",
        "Age": 24,
        "Course": "Low",
        "University": "TBU bauchi",
        "State": "Bauchi State",
        "Country": "Nigeria"
    },
    {
        "Name": "Ibrahim",
        "Age": 23,
        "Course": "Biochemistry",
        "University": "FUG gusau",
        "State": "Zamfara State",
        "Country": "Nigeria"
    },
    {
        "Name": "Sani",
        "Age": 25,
        "Course": "Business administration",
        "University": "BUK kano",
        "State": "Kano State",
        "Country": "Nigeria"
    }
]

for student in students:
    print(f"Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Course: {student['Course']}")
    print(f"University: {student['University']}")
    print(f"State: {student['State']}")
    print(f"Country: {student['Country']}")
    print()
