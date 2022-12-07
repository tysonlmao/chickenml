import os
extension = ".chicken" # temporary var

def avaliableFiles():
    path = './read'
    files = os.listdir(path)

    for file in files:
        if '.chicken' in file:
            print("Avaliable files:")
            print(file)

# prompts for what file you would like to view (no extension required)
# adding an extension will break
f = input("which file > ")
r = open(f'{f}{extension}', "r")

def read():
    print(r.read())


def start():
    avaliableFiles()
    read()

start()

