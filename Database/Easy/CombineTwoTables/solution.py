"""
Author: Marcus Curry
Date: 07/20/2024
GitHub: https://github.com/marcuscurry/leetcode/tree/main

Leetcode Question: https://leetcode.com/problems/combine-two-tables/description/
"""

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address, how='outer', on='personId').drop(columns=['personId', 'addressId']).dropna(subset=['lastName', 'firstName'])

if __name__ == '__main__':
    data1 = {
        'personId': [1,2],
        'lastName': ['Wang', 'Alice'],
        'firstName': ['Allen', 'Bob']
    }
    t1 = pd.DataFrame(data1)

    data2 = {
        'addressId': [1, 2],
        'personId': [2, 3],
        'city': ['New York City', 'Leetcode'],
        'state': ['New York', 'California']
    }
    t2 = pd.DataFrame(data2)

    print(combine_two_tables(t1, t2))