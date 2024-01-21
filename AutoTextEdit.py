import json
import os

rulesFile = "./editrules.json"

inputDir = "./input/"
outputDir = "./output/"

filenames = os.listdir(inputDir)

editjson = open(rulesFile, "r", encoding="utf-8")
edit = json.load(editjson)
editjson.close()

def replace_text_in_files(filenames):
    for file in filenames:
        inputtxt = open(f"{inputDir}{file}", "r", encoding="utf-8")
        inputlist = inputtxt.readlines()
        inputtxt.close()

        for i in range(len(inputlist)):
            for text in edit["remove"]:
                if text in inputlist[i]:
                    inputlist[i] = inputlist[i].replace(text, "")
                    print(f"We removed {text}(s) on line " + str(i))
            for pair in edit["replace"]:
                if pair[0] in inputlist[i]:
                    inputlist[i] = inputlist[i].replace(pair[0], pair[1])
                    print(f"We replaced {pair[0]}(s) with {pair[1]} on line " + str(i))


        os.makedirs(os.path.dirname(f"{outputDir}{file}"), exist_ok=True)
        outputtxt = open(f"{outputDir}{file}", "w", encoding="utf-8")
        outputtxt.writelines(inputlist)
        outputtxt.close()

replace_text_in_files(filenames)