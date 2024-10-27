from typing import List

class InputValidator:
    """Utility class for input validation."""
    
    @staticmethod
    def validate_grade(grade: str) -> float:
        """Validate and convert grade input."""
        if not grade.strip():
            raise ValueError("Grade cannot be empty")
            
        try:
            grade_float = float(grade)
            
            # Check if grade has more than 2 decimal places
            if len(str(grade_float).split('.')[-1]) > 2:
                raise ValueError("Grade can have at most 2 decimal places")
                
            if 0 <= grade_float <= 100:
                return round(grade_float, 2)
            raise ValueError("Grade must be between 0 and 100")
        except ValueError as e:
            if str(e) == "could not convert string to float":
                raise ValueError("Grade must be a valid number")
            raise e

    @staticmethod
    def validate_name(name: str) -> str:
        """Validate name input."""
        if not name.strip():
            raise ValueError("Name cannot be empty")
            
        cleaned_name = name.strip()
        if not cleaned_name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces")
            
        return cleaned_name

    @staticmethod
    def get_validated_grades() -> List[float]:
        """Get and validate all grades for a student."""
        grades = []
        required_grades = 4
        
        print("\nEnter grades for each month (0-100):")
        for month in range(1, required_grades + 1):
            while True:
                try:
                    grade_input = input(f"Month {month} grade: ").strip()
                    grade = InputValidator.validate_grade(grade_input)
                    grades.append(grade)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
        
        if len(grades) != required_grades:
            raise ValueError(f"Exactly {required_grades} grades are required")
            
        return grades

    @staticmethod
    def confirm_action(prompt: str) -> bool:
        """Validate user confirmation for important actions."""
        while True:
            response = input(f"{prompt} (y/n): ").strip().lower()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            print("Please enter 'y' for yes or 'n' for no.")
