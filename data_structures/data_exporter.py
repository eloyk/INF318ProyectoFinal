import csv
import json
import os
from typing import List
from models.student import Student

class DataExporter:
    
    @staticmethod
    def export_to_csv(students: List[Student], filename: str = "data/students.csv") -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Apellidos', 'Nombres', 'Nota Mes 1', 'Nota Mes 2', 'Nota Mes 3', 'Nota Mes 4', 'Promedio'])
            
            for student in students:
                row = [student.last_name, student.first_name]
                row.extend(student.grades)
                row.append(student.average)
                writer.writerow(row)

    @staticmethod
    def export_to_json(students: List[Student], filename: str = "data/students.json") -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = []
        for student in students:
            student_data = {
                'apellidos': student.last_name,
                'nombres': student.first_name,
                'calificaciones': {f'notaMes{i+1}': grade for i, grade in enumerate(student.grades)},
                'promedio': student.average
            }
            data.append(student_data)
            
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2)
