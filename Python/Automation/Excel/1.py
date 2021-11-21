import pandas as pd
from openpyxl.workbook import Workbook
loc = "C:/Users/allen/OneDrive/Desktop/Github/Learning/" \
      "Python/Automation/Excel/data/read"                                   # Location of the directory

df_excel = pd.read_excel(f"{loc}/ReadExcel.xlsx")                           # Read the excel file
df_text = pd.read_csv(f"{loc}/ReadText.txt", delimiter="/t")                # Read the text file
df_csv = pd.read_csv(f"{loc}/ReadCSV.csv", header=None)                     # Read the csv file

df_csv.columns = ["First", "Last", "Address", "City", "State", "Zip"]       # Rename the columns
df_csv.to_excel(f"{loc}/WriteExcel.xlsx", index=False)                      # Write the csv file to excel

print(df_csv[["Last", "Zip"]], end="\n\n")                                  # Print the last name and zip code columns
print(df_csv["City"][0:4], end="\n\n")                                      # Print the first 4 cities
print(df_csv.iloc[1,1], end="\n\n")                                         # Print the second row, second column
print(df_csv.loc[(df_csv["First"]=="John") & 
     (df_csv["City"]=="Riverside")], end="\n\n")                            # Print the rows where first name is John and city is Riverside