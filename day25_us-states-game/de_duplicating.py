import pandas as pd

data_frame_object = pd.read_csv("european_countries.csv")
# columns=["state", "x", "y"]
duplicate_rows = data_frame_object[data_frame_object.duplicated(["state"], keep=False)]
print(duplicate_rows)