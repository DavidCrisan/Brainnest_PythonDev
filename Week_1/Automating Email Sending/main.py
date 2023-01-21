from datetime import date  # core python module
import pandas as pd  # pip install pandas
from send_email import send_email  # local python module


# Public GoogleSheets url - not secure!
SHEET_ID = "1NqT7QdaoJhhIZ8O0wqhRPxYi3bYg3gnpXFjxnZtZ4x0"  # !!! CHANGE ME !!!
SHEET_NAME = "Sheet1"  # !!! CHANGE ME !!!
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["Email", "Name"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


print(load_df(URL))