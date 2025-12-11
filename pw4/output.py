def show_gpa_list(students):
    print("\n" + "*"*40)
    print(f"{'ID':<10} | {'Name':<20} | {'GPA':<5}")
    print("-" * 40)
    
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"{s.sid:<10} | {s.name:<20} | {s.gpa:.2f}")
    print("*"*40 + "\n")