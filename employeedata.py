class Employee:
    def __init__(self):
        self.EmployeeID = int(input("Enter Employee ID: "))
        self.Gender = input("Enter Gender: ")
        self.Salary = float(input("Enter Salary: "))
        self.PerformanceRating = int(input("Enter Performance Rating (out of 5): "))

class JoiningDetail:
    def __init__(self):
        self.DateOfJoining = input("Enter Date of Joining (YYYY-MM-DD): ")

class Information(Employee, JoiningDetail):
    def __init__(self):
        Employee.__init__(self)
        JoiningDetail.__init__(self)

    def display(self):
        print(f"EmployeeID: {self.EmployeeID}, Gender: {self.Gender}, Salary: {self.Salary}, "
              f"PerformanceRating: {self.PerformanceRating}, DateOfJoining: {self.DateOfJoining}")

# ---------------- Main Program ----------------
employees = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp = Information()
    employees.append(emp)

# Sort by rating (descending)
employees.sort(key=lambda x: x.PerformanceRating, reverse=True)

# Take top 3
top_employees = employees[:3]

# Sort top 3 by joining date (ascending)
top_employees.sort(key=lambda x: x.DateOfJoining)

# Display
print("\nTop 3 Employees (based on rating, sorted by Date of Joining):")
for emp in top_employees:
    emp.display()
