"""
176. Second-Highest Salary
Difficulty: Medium
Topics: Companies, SQL Schem, Pandas Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second-highest salary from the Employee table. If there is no second-highest salary, return null (return None in Pandas).

The result format is in the following example.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    ph = employee['salary'].unique()
    if employee.empty or len(ph) == 1:
        salary = None
        return pd.DataFrame({'SecondHighestSalary': [salary]})
    else:
        employee = employee['salary'].drop_duplicates()
        ph = employee.sort_values(ascending=False)
        salary = ph.iloc[1]
        return pd.DataFrame({'SecondHighestSalary': [salary]})


if __name__ == '__main__':
    t1 = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300]
    }

    t2 = {
        'id': [1],
        'salary': [100]
    }

    t3 = {
        'id': [1, 2],
        'salary': [100, 200]
    }

    df1 = pd.DataFrame(t1)
    df2 = pd.DataFrame(t2)
    df3 = pd.DataFrame(t3)

    print(second_highest_salary(df1))
    print(second_highest_salary(df2))
    print(second_highest_salary(df3))