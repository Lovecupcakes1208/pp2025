# Import modules
from domains.student import Student
from domains.course import Course
import input as inp  
import output as out
import sys

def main():
    students = []
    courses = []

    while True:
        print("\n== STUDENT GPA SYSTEM ==")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Calculate & Show GPA")
        print("5. Exit")
        
        choice = input("Select option (1-5): ")

        if choice == '1':
            raw_students = inp.input_students()
            for s in raw_students:
                students.append(Student(s[0], s[1], s[2]))
            print(f" Added {len(raw_students)} students.")

        elif choice == '2':
            raw_courses = inp.input_courses()
            for c in raw_courses:
                courses.append(Course(c[0], c[1], c[2]))
            print(f" Added {len(raw_courses)} courses.")

        elif choice == '3':
            if not students:
                print(" Error: No students. Please use Option 1 first.")
            elif not courses:
                print(" Error: No courses. Please use Option 2 first.")
            else:
                inp.input_marks(students, courses)

        elif choice == '4':
            if not students:
                print(" Error: No data available.")
            else:
                # Calculate GPA 
                for s in students:
                    s.cal_gpa(courses)
                
                # Sort 
                students.sort(key=lambda x: x.gpa, reverse=True)
                
                # Display
                out.show_gpa_list(students)

        elif choice == '5':
            print("Exiting...")
            sys.exit(0)

        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()