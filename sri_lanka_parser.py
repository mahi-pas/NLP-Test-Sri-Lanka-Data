import sys
import importlib;
from datetime import datetime;
from PDFoperations import formatPDF, PDFtoRTF
from rtfExtractor import extractDataFromRTF
from convertToTable import convertToTable


if __name__ == "__main__":
    
    n = len(sys.argv)
    if (n<4):
        print("Invalid number of arguments! Correct usage: sri_lanka_parser.py <folder-to-parse/> <output-file.csv> <parsing-model.py>")
        quit()
    
    #Import Arguments
    inFolder = sys.argv[1]  # Arg 1: folder of PDFs to parse. They should all be compatible with the same parsing model
    outFile = sys.argv[2]   # Arg 2: output file, in csv format
    modelFile = sys.argv[3] # Arg 3: parsing model. PDF will be converted to text, but model will convert text to array data

    model = importlib.import_module(modelFile) 

    formattedPDF = formatPDF(filename) #Alan
    rtfData = PDFtoRTF(formattedPDF) #Alan
    importantText,timestamps = model.extractDataFromRTF(rtfData) #Eoin
    table = model.convertToTable(importantText,timestamps) #Mahi

    print(table)


