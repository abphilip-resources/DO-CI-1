import pandas as pd
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Alignment, Border 
from openpyxl.styles import Side, PatternFill, Color
from openpyxl.styles import GradientFill, colors
loc = 'C:/Users/allen/OneDrive/Desktop/Github/Learning/' \
      'Python/Automation/Excel/data/2'                          # Location of the directory
wb1 = Workbook()                                                # Create workbook
ws1 = wb1.active                                                # Go to active sheet of 

for z in range(1,20): ws.append(range(300))

ws.merge_cells('A1:B5')                                         # Merge cells A1:B5
ws.unmerge_cells('A1:B5')                                       # Unmerge cells A1:B5
ws.merge_cells(
    start_row=1, start_column=1, 
    end_row=5, end_column=2
)                                                               # Merge cells A1:B5 