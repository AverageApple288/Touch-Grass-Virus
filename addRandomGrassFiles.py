import os
import random
import string


def makeGrass(path):
    randName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    with open(path + randName + ".txt", 'w') as f:
        f.write("Grass :)")


def makeLotsOfFolders(path):
    origin=""
    for i in range (random.randint(1,10)):
            fileName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if i==0:
                 origin=path+fileName
            os.mkdir(path+fileName+"/")
            if not(i==0):
                for i in range (random.randint(1,2)):
                    makeGrass(path)
                for i in range (random.randint(1,5)):
                    decoyFile=''.join(random.choices(string.ascii_letters + string.digits, k=8))
                    os.mkdir(path+decoyFile+"/")
            path+=fileName+"/"
    return origin

def main():
    path=os.getcwd()
    newpath=path.split('/')
    i=2
    newPathString="/"+newpath[1]+"/"
    done=False
    while not(done):
            if (not (os.access(newPathString, os.W_OK))):
                entry=newpath[i]
                i+=1
                newPathString+=entry+"/"
            else:
                done=True



    origin=[]
    for i in range (2):
        origin.append(makeLotsOfFolders(newPathString))
    with open("lawnmower.txt", 'a') as f:
        for i in range (len(origin)):
            f.write(origin[i]+"\n")
        f.close()
