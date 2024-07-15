"""
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
The result format is in the following example.

Example 1:

Input:
student_data:
[   [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]]

Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
"""

import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    if student_data is None:
        return pd.DataFrame({'student_id': None, 'age': None})

    student_ids = list(map(lambda x: x[0], student_data))
    ages = list(map(lambda x: x[1], student_data))
    return pd.DataFrame({'student_id': student_ids, 'age': ages})

if __name__ == '__main__':
    t1 = [[1,15],[2,11],[3,11],[4,20]]
    print(createDataframe(t1))