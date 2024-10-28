from typing import List

class InputValidator:
    
    @staticmethod
    def validate_grade(grade: str) -> float:
        if not grade.strip():
            raise ValueError("La calificacion del mes no puede estar vacio")
            
        try:
            grade_float = float(grade)
            
            if len(str(grade_float).split('.')[-1]) > 2:
                raise ValueError("La calificacion del mes no puede tener mas de 2 decimales")
                
            if 0 <= grade_float <= 100:
                return round(grade_float, 2)
            raise ValueError("La calificacion debe estar entre 0 y 100")
        except ValueError as e:
            if str(e) == "No se pudo convertir a numerico el valor ingresado":
                raise ValueError("La calificacion debe ser un numero valido")
            raise e

    @staticmethod
    def validate_name(name: str) -> str:
        if not name.strip():
            raise ValueError("El nombre no puede estar vacio")
            
        cleaned_name = name.strip()
        if not cleaned_name.replace(" ", "").isalpha():
            raise ValueError("El nombre debe contener solo letras y espacios")
            
        return cleaned_name

    @staticmethod
    def get_validated_grades() -> List[float]:
        grades = []
        required_grades = 4
        
        print("\nIngrese las calificaciones para cada mes entre (0-100):")
        for month in range(1, required_grades + 1):
            while True:
                try:
                    grade_input = input(f"Mes {month} calificacion: ").strip()
                    grade = InputValidator.validate_grade(grade_input)
                    grades.append(grade)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Por favor intente nuevamente.")
        
        if len(grades) != required_grades:
            raise ValueError(f"Exactamente {required_grades} calificaciones son requeridas")
            
        return grades

    @staticmethod
    def confirm_action(prompt: str) -> bool:
        while True:
            response = input(f"{prompt} (y/n): ").strip().lower()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            print("Por favor ingrese 'y' para si o 'n' para no.")
