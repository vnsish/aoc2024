import re

def part1(file):
    with open(file, 'r') as fp:
        text = fp.read()
    
    matches = re.findall(r"mul\(\d+,\d+\)", text)

    total = 0

    for match in matches:
        total += int(match[match.index("(")+1:match.index(",")]) * int(match[match.index(",")+1:match.index(")")])

    print(total)

def part2(file):
    with open(file, 'r') as fp:
        text = ''.join(fp.read().splitlines())

    #text = text.replace('\n', '')
    #remove everything between a do() and don't()
    text = re.sub(r"don\'t\(\).*?do\(\)", '', text)
    #remove everything after a don't()
    text = re.sub(r"don\'t\(\).*", '', text)

    matches = re.findall(r"mul\(\d+,\d+\)", text)

    total = 0

    for match in matches:
        total += int(match[match.index("(")+1:match.index(",")]) * int(match[match.index(",")+1:match.index(")")])

    print(total)


part1('input')
part2('input')