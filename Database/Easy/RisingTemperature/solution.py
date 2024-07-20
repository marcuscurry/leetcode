"""
https://leetcode.com/problems/rising-temperature/description/
"""

import pandas as pd
from datetime import timedelta


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by=['recordDate'], ascending=True, ignore_index=True)
    ret = []
    for day in range(len(weather.recordDate)-1):
        tmrw = weather.recordDate[day+1]
        if tmrw-weather.recordDate[day] == timedelta(days=1) and weather.temperature[day+1] > weather.temperature[day]:
            ret.append(weather.id[day+1])
    return pd.DataFrame(data=ret, columns=['Id'])

if __name__ == '__main__':
    # data = {
    #         'id': [1, 2, 3, 4],
    #         'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    #         'temperature': [10, 25, 20, 30]
    # }
    # t1 = pd.DataFrame(data)
    # t1.recordDate = pd.to_datetime(t1.recordDate)

    data2 = {
            'id': [1, 2],
            'recordDate': ['2000-12-16', '2000-12-15'],
            'temperature': [3,-1]
    }
    t2 = pd.DataFrame(data2)
    t2.recordDate = pd.to_datetime(t2.recordDate)

    print(rising_temperature(t2))