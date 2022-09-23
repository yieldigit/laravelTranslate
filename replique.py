#coding:utf-8
from io import TextIOWrapper
import sys

INPUT_FILE = ""
OUTPUT_FILE = ""

def getFileContent(filePath:str) -> TextIOWrapper:
    
    try:
        return open(filePath, 'r')
    except  :
        sys.exit("unable to open file !")

def fileElement(fileResource:TextIOWrapper) -> list:
    words = []
    while fileResource :
        for i in fileResource :
            words.append(i)
        break
    return words


def removeLine(contentLineToRemove, inpuFile):
    "Function to auto update File by remove old entry"
    src_file = inpuFile
    f = open(src_file, "r")
    contents = f.readlines()
    f.close()

    # remove the line item from list, by line number, starts from 0
    contents.remove(contentLineToRemove)
    f = open(src_file, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def openAndWrite(filename,content) :
    target_file = open(filename, 'a')
    target_file.write(content)
    target_file.close()
    
def main() :
    fileContents = getFileContent(INPUT_FILE)
    for wordOrignal in fileElement(fileContents) :
        word = wordOrignal.strip().replace(",","")
        if word not in ["{","}"] :
            words = word.replace('"',"").split(":")
            print(words[0])
            openAndWrite(OUTPUT_FILE, '"' + words[0] + '"' + ":" + '"' + words[0] + '"'+","+"\n")
            removeLine(wordOrignal, INPUT_FILE)
        
main()