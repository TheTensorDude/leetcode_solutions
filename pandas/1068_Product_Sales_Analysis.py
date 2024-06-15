import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    out = sales.merge(product, on="product_id", how="left")
    return out[["product_name", "year", "price"]]
