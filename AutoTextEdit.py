import json

editjson = open("./edit.json", "r", encoding="utf-8")
edit = json.load(editjson)
editjson.close()

inputtxt = open("./input.txt", "r", encoding="utf-8")
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

outputtxt = open("output.txt", "w", encoding="utf-8")
outputtxt.writelines(inputlist)
outputtxt.close()