# readFile and writeFile functions from 15-112 class notes

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def checkSaved(self):
    self.saved = readFile("saved.txt")

# contentsToWrite = "This is a test!\nIt is only a test!\nWhat's new?\nin fact nothing"
# writeFile("saved.txt", contentsToWrite)

# contentsRead = readFile("saved.txt")
# print(contentsRead)
# assert(contentsRead == "")

# note to self: write file will create the file if not already existing
# if exists, just overwrites it