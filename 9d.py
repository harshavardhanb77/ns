s="""
def tocel(far):
    cel=((5/9)*(far-32))
    return cel
def tofar(cel):
    far=((9/5)*(cel))+32
    return far
"""

with open('util.py','x+') as f:
    f.write(s)