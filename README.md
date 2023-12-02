This is a python script to extract table from a pdf file.

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