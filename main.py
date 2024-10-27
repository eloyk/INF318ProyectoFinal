from data_structures.vector_array import StudentVector
from data_structures.file_storage import StudentFileStorage
from data_structures.xml_generator import XMLGenerator
from data_structures.data_exporter import DataExporter
from models.student import Student
from utils.input_validator import InputValidator

class GradeManagementSystem:
    def __init__(self):
        self.vector_storage = StudentVector()
        self.file_storage = StudentFileStorage()
        self.input_validator = InputValidator()
        
        # Load existing data
        students = self.file_storage.load_students()
        for student in students:
            self.vector_storage.add_student(student)

    def add_student(self):
        """Add a new student with grades."""
        try:
            print("\nEnter student details:")
            last_name = self.input_validator.validate_name(input("Last name: "))
            first_name = self.input_validator.validate_name(input("First name: "))
            
            # Check if student already exists
            if self.vector_storage.get_student(last_name, first_name):
                print("Error: A student with this name already exists!")
                return
                
            grades = self.input_validator.get_validated_grades()
            
            student = Student(last_name, first_name, grades)
            student.calculate_average()
            
            self.vector_storage.add_student(student)
            self.save_data()
            print("\nStudent added successfully!")
        except ValueError as e:
            print(f"\nError: {e}")

    def remove_student(self):
        """Remove a student."""
        try:
            print("\nEnter student details to remove:")
            last_name = self.input_validator.validate_name(input("Last name: "))
            first_name = self.input_validator.validate_name(input("First name: "))
            
            student = self.vector_storage.get_student(last_name, first_name)
            if not student:
                print("\nError: Student not found!")
                return
                
            # Show student details and confirm deletion
            print(f"\nStudent found:")
            print(f"Name: {student.last_name}, {student.first_name}")
            print(f"Average: {student.average:.2f}")
            
            if self.input_validator.confirm_action("Are you sure you want to remove this student?"):
                if self.vector_storage.remove_student(last_name, first_name):
                    self.save_data()
                    print("\nStudent removed successfully!")
            else:
                print("\nOperation cancelled.")
        except ValueError as e:
            print(f"\nError: {e}")

    def update_student(self):
        """Update student grades."""
        try:
            print("\nEnter student details to update:")
            last_name = self.input_validator.validate_name(input("Last name: "))
            first_name = self.input_validator.validate_name(input("First name: "))
            
            student = self.vector_storage.get_student(last_name, first_name)
            if not student:
                print("\nError: Student not found!")
                return
                
            print(f"\nCurrent grades for {student.first_name} {student.last_name}:")
            for i, grade in enumerate(student.grades, 1):
                print(f"Month {i}: {grade}")
                
            if self.input_validator.confirm_action("Do you want to update these grades?"):
                grades = self.input_validator.get_validated_grades()
                self.vector_storage.update_student_grades(last_name, first_name, grades)
                self.save_data()
                print("\nGrades updated successfully!")
            else:
                print("\nOperation cancelled.")
        except ValueError as e:
            print(f"\nError: {e}")

    def display_students(self, students=None):
        """Display students and their grades."""
        if students is None:
            students = self.vector_storage.get_all_students()
        
        if not students:
            print("\nNo students found!")
            return
        
        print("\nStudent Grade Report:")
        print("-" * 60)
        for student in students:
            print(f"Name: {student.last_name}, {student.first_name}")
            for i, grade in enumerate(student.grades, 1):
                print(f"Month {i}: {grade:.2f}")
            print(f"Average: {student.average:.2f}")
            print("-" * 60)

    def sort_students(self):
        """Sort students by different criteria."""
        if not self.vector_storage.get_all_students():
            print("\nNo students to sort!")
            return

        print("\nSort Options:")
        print("1. Sort by Last Name (A-Z)")
        print("2. Sort by Last Name (Z-A)")
        print("3. Sort by Average Grade (Highest First)")
        print("4. Sort by Average Grade (Lowest First)")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            sorted_students = self.vector_storage.sort_by_last_name(reverse=False)
            print("\nStudents sorted by last name (A-Z):")
        elif choice == "2":
            sorted_students = self.vector_storage.sort_by_last_name(reverse=True)
            print("\nStudents sorted by last name (Z-A):")
        elif choice == "3":
            sorted_students = self.vector_storage.sort_by_average(reverse=True)
            print("\nStudents sorted by average grade (Highest First):")
        elif choice == "4":
            sorted_students = self.vector_storage.sort_by_average(reverse=False)
            print("\nStudents sorted by average grade (Lowest First):")
        else:
            print("\nError: Invalid choice!")
            return
            
        self.display_students(sorted_students)

    def search_students(self):
        """Search students by different criteria."""
        if not self.vector_storage.get_all_students():
            print("\nNo students to search!")
            return

        print("\nSearch Options:")
        print("1. Search by Name")
        print("2. Search by Grade Range")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            name = input("\nEnter name to search: ").strip()
            if not name:
                print("Error: Search term cannot be empty!")
                return
            results = self.vector_storage.search_by_name(name)
            print(f"\nSearch results for '{name}':")
            
        elif choice == "2":
            try:
                min_grade = self.input_validator.validate_grade(input("\nEnter minimum grade: "))
                max_grade = self.input_validator.validate_grade(input("Enter maximum grade: "))
                if min_grade > max_grade:
                    min_grade, max_grade = max_grade, min_grade
                results = self.vector_storage.search_by_grade_range(min_grade, max_grade)
                print(f"\nStudents with average grades between {min_grade:.2f} and {max_grade:.2f}:")
            except ValueError as e:
                print(f"\nError: {e}")
                return
        else:
            print("\nError: Invalid choice!")
            return
            
        self.display_students(results)

    def export_data(self):
        """Export data to different formats."""
        if not self.vector_storage.get_all_students():
            print("\nNo students to export!")
            return

        print("\nExport Options:")
        print("1. Export to CSV")
        print("2. Export to JSON")
        print("3. Export to XML")
        print("4. Export to All Formats")
        
        choice = input("\nEnter your choice (1-4): ")
        students = self.vector_storage.get_all_students()
        
        try:
            if choice == "1":
                DataExporter.export_to_csv(students)
                print("\nData exported to CSV successfully!")
            elif choice == "2":
                DataExporter.export_to_json(students)
                print("\nData exported to JSON successfully!")
            elif choice == "3":
                XMLGenerator.generate_xml(students)
                print("\nData exported to XML successfully!")
            elif choice == "4":
                DataExporter.export_to_csv(students)
                DataExporter.export_to_json(students)
                XMLGenerator.generate_xml(students)
                print("\nData exported to all formats successfully!")
            else:
                print("\nError: Invalid choice!")
        except Exception as e:
            print(f"\nError during export: {e}")

    def save_data(self):
        """Save data to both file and XML formats."""
        students = self.vector_storage.get_all_students()
        self.file_storage.save_students(students)
        XMLGenerator.generate_xml(students)

    def run(self):
        """Main application loop."""
        while True:
            print("\nStudent Grade Management System")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Update Student Grades")
            print("4. Display All Students")
            print("5. Sort Students")
            print("6. Search Students")
            print("7. Export Data")
            print("8. Exit")
            
            choice = input("\nEnter your choice (1-8): ")
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.display_students()
            elif choice == "5":
                self.sort_students()
            elif choice == "6":
                self.search_students()
            elif choice == "7":
                self.export_data()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("\nError: Invalid choice! Please try again.")

if __name__ == "__main__":
    system = GradeManagementSystem()
    system.run()
