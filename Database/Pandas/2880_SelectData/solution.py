"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.
The result format is in the following example.

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age |
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.query("student_id == 101")[['name', 'age']]


if __name__ == '__main__':
    student_data = {
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    }

    t1 = pd.DataFrame(student_data)
    print(selectData(t1))

"""
Question is a little tricky , it's testing on the use of either loc or query functions.

Use loc as follows :
df.loc[df[column_name] put the filter here] [[name of the columns to returned]]

or use the query as follows :
df.query("column name conditon")[[name of the columns]]
"""