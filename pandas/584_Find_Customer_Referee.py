import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filt = (customer["referee_id"] != 2) | customer["referee_id"].isna()
    return customer[filt][["name"]]
