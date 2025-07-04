from historical import df

# Members per party, ordered by count desc.
# members_per_party = df.groupby("party", sort=False)["full_name"].count().sort_values(ascending=False)

# which parties have the most female legislators.
#females_per_party = df[df["gender"] == "F"].groupby("party")["party"].count()

# sort states per population count, breakdown by gender