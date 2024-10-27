import csv
import json
import os
from typing import List
from models.student import Student

class DataExporter:
    """Handles exporting student data to different formats."""
    
    @staticmethod
    def export_to_csv(students: List[Student], filename: str = "data/students.csv") -> None:
        """Export student data to CSV format."""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(['Last Name', 'First Name', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Average'])
            
            # Write student data
            for student in students:
                row = [student.last_name, student.first_name]
                row.extend(student.grades)
                row.append(student.average)
                writer.writerow(row)

    @staticmethod
    def export_to_json(students: List[Student], filename: str = "data/students.json") -> None:
        """Export student data to JSON format."""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = []
        for student in students:
            student_data = {
                'lastName': student.last_name,
                'firstName': student.first_name,
                'grades': {f'month{i+1}': grade for i, grade in enumerate(student.grades)},
                'average': student.average
            }
            data.append(student_data)
            
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2)
