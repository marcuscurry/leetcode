"""
Author: Marcus Curry
Date: 07/20/2024
GitHub: https://github.com/marcuscurry/leetcode/tree/main

Leetcode Question: https://leetcode.com/problems/duplicate-emails/description/
"""

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    ret = pd.DataFrame(data=person.email.value_counts()).reset_index()
    ret.columns = ['Email', 'count']
    return ret.query('count >= 2')[['Email']]

if __name__ == '__main__':
    data = {
        "id": [1, 2, 3],
        "email": ["a@b.com", "b@c.com", "a@b.com"]
    }

    t1 = pd.DataFrame(data)
    print(duplicate_emails(t1))