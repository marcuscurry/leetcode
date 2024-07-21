"""
Author: Marcus Curry
Date: 07/18/2024
GitHub: https://github.com/marcuscurry/leetcode/tree/main

Leetcode Question: https://leetcode.com/problems/second-highest-salary/description/
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
