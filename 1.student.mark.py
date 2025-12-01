import sys

students = []
courses = []
marks = {}

def input_number_of_students():
    """Input num of students"""
    try:
        num_students = int(input("Enter the num of students: "))
        if num_students >= 0:
            return num_students
        else:
            print("Num of students can't be negative bruh ")
            return 0
    except ValueError:
        print("Invalid input ~~ Enter a whole num")
        return 0

def input_student_info(num_students):
    """Input student info: id, name, DoB"""
    for i in range(num_students):
        student_id = input(f"Enter student {i+1} ID: ")
        student_name = input(f"Enter student {i+1} name: ")
        dob = input(f"Enter student {i+1} date of birth (DD-MM-YYYY): ")
        students.append((student_id, student_name, dob))

def input_number_of_courses():
    """Input num of courses"""
    try:
        num_courses = int(input("Enter the num of courses: "))
        return num_courses
    except ValueError:
        print("Invalid input ~~ Please enter a whole num")
        return 0

def input_course_info(num_courses):
    """Input course info: id, name"""
    for i in range(num_courses):
        course_id = input(f"Enter course {i+1} ID: ")
        course_name = input(f"Enter course {i+1} name: ")
        courses.append((course_id, course_name))

def select_course_and_input_marks():
    """Select a course, input marks for student"""
    if not courses:
        print("No courses available.")
        return
    print("Available courses:")
    for i, (course_id, course_name) in enumerate(courses):
        print(f"{i+1}. {course_name} ({course_id})")
        
    try:
        course_choice = int(input("Select a course by entering num: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
        
    if course_choice < 0 or course_choice >= len(courses):
        print("Invalid course selection.")
        return
        
    selected_course_id, selected_course_name = courses[course_choice]
    
    print(f"Input marks for students in {selected_course_name} ({selected_course_id}):")
    for student_id, _, _ in students:
        try:
            mark = float(input(f"Enter mark for student ID {student_id}: "))
            marks[(student_id, selected_course_id)] = mark
        except ValueError:
            print(f"Invalid mark entered for student {student_id}. Please enter a number.")


def list_courses():
    """List courses"""
    if not courses:
        print("No courses available.")
        return
    print("Available courses:")
    for course_id, course_name in courses:
        print(f"{course_id}: {course_name}")

def list_students():
    """List students"""
    if not students:
        print("No students available.")
        return
    print("Available students:")
    for student_id, student_name, _ in students:
        print(f"{student_id}: {student_name}")

def show_marks_for_selected_course(): 
    """Show student marks for a given course"""
    if not courses:
        print("No courses available.")
        return
    print("\nAvailable courses to view marks for:")
    for i, (course_id, course_name) in enumerate(courses):
        print(f"{i+1}. {course_name} ({course_id})")
        
    try:
        course_choice = int(input("Select a course by entering number: ")) - 1
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    if course_choice < 0 or course_choice >= len(courses):
        print("Invalid course selection.")
        return
        
    selected_course_id, selected_course_name = courses[course_choice]
    
    print(f"\n--- Marks for {selected_course_name} ({selected_course_id}) ---")
    
    found_marks = False
    for (student_id, course_id), mark in marks.items():
        if course_id == selected_course_id:
            student_name = next((name for s_id, name, _ in students if s_id == student_id), "Unknown")
            print(f"Student ID {student_id} ({student_name}): {mark}")
            found_marks = True
            
    if not found_marks:
        print("No marks have been recorded for this course yet.")

def main():
    num_students = 0
    num_courses = 0
    
    while True:
        print("\nStudent Mark Management System")
        print("1. Input num of students")
        print("2. Input student info")
        print("3. Input num of courses")
        print("4. Input course info")
        print("5. Select a course and input marks for students")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a given course")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input ~~ Please enter a valid number.")
            continue
            
        if choice == 1:
            num_students = input_number_of_students()
        elif choice == 2:
            if num_students == 0:
                 print("Please input the number of students first (Option 1).")
            else:
                input_student_info(num_students)
        elif choice == 3:
            num_courses = input_number_of_courses()
        elif choice == 4:
            if num_courses == 0:
                 print("Please input the number of courses first (Option 3).")
            else:
                input_course_info(num_courses)
        elif choice == 5:
            select_course_and_input_marks()
        elif choice == 6:
            list_courses()
        elif choice == 7:
            list_students()
        elif choice == 8:
            show_marks_for_selected_course()
        elif choice == 9:
            print("Exiting the system.")
            sys.exit(0)
        else:
            print("Invalid input ~~ Please enter a valid number.")

if __name__ == "__main__":
    main()