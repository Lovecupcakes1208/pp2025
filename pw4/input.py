import math

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Invalid input. Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Invalid input. Please enter a number.")

def input_students():
    print("\n-- INPUT STUDENTS --")
    num = get_int("Number of students: ")
    
    data = []
    for i in range(num):
        print(f"Student #{i+1}")
        sid = input("  Student ID: ")
        name = input("  Student Name: ")
        dob = input("  Student DoB(dd-mm-yyyy): ")
        data.append((sid, name, dob))
    return data

def input_courses():
    print("\n-- INPUT COURSES --")
    num = get_int("Number of courses: ")
    
    data = []
    for i in range(num):
        print(f"Course #{i+1}")
        cid = input("  Course ID: ")
        name = input("  Course Name: ")
        cre = get_int("  Credits: ")
        data.append((cid, name, cre))
    return data

def input_marks(students, courses):
    print("\n-- INPUT MARKS --")
    for c in courses:
        print(f"\nEntering marks for: {c.name} (ID: {c.cid})")
        for s in students:
            
            val = get_float(f"  Mark for {s.name}: ")
            
            val = math.floor(val * 10) / 10

            s.add_mark(c.cid, val)