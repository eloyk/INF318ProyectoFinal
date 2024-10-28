import os
import xml.etree.ElementTree as ET
from typing import List
from models.student import Student

class XMLGenerator:
    
    @staticmethod
    def generate_xml(students: List[Student], filename: str = "data/students.xml") -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        root = ET.Element("students")
        
        for student in students:
            student_elem = ET.SubElement(root, "student")
            
            name = ET.SubElement(student_elem, "name")
            last_name = ET.SubElement(name, "apellidos")
            last_name.text = student.last_name
            first_name = ET.SubElement(name, "nombres")
            first_name.text = student.first_name
            
            grades = ET.SubElement(student_elem, "calificaciones")
            for i, grade in enumerate(student.grades, 1):
                grade_elem = ET.SubElement(grades, f"notaMes{i}")
                grade_elem.text = str(grade)
            
            average = ET.SubElement(student_elem, "promedio")
            average.text = f"{student.average:.2f}"

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
