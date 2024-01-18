import sys
from PDFoperations import formatPDF, PDFtoRTF
from rtfExtractor import extractTextFromRTF
from convertToTable import convertToTable


if __name__ == "__main__":
    
    n = len(sys.argv)
    if (n<2):
        print("Invalid number of arguments! Correct usage: sri_lanka_parser.py <file-to-parse>")
        quit()
    
    #using filename, upload the pdf and process it
    filename = sys.argv[1]

    formattedPDF = formatPDF(filename) #Alan
    rtfData = PDFtoRTF(formattedPDF) #Alan
    importantText,timestamps = extractDataFromRTF(rtfData) #Eoin
    table = convertToTable(importantText,timestamps) #Mahi

    print(table)


