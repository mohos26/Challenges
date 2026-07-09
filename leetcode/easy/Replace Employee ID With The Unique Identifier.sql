# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
# 09.07.2026


SELECT EmployeeUNI.unique_id, Employees.name FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;

