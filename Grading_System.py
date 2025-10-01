class StudentGradingSystem:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """Add a grade if valid (0–100)."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Invalid grade {grade}. Must be 0–100.")

    def compute_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def compute_point_grade(self, average):
        return ((100 - average) + 10) / 10

    def get_remarks(self, average):
        """Determine remarks based on rules."""
        if average < 50:
            return "Dropped"
        elif average < 75:
            return "Failed"
        elif 75 <= average <= 79:
            return "Passed – Satisfactory"
        elif 80 <= average <= 84:
            return "Passed – Good"
        elif 85 <= average <= 89:
            return "Passed – Average"
        elif 90 <= average <= 99:
            return "Passed – Very Good"
        elif average == 100:
            return "Passed – Excellent"
        return "Invalid"

    def display_results(self):
        if not self.grades:
            print("No grades entered.")
            return

        avg = self.compute_average()
        point = self.compute_point_grade(avg)
        remarks = self.get_remarks(avg)

        print("\n=== Student Grading System ===")
        print(f"Grades Entered: {self.grades}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Point Grade: {point:.2f}")
        print(f"Remarks: {remarks}")

grading = StudentGradingSystem()

print("Enter grades (0–100). Type -1 to finish:")
while True:
    try:
        g = float(input("Enter grade: "))
        if g == -1:
            break
        grading.add_grade(g)
    except ValueError:
        print("Invalid input. Try again.")

grading.display_results()
