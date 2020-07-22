import os
import shutil


def copyFile(fileName):
    # target =
    fileList = os.listdir(fileName)
    for i in fileList:
        source = fileName + "/" + i + "/.mooctest/answer.py"
        target = fileName + "/" + i + ".py"
        shutil.copy(source, target)


soruce = "../代码/"
fileList = os.listdir(soruce)
for i in fileList:
    if os.path.isdir(soruce+i):
        copyFile(soruce + i)
