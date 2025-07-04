import pandas as pd

dtypes = {
    "first_name": "str",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}
df = pd.read_csv(
    "datasets/legislators-historical.csv",
    dtype=dtypes,
    usecols=list(dtypes) + ["birthday", "last_name"],
    parse_dates=["birthday"]
)

df["full_name"] = df["first_name"] + " " + df["last_name"]