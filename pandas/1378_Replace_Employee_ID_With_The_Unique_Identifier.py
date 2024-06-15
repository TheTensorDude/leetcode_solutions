import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    out = employees.merge(employee_uni, on="id", how="left")
    out = out[["unique_id", "name"]]
    return out
