from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    last_name: str
    first_name: str
    grades: List[float]
    average: float = 0.0

    def calculate_average(self) -> None:
        if self.grades:
            self.average = sum(self.grades) / len(self.grades)
        else:
            self.average = 0.0

    def to_string(self) -> str:
        grades_str = ",".join(map(str, self.grades))
        return f"{self.last_name}|{self.first_name}|{grades_str}|{self.average}"

    @classmethod
    def from_string(cls, data: str) -> 'Student':
        last_name, first_name, grades_str, average = data.strip().split('|')
        grades = [float(g) for g in grades_str.split(',')]
        return cls(last_name, first_name, grades, float(average))
