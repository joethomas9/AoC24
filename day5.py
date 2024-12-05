import sys, itertools

def read_file(file):
    rul, pgs = open(file).read().split("\n\n")
    return [tuple(map(int, line.split('|'))) for line in rul.strip().split('\n')], pgs.splitlines()

def pt2(rules, pages):
    for i, j in itertools.combinations(range(len(pages)), 2):
        if (pages[j], pages[i]) in rules:
            pages[j], pages[i] = pages[i], pages[j]
            if all(rule[0] not in pages or rule[1] not in pages or pages.index(rule[0]) < pages.index(rule[1]) for rule in rules):
                return pages[len(pages)//2]

def pt1(rules, pagelist):
    pageL, tot1, tot2 = [[int(i) for i in line.split(",")] for line in pagelist], 0, 0
    for pages in pageL:
        valid = all(rule[0] not in pages or rule[1] not in pages or pages.index(rule[0]) < pages.index(rule[1]) for rule in rules)
        if not valid: tot2 += pt2(rules, pages)
        tot1 += pages[len(pages)//2] * valid
    return tot1, tot2

pairs, pglist = read_file(sys.argv[1])
print(pt1(pairs, pglist))
