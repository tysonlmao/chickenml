import re

r = []

def read():
    r = open("test.chicken", "r")
    print(r.read())

text = read()

def apply(r):
    marked = re.sub(r'\bi\b', '<i>i</i>', r)
    marked = re.sub(r'\bb\b', '<b>b</b>', marked)

    return marked

apply()