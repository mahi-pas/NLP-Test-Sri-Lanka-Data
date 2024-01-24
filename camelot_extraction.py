import camelot
import pandas

tables = camelot.read_pdf('Data/Dengue/sri lanka weekly.pdf')
print(f'tables: \n{tables}\n\n')

tables.export('result.csv', f='csv', compress=False) # json, excel, html, markdown, sqlite
print(f'report: {tables[0].parsing_report}')
