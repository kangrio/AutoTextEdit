import json
import os

rulesFile = "./editrules.json"
editjson = open(rulesFile, "r", encoding="utf-8")
edit = json.load(editjson)
editjson.close()

inputDir = "input"
outputDir = "output"
allFileNames = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(inputDir) for f in filenames if f.split(".")[-1] in edit["whitelist"]]

def replace_text_in_files(filenames):
    for index, file in enumerate(filenames, 1):
        print(f"{"="*50}\nProcessing {index}: {file}\n{"="*50}")
        inputtxt = open(f"{file}", "r", encoding="utf-8")
        inputlist = inputtxt.readlines()
        inputtxt.close()

        outputlist = inputlist.copy()

        for i in range(len(inputlist)):
            for text in edit["remove"]:
                if text in outputlist[i]:
                    outputlist[i] = outputlist[i].replace(text, "")
                    print(f"We removed {text}(s) on line " + str(i+1))
            for pair in edit["replace"]:
                if pair[0] in outputlist[i]:
                    outputlist[i] = outputlist[i].replace(pair[0], pair[1])
                    print(f"We replaced {pair[0]}(s) with {pair[1]} on line " + str(i+1))

        if outputlist != inputlist:
            file = os.path.relpath(file, 'input')

            os.makedirs(os.path.dirname(f"{os.path.join(outputDir,file)}"), exist_ok=True)
            outputtxt = open(f"{os.path.join(outputDir,file)}", "w", encoding="utf-8")
            outputtxt.writelines(outputlist)
            outputtxt.close()
        
        print("")

replace_text_in_files(allFileNames)