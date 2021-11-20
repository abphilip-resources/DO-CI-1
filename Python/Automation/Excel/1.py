import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel("data/read/ReadExcel.xlsx")
df_text = pd.read_csv("data/read/ReadText.txt", delimiter="\t")
df_csv = pd.read_csv("data/read/ReadCSV.csv", header=None)

df_csv.columns = ["First", "Last", "Address", "City", "State", "Zip", "Amount"]
df_csv.to_excel("data/read/WriteExcel.xlsx", index=False)