import pandas as pd
from openpyxl.workbook import Workbook
loc = "C:/Users/allen/OneDrive/Desktop/Github/Learning/" \
      "Python/Automation/Excel/data/read"

df_excel = pd.read_excel(f"{loc}/ReadExcel.xlsx")
df_text = pd.read_csv(f"{loc}/ReadText.txt", delimiter="/t")
df_csv = pd.read_csv(f"{loc}/ReadCSV.csv", header=None)

df_csv.columns = ["First", "Last", "Address", "City", "State", "Zip", "Amount"]
df_csv.to_excel(f"{loc}/WriteExcel.xlsx", index=False)

print(df_csv[["First", "Zip"]], end="\n\n")
print(df_csv["City"][0:4], end="\n\n")
print(df_csv.iloc[1,1])