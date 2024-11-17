from time import sleep
import os

studentsList = []

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getName() -> str:
    while True:
        clear()
        name: str = input("Student name: ").strip()
        if name:
            return name
        print("Invalid name. Please try again.")
        sleep(2)

def ableStudent(grade: float) -> str:
    return "Retained" if grade < 5 else "Approved"

def getGrade(name: str) -> float:
    while True:
        clear()
        try:
            grade: float = float(input(f"{name}'s average grade: "))
            return grade
        except ValueError:
            print("Invalid grade. Please try again.")
            sleep(2)

def unifyToDict(name: str, grade: float) -> dict:
    return {
        "Student Name": name,
        "Student Average Grade": grade,
        "Status": ableStudent(grade),
    }

def unifyAll() -> dict:
    name = getName()
    grade = getGrade(name)
    student_data = unifyToDict(name, grade)
    return student_data

def countRetainedStudents(listS: list) -> int:
    return sum(1 for student in listS if student["Status"] == "Retained")

def mainAsk(listS: list):
    while True:
        clear()
        print("What do you want to do?")
        print("[L]ist of students")
        print("[C]reate student")
        print("[R]etained students count")
        print("[E]xit")
        print("")
        choice = input("Your choice: ").strip().lower()

        if choice == "l":
            clear()
            if not listS:
                print("No students in the list.")
            else:
                print("List of Students:")
                for student in listS:
                    print(f"- {student['Student Name']}: {student['Student Average Grade']} ({student['Status']})")
                retained_count = countRetainedStudents(listS)
                print(f"\nNumber of retained students: {retained_count}")
            input("\nPress Enter to return to the menu...")
            
        elif choice == "c":
            student = unifyAll()
            listS.append(student)
            print("\nStudent added successfully!")
            sleep(2)
            input("\nPress Enter to return to the menu...")
            
        elif choice == "e":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 'L', 'C', or 'E'.")
            sleep(2)

mainAsk(studentsList)