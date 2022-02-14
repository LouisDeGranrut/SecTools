#!/usr/bin/env python 3
import PyPDF2
import argparse
import re
import exifread
import sqlite3

def get_pdf_meta(file):
    pdf_file = PyPDF2.PdfFileReader(open(file,"rb"))
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print("[+] " + info + ": " + doc_info[info])

def get_strings(file):
    with open(file, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())

def get_exif(file):
    with open(file, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print("No EXIF data found")
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag])) 

def get_help():
    print("[+] " + "-pdf PDF analysis")
    print("[+] " + "-str")
    print("[+] " + "-exif Image exif extractor")


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
    get_exif(args.str)
if args.help:
    get_help()
