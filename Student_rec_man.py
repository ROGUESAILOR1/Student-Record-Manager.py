import csv
import re
import os


class StudentRecordManager:
    def __init__(self,):
        self.filename = "StudentsRecord.csv"
        self.fields=["Student_ID", "Name", "Age", "Grade"]
    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")

        self.studentrecord={
                "Student_ID": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade
            }

        f_exits = os.path.exists(self.filename)
        with open('StudentsRecord.csv',"a" if f_exits else  "w", newline='') as file:
            writer=csv.DictWriter(file, fieldnames=self.fields)
            if not f_exits:
                writer.writeheader()
            writer.writerow(self.studentrecord)
    def remove_student(self):
        student_id = input("Enter the student ID to remove: ")
        rows = []
        with open(self.filename, newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                if row["Student_ID"] != student_id:
                    rows.append(row)
        with open(self.filename, "w", newline="") as file:
            writer=csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
    def update_student(self):
        student_id = input("Enter the student ID to update: ")
        with open(self.filename,"r") as file:
            rows=[]
            reader=csv.DictReader(file)
            for row in reader:
                if row["Student_ID"]==student_id:
                    row["Name"]=input("Type name to update: ")
                    row["Age"]=input("Type age to update: ")
                    row["Grade"]=input("Type grade to update: ")
                    rows.append(row)
        with open(self.filename, "w", newline="") as file:
            writer=csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
    def search_student(self):
        student_id = input("Enter the student ID to search: ")
        with open(self.filename, newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                if row["Student_ID"] == student_id:
                    print(f"Student found: {row}")
                    return row
        print("Student not found.")
        return None

SRM=StudentRecordManager()

print("""welcome to Student Record Manager
         1. Add Student
         2. Remove Student
         3. Update Record
         4. Search Student
         5. Exit""")
while True:
    choice=input("Please select your choice: ")
    if choice=="1":
        SRM.add_student()
    elif choice=="2":
        SRM.remove_student()
    elif choice=="3":
        SRM.update_student()
    elif choice=="4":
        SRM.search_student()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")