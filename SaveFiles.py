# readFile and writeFile functions from 15-112 class notes

import ast
from Model import Model

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def checkSaved(self):
    savedTxt = readFile("saved.txt")
    self.saved = []
    tmpSaved = []
    for lines in savedTxt.splitlines():
        print("lines",lines)
        tmpSaved.append(lines)
        if len(tmpSaved) == 3:
            self.saved.append(tmpSaved)
            tmpSaved = []
        elif lines == "":
            tmpSaved = []
    for line in self.saved:
        line[1] = ast.literal_eval(line[1])
        line[2] = ast.literal_eval(line[2])
    print(tmpSaved)
    print(self.saved)
    #self.saved = readFile("saved.txt")

def saveNew(self, verts, edges):
    self.saved.append([self.curName, verts, edges])
    save(self)

def save(self):
    saveStr = ""
    for model in self.saved:
        name = model[0]
        verts = model[1]
        edges = model[2]
        saveStr += ("\n"+ str(name)+"\n" +str(verts) + "\n" + str(edges) + "\n")
    writeFile("saved.txt", saveStr)

# contentsToWrite = "This is a test!\nIt is only a test!\nWhat's new?\nin fact nothing"
# writeFile("saved.txt", contentsToWrite)

# contentsRead = readFile("saved.txt")
# print(contentsRead)
# assert(contentsRead == "")

# note to self: write file will create the file if not already existing
# if exists, just overwrites it