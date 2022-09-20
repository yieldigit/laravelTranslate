#coding:utf-8
from io import TextIOWrapper
import json
from time import sleep
from re import M
import deepl
import sys

INPUT_FILE = "file.txt"
FROM_LANG = "FR"
TO_LANG = "DE"
OUTPUT_FILE = str(TO_LANG)+".json"

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


def translateWord(from_lg:str, to_lg:str,word:str) -> str:
    return deepl.translate(from_lg,to_lg,word)

def openAndWrite(filename,content) :
    target_file = open(filename, 'a')
    target_file.writelines(content)
    target_file.close()


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

def makeTranslation() :
    fileContents = getFileContent(INPUT_FILE)
    for word in fileElement(fileContents) :
        translateOutput = translateWord(FROM_LANG, TO_LANG, word)
        print(translateOutput)
        openAndWrite(OUTPUT_FILE, '"' + word + '"' + ":" + '"' + translateOutput + '"'+",")
        removeLine(word, INPUT_FILE)
        sleep(250)
            
def main() :
    makeTranslation()

if __name__ == "__main__":
        
    main()