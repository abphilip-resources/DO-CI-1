import pandas as pd
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Alignment, Border 
from openpyxl.styles import Side, PatternFill, Color
from openpyxl.styles import GradientFill, colors
loc = 'C:/Users/allen/OneDrive/Desktop/Github/Learning/' \
      'Python/Automation/Excel/data/2'                          # Location of the directory
wb1 = Workbook()                                                # Create workbook
ws1 = wb1.active                                                # Go to active sheet of wb1