import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filt = (products.recyclable == "Y") & (products.low_fats == "Y")
    return products[filt][["product_id"]]
