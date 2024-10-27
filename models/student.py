from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    """Represents a student and their grades."""
    last_name: str
    first_name: str
    grades: List[float]
    average: float = 0.0

    def calculate_average(self) -> None:
        """Calculate the average grade for the student."""
        if self.grades:
            self.average = sum(self.grades) / len(self.grades)
        else:
            self.average = 0.0

    def to_string(self) -> str:
        """Convert student data to string format for file storage."""
        grades_str = ",".join(map(str, self.grades))
        return f"{self.last_name}|{self.first_name}|{grades_str}|{self.average}"

    @classmethod
    def from_string(cls, data: str) -> 'Student':
        """Create a Student instance from a string."""
        last_name, first_name, grades_str, average = data.strip().split('|')
        grades = [float(g) for g in grades_str.split(',')]
        return cls(last_name, first_name, grades, float(average))
