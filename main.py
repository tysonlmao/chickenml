# this is really stupid
import lex # lex.py

def read():
    r = open("test.chicken", "r")
    print(r.read())
    


def test():
    sample = "<text>This is some text</text>"
    x = sample.split()
    print(x)

test()