#!/usr/bin/env python 3
import PyPDF2
import argparse
import re
import exifread
import sqlite3
import pyfiglet
from termcolor import colored

#PDF Analysis
def get_pdf_meta(file):
    pdf_file = PyPDF2.PdfFileReader(open(file,"rb"))
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print(colored("[+] " + info + ": " + doc_info[info], "green"))

def get_strings(file):
    with open(file, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())

#Image analysis
def get_exif(file):
    with open(file, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print(colored("No EXIF data found", "red"))
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag])) 

def get_help():
    print(colored("[+] " + "-pdf: PDF analysis", "yellow" ))
    print(colored("[+] " + "-str:", "yellow"))
    print(colored("[+] " + "-exif: Image exif extractor", "yellow"))

if __name__ == "__main__":
    print(colored(pyfiglet.figlet_format('File Forensic', font='big'), "yellow"))
    get_help()
    parser = argparse.ArgumentParser(description="File analysis tool")
    parser.add_argument("-help", dest="help", help = "Shows help", required=False)
    parser.add_argument("-pdf", dest="pdf", help = "Path of the PDF file to analyse", required=False)
    parser.add_argument("-str", dest="str", help = "Path of the file to analyse", required=False)
    parser.add_argument("-exif", dest="exif", help = "Path of the image to analyse", required=False)

    args = parser.parse_args()

    if args.pdf:
        get_pdf_meta(args.pdf)
    if args.str:
        get_strings(args.str)
    if args.exif:
        get_exif(args.exif)
    if args.help:
        get_help()
