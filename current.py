import pandas as pd

dtypes = {
    "first_name": "str",
    "last_name": "str",
    "middle_name": "str",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}
df = pd.read_csv(
    "datasets/legislators-current.csv",
    dtype=dtypes,
    usecols=list(dtypes)
)

df["full_name"] = df["first_name"] + " " + df["last_name"]
