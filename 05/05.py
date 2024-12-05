def open_file(filename):
    with open(filename, 'r') as fp:
        rulepages = fp.read()
    rules = rulepages.split('\n\n')[0]
    pages = rulepages.split('\n\n')[1]
    ruledict = {}
    for rule in rules.split():
        ruledict.setdefault(rule.split('|')[1], []).append(rule.split('|')[0])

    return ruledict, pages

def part1(file):
    ruledict, pages = open_file(file)

    orderedupdates = []

    for update in pages.split():
        ordered = True
        if checkupdate(ruledict,update.split(',')):
            orderedupdates.append([int(x) for x in update.split(',')])
    
    total = sum(orderedupdate[int(len(orderedupdate)/2)] for orderedupdate in orderedupdates)

    print(total)

def checkupdate(ruledict, updates):
    ordered = True
    for i, page in enumerate(updates):
        for j in range(i+1, len(updates)):
            if page in ruledict and updates[j] in ruledict[page]:
                ordered = False
    return ordered

def part2(file):
    ruledict, pages = open_file(file)

    unorderedupdates = []

    for update in pages.split():
        if not checkupdate(ruledict,update.split(',')):
            unorderedupdates.append(update.split(','))
    
    fixedupdates = []
    
    for unordered in unorderedupdates:
        while not checkupdate(ruledict, unordered):
            swapped = False
            for i, page in enumerate(unordered):
                if swapped: break
                for j in range(i+1, len(unordered)):
                    if swapped: break
                    if page in ruledict and unordered[j] in ruledict[page]:
                        unordered[i], unordered[j] = unordered[j], unordered[i]
                        swapped = True
        
        fixedupdates.append([int(x) for x in unordered])
 
    print(sum(fixedupdate[int(len(fixedupdate) / 2)] for fixedupdate in fixedupdates))

part1('input')
part2('input')