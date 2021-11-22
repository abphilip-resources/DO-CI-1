import pandas as pd
loc = 'C:/Users/allen/OneDrive/Desktop/Github/Learning/' \
      'Python/Automation/Excel/data/3'                          # Location of the directory

df1 = pd.read_excel(f'{loc}/A_Read.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel(f'{loc}/A_Read.xlsx', sheet_name='Sheet2')
df3 = pd.read_excel(f'{loc}/B_Read.xlsx')
df = pd.concat([df1, df2, df3], sort=False)
print(df)