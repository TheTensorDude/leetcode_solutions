import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # The author will see his own article
    # So the ids should be same
    # Kinda high when I wrote this
    # TODO: Recheck later
    filt = views["author_id"] == views["viewer_id"]
    out = views[filt][["author_id"]]
    out.rename(columns={"author_id": "id"}, inplace=True)
    out.drop_duplicates(keep="first", inplace=True)
    out.sort_values(by="id", inplace=True)
    return out
