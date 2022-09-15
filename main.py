#coding:utf-8
from io import TextIOWrapper
import json
from time import sleep
from re import M
import deepl
import sys
# py = deepl.translate("EN", "FR","good is god")
# print(py)

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
    
def main() :
    # filaFileMatche = open(fileOutput, 'a')
    translateFinal={}
    source_lang = ["FR","EN"]
    target_lang = ["EN","DE"]
    fileContents = getFileContent("file.txt")
    target_file = open(str(target_lang[1]).lower()+".json",'a')
    
    for word in fileElement(fileContents) :
        enTranslate = translateWord("FR", "EN", word)
        print(enTranslate)
        sleep(50)
        deTranslate = translateWord("EN", "DE", enTranslate)
        print(deTranslate)
        # translateFinal[enTranslate.strip()] = deTranslate.strip()
        openAndWrite("de.txt", '"' + enTranslate +'"' + ":" + '"' + deTranslate + '"'+",")
        sleep(250)

    
# fileResource = getFileContent("combolist.txt")

# fileElement(fileResource)
main()