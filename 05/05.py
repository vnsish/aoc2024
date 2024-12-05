def part1(file):
    with open(file, 'r') as fp:
        rulepages = fp.read()

    rules = rulepages.split('\n\n')[0]
    pages = rulepages.split('\n\n')[1]

    ruledict = {}
    for rule in rules.split():
        if rule.split('|')[1] not in ruledict:
            ruledict[rule.split('|')[1]] = [rule.split('|')[0]]
        else:
            ruledict[rule.split('|')[1]].append(rule.split('|')[0])

    orderedupdates = []

    for update in pages.split():
        ordered = True
        updates = update.split(',')
        for i, page in enumerate(updates):
            for j in range(i+1, len(updates)):
                if page in ruledict and updates[j] in ruledict[page]:
                    ordered = False
                
        if ordered:
            orderedupdates.append([int(x) for x in update.split(',')])
    
    total = 0

    for orderedupdate in orderedupdates:
        total += orderedupdate[int(len(orderedupdate)/2)]            

    print(total)

def checkupdate(ruledict, updates):
    ordered = True
    for i, page in enumerate(updates):
        for j in range(i+1, len(updates)):
            if page in ruledict and updates[j] in ruledict[page]:
                ordered = False

    return ordered

def part2(file):
    with open(file, 'r') as fp:
        rulepages = fp.read()

    rules = rulepages.split('\n\n')[0]
    pages = rulepages.split('\n\n')[1]

    ruledict = {}
    for rule in rules.split():
        if rule.split('|')[1] not in ruledict:
            ruledict[rule.split('|')[1]] = [rule.split('|')[0]]
        else:
            ruledict[rule.split('|')[1]].append(rule.split('|')[0])

    unorderedupdates = []

    for update in pages.split():
        ordered = True
        updates = update.split(',')
        for i, page in enumerate(updates):
            for j in range(i+1, len(updates)):
                if page in ruledict and updates[j] in ruledict[page]:
                    ordered = False
            
        if not ordered:
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

    total = 0

    for fixedupdate in fixedupdates:
        total += fixedupdate[int(len(fixedupdate)/2)]      

    print(total)

part1('input')
part2('input')