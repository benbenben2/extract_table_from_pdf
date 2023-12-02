'''
# PREREQUISITES
python3

# INSTALLATION
## install virtual environment
sudo apt install python3.11-venv
python3 -m venv venv
source venv/bin/activate
## install needed packages
pip install "camelot-py[base]"
pip install --upgrade PyPDF2==2.12.1
pip install opencv-python

# SETUP
- copy pdf file in "extract_table_from_pdf" folder
- update the variables "file_name" and "pages" below

# RUN
python3 extract_table_from_pdf.py

# POSTPROCESSING
- to be done manually
- deactivate the virtual environment:
deactivate
'''

import camelot


# TO UPDATE FILE NAME (replace <file_name> by the name of the pdf file)
file_name = "<file_name>.pdf"
# TO UPDATE PAGES (COMMA SEPARATED LIST OF PAGES, EXAMPLE: "1,2,4")
pages = "4"


tables = camelot.read_pdf(file_name, pages=pages, flavor="stream")

print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

tables.export(file_name + ".csv", f="csv", compress=False)
