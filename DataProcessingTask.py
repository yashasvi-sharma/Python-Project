# Data Processing Task:
# Write a Python function that takes a dictionary of employee records as input.
# Each record should contain an employee’s name, department, and monthly salary.
# The function should return the total salary expense for each department, as well as the average salary per department.
# Make sure to handle cases where departments may have no employees.


def calculate_salary_expenses(employee_records):
    """
    Calculate total and average salary for each department.
    
    :param employee_records: Dictionary with employee data. 
                             Format: {'EmployeeName': {'department': str, 'salary': float}}
    :return: Tuple of dictionaries (total_salary, avg_salary) by department.
    """
    from collections import defaultdict

    department_totals = defaultdict(float)
    department_counts = defaultdict(int)
    
    for record in employee_records.values():
        dept = record['department']
        salary = record['salary']
        department_totals[dept] += salary
        department_counts[dept] += 1
    
    avg_salary = {dept: (department_totals[dept] / count if count > 0 else 0)
                  for dept, count in department_counts.items()}
    
    return dict(department_totals), avg_salary

# Example usage:
employees = {
    "Alice": {"department": "HR", "salary": 5000},
    "Bob": {"department": "Engineering", "salary": 7000},
    "Charlie": {"department": "HR", "salary": 4500},
    "David": {"department": "Engineering", "salary": 8000},
    "Eve": {"department": "Marketing", "salary": 6000},
}
print(calculate_salary_expenses(employees)) # Output: ({'HR': 9500.0, 'Engineering': 15000.0, 'Marketing': 6000.0}, {'HR': 4750.0, 'Engineering': 7500.0, 'Marketing': 6000.0})
