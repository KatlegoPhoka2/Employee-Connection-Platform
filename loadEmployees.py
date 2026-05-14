import pandas as pd
import random
import yagmail



# LOAD EMPLOYEES


class LoadEmployees :

    def load_employees(self,sheet_id):

     url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv"
    )

     df = pd.read_csv(url)

    # Clean data
     df = df.dropna()

     df = df.drop_duplicates(subset=["email"])
     return df   



