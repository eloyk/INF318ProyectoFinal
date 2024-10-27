import os
from typing import List
from models.student import Student

class StudentFileStorage:
    """File-based storage implementation for student data."""
    
    def __init__(self, filename: str = "data/students.txt"):
        self.filename = filename
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def save_students(self, students: List[Student]) -> None:
        """Save all students to file."""
        # Ensure directory exists before saving
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'w', encoding='utf-8') as f:
            for student in students:
                f.write(f"{student.to_string()}\n")

    def load_students(self) -> List[Student]:
        """Load all students from file."""
        students = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        students.append(Student.from_string(line))
        except FileNotFoundError:
            pass
        return students
