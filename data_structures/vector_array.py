from typing import List, Optional
from models.student import Student

class StudentVector:
    """Vector array implementation for student data."""
    
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a student to the vector."""
        self.students.append(student)

    def remove_student(self, last_name: str, first_name: str) -> bool:
        """Remove a student from the vector."""
        for i, student in enumerate(self.students):
            if student.last_name == last_name and student.first_name == first_name:
                self.students.pop(i)
                return True
        return False

    def get_student(self, last_name: str, first_name: str) -> Optional[Student]:
        """Retrieve a student from the vector."""
        for student in self.students:
            if student.last_name == last_name and student.first_name == first_name:
                return student
        return None

    def update_student_grades(self, last_name: str, first_name: str, grades: List[float]) -> bool:
        """Update student grades."""
        student = self.get_student(last_name, first_name)
        if student:
            student.grades = grades
            student.calculate_average()
            return True
        return False

    def get_all_students(self) -> List[Student]:
        """Return all students."""
        return self.students

    def sort_by_last_name(self, reverse: bool = False) -> List[Student]:
        """Sort students by last name."""
        return sorted(self.students, key=lambda x: x.last_name.lower(), reverse=reverse)

    def sort_by_average(self, reverse: bool = False) -> List[Student]:
        """Sort students by average grade."""
        return sorted(self.students, key=lambda x: x.average, reverse=reverse)

    def search_by_name(self, name: str) -> List[Student]:
        """Search students by partial name match (case-insensitive)."""
        name = name.lower()
        return [
            student for student in self.students
            if name in student.first_name.lower() or name in student.last_name.lower()
        ]

    def search_by_grade_range(self, min_grade: float, max_grade: float) -> List[Student]:
        """Search students by average grade range."""
        return [
            student for student in self.students
            if min_grade <= student.average <= max_grade
        ]
