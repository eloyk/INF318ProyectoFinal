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
        
        students = self.file_storage.load_students()
        for student in students:
            self.vector_storage.add_student(student)

    def add_student(self):
        try:
            print("\nIngresa los detalles para agregar el estudiante:")
            last_name = self.input_validator.validate_name(input("Apellidos: "))
            first_name = self.input_validator.validate_name(input("Nombres: "))
            
            if self.vector_storage.get_student(last_name, first_name):
                print("Error: Ya existe un estudiante con el mismo nombre y apellido!")
                return
                
            grades = self.input_validator.get_validated_grades()
            
            student = Student(last_name, first_name, grades)
            student.calculate_average()
            
            self.vector_storage.add_student(student)
            self.save_data()
            print("\nEstudiante agregado de manera satisfactoria!")
        except ValueError as e:
            print(f"\nError: {e}")

    def remove_student(self):
        try:
            print("\nIngresa los detalles para eliminar el estudiante:")
            last_name = self.input_validator.validate_name(input("Apellidos: "))
            first_name = self.input_validator.validate_name(input("Nombres: "))
            
            student = self.vector_storage.get_student(last_name, first_name)
            if not student:
                print("\nError: No se encontro estudiante!")
                return
                
            print(f"\nEstudiante encontrado:")
            print(f"Nombre: {student.last_name}, {student.first_name}")
            print(f"Promedio: {student.average:.2f}")
            
            if self.input_validator.confirm_action("Estas seguro que quieres eliminar este estudiante?"):
                if self.vector_storage.remove_student(last_name, first_name):
                    self.save_data()
                    print("\nEstudiante eliminado de manera satisfactoria!")
            else:
                print("\nOperacion cancelada.")
        except ValueError as e:
            print(f"\nError: {e}")

    def update_student(self):
        try:
            print("\nIngresa los detalles para actualizar el estudiante:")
            last_name = self.input_validator.validate_name(input("Apellidos: "))
            first_name = self.input_validator.validate_name(input("Nombres: "))
            
            student = self.vector_storage.get_student(last_name, first_name)
            if not student:
                print("\nError: No se encontro estudiante!")
                return
                
            print(f"\nCalificaciones actuales para {student.first_name} {student.last_name}:")
            for i, grade in enumerate(student.grades, 1):
                print(f"Mes {i}: {grade}")
                
            if self.input_validator.confirm_action("Quieres actualizar estas calificaciones?"):
                grades = self.input_validator.get_validated_grades()
                self.vector_storage.update_student_grades(last_name, first_name, grades)
                self.save_data()
                print("\nCalificaciones actualizadas de manera satisfactoria!")
            else:
                print("\nOperacion cancelada.")
        except ValueError as e:
            print(f"\nError: {e}")

    def display_students(self, students=None):
        if students is None:
            students = self.vector_storage.get_all_students()
        
        if not students:
            print("\nNo se encontro estudiante!")
            return
        
        print("\nReporte de calificaciones del estudiante:")
        print("-" * 60)
        for student in students:
            print(f"Nombre: {student.last_name}, {student.first_name}")
            for i, grade in enumerate(student.grades, 1):
                print(f"Mes {i}: {grade:.2f}")
            print(f"Promedio: {student.average:.2f}")
            print("-" * 60)

    def sort_students(self):
        if not self.vector_storage.get_all_students():
            print("\nNo hay estudiantes para ordenar!")
            return

        print("\nOpciones de ordenacion:")
        print("1. Ordenar por apellidos (A-Z)")
        print("2. Ordenar por apellidos (Z-A)")
        print("3. Odenar por promedio de calificacion (De mayor a menor)")
        print("4. Odenar por promedio de calificacion (De menor a mayor)")
        
        choice = input("\nIngresa tu eleccion (1-4): ")
        
        if choice == "1":
            sorted_students = self.vector_storage.sort_by_last_name(reverse=False)
            print("\nOrdenar por apellidos (A-Z):")
        elif choice == "2":
            sorted_students = self.vector_storage.sort_by_last_name(reverse=True)
            print("\nOrdenar por apellidos (Z-A):")
        elif choice == "3":
            sorted_students = self.vector_storage.sort_by_average(reverse=True)
            print("\nOdenar por promedio de calificacion (De mayor a menor):")
        elif choice == "4":
            sorted_students = self.vector_storage.sort_by_average(reverse=False)
            print("\nOdenar por promedio de calificacion (De menor a mayor):")
        else:
            print("\nError: Seleccion invalida!")
            return
            
        self.display_students(sorted_students)

    def search_students(self):
        if not self.vector_storage.get_all_students():
            print("\nNo hay estudiante para buscar!")
            return

        print("\nOpciones de busqueda:")
        print("1. Buscar por nombre")
        print("2. Buscar por rango de calificaciones")
        
        choice = input("\nIngresa tu eleccion (1-2): ")
        
        if choice == "1":
            name = input("\nIngresa el nombre para la busqueda: ").strip()
            if not name:
                print("Error: El termino de busqueda no puede estar vacio!")
                return
            results = self.vector_storage.search_by_name(name)
            print(f"\nResultados de la busqeda para '{name}':")
            
        elif choice == "2":
            try:
                min_grade = self.input_validator.validate_grade(input("\nIngresa la calificacion minima: "))
                max_grade = self.input_validator.validate_grade(input("Ingresa la calificacion maxima: "))
                if min_grade > max_grade:
                    min_grade, max_grade = max_grade, min_grade
                results = self.vector_storage.search_by_grade_range(min_grade, max_grade)
                print(f"\nEstudiante con promedio de calificaiones entre {min_grade:.2f} y {max_grade:.2f}:")
            except ValueError as e:
                print(f"\nError: {e}")
                return
        else:
            print("\nError: Seleccion invalida!")
            return
            
        self.display_students(results)

    def export_data(self):
        if not self.vector_storage.get_all_students():
            print("\nNo hay estudiantes para exportar!")
            return

        print("\nOpciones de exportacion:")
        print("1. Exportar a CSV")
        print("2. Exportar a JSON")
        print("3. Exportar a XML")
        print("4. Exportar a todos los formatos")
        
        choice = input("\nIngresa tu eleccion (1-4): ")
        students = self.vector_storage.get_all_students()
        
        try:
            if choice == "1":
                DataExporter.export_to_csv(students)
                print("\nDatos CSV exportados de manera satisfactoria!")
            elif choice == "2":
                DataExporter.export_to_json(students)
                print("\nDatos JSON exportados de manera satisfactoria!")
            elif choice == "3":
                XMLGenerator.generate_xml(students)
                print("\nDatos XML exportados de manera satisfactoria!")
            elif choice == "4":
                DataExporter.export_to_csv(students)
                DataExporter.export_to_json(students)
                XMLGenerator.generate_xml(students)
                print("\nDatos exportados a todos los formatos de manera satisfactoria!")
            else:
                print("\nError: Seleccion invalida!")
        except Exception as e:
            print(f"\nError durante la exportacion: {e}")

    def save_data(self):
        students = self.vector_storage.get_all_students()
        self.file_storage.save_students(students)
        XMLGenerator.generate_xml(students)

    def run(self):
        while True:
            print("\nSistema de gestión de calificaciones de estudiantes")
            print("1. Agregar Estudiante")
            print("2. Eliminar Estudiante")
            print("3. Actualizar Calificaciones")
            print("4. Mostrar Todos los Estudiantes")
            print("5. Ordenar Estudiantes")
            print("6. Buscar Estudiantes")
            print("7. Exportar Datos")
            print("8. Salir")
            
            choice = input("\nIngresa tu eleccion (1-8): ")
            
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
                print("Hasta la proxima!")
                break
            else:
                print("\nError: Seleccion invalida! Por favor intente nuevamente.")

if __name__ == "__main__":
    system = GradeManagementSystem()
    system.run()
