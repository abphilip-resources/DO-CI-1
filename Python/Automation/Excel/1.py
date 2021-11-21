import pandas as pd
from openpyxl.workbook import Workbook
loc = 'C:/Users/allen/OneDrive/Desktop/Github/Learning/' \
      'Python/Automation/Excel/data/read'                   # Location of the directory

print(pd.read_excel(f'{loc}/ReadExcel.xlsx'))               # Read the excel file
print(pd.read_csv(f'{loc}/ReadText.txt', delimiter='/t'))   # Read the text file
df = pd.read_csv(f'{loc}/ReadCSV.csv', header=None)         # Read the csv file

df.columns = ['First', 'Last', 'Address', 
              'City', 'State', 'Zip', 'Income']             # Rename the columns
df.to_excel(f'{loc}/WriteExcel.xlsx', index=False)          # Write the csv file to excel
df['Tax'] = df['Income'].apply(
      lambda x: .15 if x in range(0,5000)
           else .20 if x in range(5000,15000)
           else .25
)                                                           # Create Tax column to df and calculate tax
df['Pay'] = df['Income'] * df['Tax']

print(df[['Last', 'Zip']],'\n\n')                           # Print the last name and zip code columns
print(df['City'][0:4],'\n\n')                               # Print the first 4 cities
print(df.iloc[1,1],'\n\n')                                  # Print the second row, second column
print(df.loc[(df['First']=='John') &                        # Print the rows where first name is John ->
     (df['City']=='Riverside')],'\n\n')                     # And city is Riverside
print(df[['Income', 'Tax', 'Pay']],'\n\n')                  # Print Income related information