#coding:utf-8
from io import TextIOWrapper
import json
from time import sleep
from re import M
import deepl
import sys

INPUT_FILE = ""
FROM_LANG = ""
TO_LANG = ""
OUTPUT_FILE = str(TO_LANG)+".json"
SET_TIMER = 200


def getFileContent(filePath: str) -> TextIOWrapper:

    try:
        return open(filePath, 'r')
    except:
        sys.exit("unable to open file !")


def fileElement(fileResource: TextIOWrapper) -> list:
    words = []
    while fileResource:
        for i in fileResource:
            words.append(i)
        break
    return words


def translateWord(from_lg: str, to_lg: str, word: str) -> str:
    return deepl.translate(from_lg, to_lg, word)


def openAndWrite(filename, content):
    target_file = open(filename, 'a')
    target_file.write(content)
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


def makeTranslation():
    fileContents = getFileContent(INPUT_FILE)
    for word in fileElement(fileContents):
        translateOutput = translateWord(FROM_LANG, TO_LANG, word)
        print(translateOutput)
        openAndWrite(OUTPUT_FILE, '"' + word.strip() + '"' + ":" +
                     '"' + translateOutput.strip() + '"'+","+"\n")
        removeLine(word, INPUT_FILE)
        sleep(250)


def repliqueTranslate():
    fileContents = getFileContent(INPUT_FILE)
    for wordOrignal in fileElement(fileContents):
        word = wordOrignal.strip().replace(",", "")
        if word not in ["{", "}"]:
            words = word.replace('"', "").split(":")
            translateOutput = translateWord(FROM_LANG, TO_LANG, words[0])
            openAndWrite(
                OUTPUT_FILE, '"' + words[0] + '"' + ":" + '"' + translateOutput + '"'+","+"\n")
            removeLine(wordOrignal, INPUT_FILE)
            print(translateOutput)
            sleep(SET_TIMER)


def main():
    repliqueTranslate()


if __name__ == "__main__":

    main()
