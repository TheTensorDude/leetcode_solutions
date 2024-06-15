import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # TODO: Wrote when high
    employee.drop_duplicates(subset=["salary"], inplace=True)
    employee.sort_values(by="salary", inplace=True)

    if employee.empty:
        return pd.DataFrame(data={"SecondHighestSalary": [None]})
    # Filter the second one
    return employee.iloc[1:2][["salary"]].rename(
        columns={"salary": "SecondHighestSalary"}
    )
