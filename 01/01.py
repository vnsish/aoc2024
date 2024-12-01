from collections import Counter

def part1(file):
    with open(file, 'r') as fp:
        lines = fp.read().split('\n')
    left = sorted([int(x.split('   ')[0]) for x in lines])
    right = sorted([int(x.split('   ')[1]) for x in lines])
    total = 0
    for a, b in zip(left, right):
        total += abs(a-b)
    print(total)

def part2(file):
    with open(file, 'r') as fp:
        lines = fp.read().split('\n')
    left = [int(x.split('   ')[0]) for x in lines]
    right = [int(x.split('   ')[1]) for x in lines]
    occurrences = Counter(right)
    total = 0
    for number in left:
        total += number*occurrences[number]
    print(total)

part1('input')
part2('input')

