from datetime import date, datetime, timedelta

import pandas as pd


def WeekNumByDatetime(dt: datetime)-> int:
    return dt.isocalendar().week

def HireWeekNumberColumn(df: pd.DataFrame, hiredate: str)-> pd.DataFrame:
    df["Hire Week Number"] = [value if value is "" else WeekNumByDatetime(value) for value in df[hiredate]]
    return df

def WeekStartbyDatetime(dt: datetime)-> date:
    return (dt - timedelta(days=dt.weekday()) - timedelta(days=1)).date()

def WeekStartColumn(df: pd.DataFrame, hiredate: str)-> pd.DataFrame:
    df["Week Start"] = [value if value is "" else WeekStartbyDatetime(value) for value in df[hiredate]]
    return df

def WeekOfColumn(df: pd.DataFrame, hiredate: str)-> pd.DataFrame:
    df["Week of"] = [value if value is "" else "week of " + str(WeekStartbyDatetime(value)) for value in df[hiredate]]
    return df

##
# week id/number: datetime.date().isocalendar().week
# start = dt - timedelta(days=dt.weekday())
# end = start + timedelta(days=6)
