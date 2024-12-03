import sys, re

def pt1(string):
    return sum(int(x) * int(y) for x,y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string))

def pt2(string):
    tot, enabled = 0, True
    for x, y, do, dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", string):
        if do or dont:
            enabled = bool(do)
        else:
            tot += (int(x) * int(y)) * enabled
    return tot
        
file = open(sys.argv[1]).read()
print(pt1(file), pt2(file))
