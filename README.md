# Employee Management System

## Overview
This project is a Python-based Employee Management System that enables users to perform CRUD (Create, Read, Update, Delete) operations on employee data stored in a CSV file. The program includes features such as:

- Adding new employees.
- Updating existing employee details.
- Deleting employee records.
- Searching for an employee by their ID.
- Listing all employees.

---

## Approach

### Problem Diagnosis
An issue occurred when attempting to load employee data from a CSV file with a header row. The program misinterpreted the header row as data, leading to a `ValueError` when attempting to convert the string 'Salary' to a float.

### Solution Implementation

1. **Header Row Handling:**
   - Modified the `load_data` method to skip the header row using the `next(reader, None)` function.
   - Ensured only valid employee data rows were processed.

2. **Data Validation:**
   - Ensured the program gracefully handles empty or malformed rows in the CSV file.

3. **Testing:**
   - Tested the program with various scenarios, including:
     - Valid CSV files with headers.
     - Missing or incomplete rows.
     - Empty files.
     - Files without headers.

---

## Tools Used

1. **Python Modules:**
   - `csv`: For reading and writing CSV files.
   - `os`: To check the existence of the CSV file.
   - `re`: For validating email formats.

2. **Standard File I/O:**
   - Used to manage and persist employee data in a CSV file.

3. **Debugging:**
   - Leveraged Python's exception traceback for identifying the source of errors.
   - Applied step-by-step debugging to isolate and resolve the issue.

---

## Challenges Faced

1. **CSV Structure Assumptions:**
   - The initial implementation assumed all rows in the file were employee data, resulting in the processing of the header row as data.

2. **Error Handling:**
   - Ensured robust handling of edge cases, such as malformed rows or empty files.

3. **Testing for Edge Cases:**
   - Simulated various scenarios to verify the program's robustness, including testing with files containing invalid or incomplete data.

---

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Place a CSV file named `employees.csv` in the same directory as the script, formatted as follows:
   ```csv
   ID,Name,Position,Salary,Email
   1,John Doe,Manager,50000,john.doe@example.com
   2,Jane Smith,Developer,40000,jane.smith@example.com
   ```
3. Run the script using the command:
   ```bash
   python employee_manager.py
   ```
4. Follow the menu-driven interface to manage employee data.

---

## Features
- **Add Employee:** Add a new employee with ID, name, position, salary, and email.
- **Update Employee:** Update specific details of an employee.
- **Delete Employee:** Remove an employee by their ID.
- **Search Employee:** Search for an employee by their ID.
- **List All Employees:** View all employees in the system.


