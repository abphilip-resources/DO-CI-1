import pandas as pd
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Alignment, Border 
from openpyxl.styles import Side, PatternFill, Color
from openpyxl.styles import GradientFill, colors
loc = 'C:/Users/allen/OneDrive/Desktop/Github/Learning/' \
      'Python/Automation/Excel/data/2'                          # Location of the directory
wb = Workbook()                                                 # Create workbook
ws = wb.active                                                  # Go to active sheet of 

for z in range(1,20): ws.append(range(300))

ws.merge_cells('A1:B5')                                         # Merge cells A1:B5
ws.unmerge_cells('A1:B5')                                       # Unmerge cells A1:B5
ws.merge_cells(
    start_row=2, start_column=2, 
    end_row=5, end_column=5
)                                                               # Merge cells B2:E5 

cell = ws['B2']                                                 # Get cell B2
cell.font = Font(
    name='Calibri', color=colors.COLOR_INDEX[44],
    size=24, bold=True
)                                                               # Set font
cell.value = 'Allen'                                            # Set value
cell.alignment = Alignment(
    horizontal='center', vertical='center'
)                                                               # Set alignment
cell.fill = GradientFill(
    stop=('009FFD', '2A2A72'), type='linear'
)                                                               # Set gradient fill
cell.border = Border(
    left=Side(border_style='thin', color='FF000000'),
    right=Side(border_style='thin', color='FF000000'),
    top=Side(border_style='thin', color='FF000000'),
    bottom=Side(border_style='thin', color='FF000000')
)                                                               # Set border
wb.save(f'{loc}/B_Write.xlsx')                                  # Save workbook