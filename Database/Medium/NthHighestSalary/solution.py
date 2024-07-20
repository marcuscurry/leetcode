"""
Author: Marcus Curry
Date: 07/20/2024
GitHub: https://github.com/marcuscurry/leetcode/tree/main

Leetcode Question: https://leetcode.com/problems/nth-highest-salary/
"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary']).reset_index()
    if employee.shape[0] < N or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        employee = employee.sort_values(by=['salary'], ascending=False).reset_index()[['salary']]
        return pd.DataFrame({f'getNthHighestSalary({N})': [employee.salary[N-1]]})

if __name__ == '__main__':
    data1 = {
        'id': [1,2,3],
        'salary': [100, 200, 300]
    }
    t1 = pd.DataFrame(data1)

    data2 = {
        'id': [1, 2],
        'salary': [100, 100]
    }
    t2 = pd.DataFrame(data2)
    print(nth_highest_salary(t1, 1))
    print(nth_highest_salary(t2, 2))