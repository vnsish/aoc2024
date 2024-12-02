def check_report(report, damp=False, is_subreport=False):
    safe = True
    positive = False
    negative = False

    for i in range(len(report)-1):
        dx = report[i] - report[i+1]
        
        if dx < 0:
            negative = True
        else:
            positive = True

        if (abs(dx) > 3 or abs(dx) == 0) or (positive and negative):
            safe = False
            break
    
    if not safe and not is_subreport and damp:
        for subreport in get_subreports(report):
            if check_report(subreport, is_subreport=True):
                safe = True

    return safe

def get_subreports(report):
    subreports = []
    for i in range(len(report)):
        subreports.append(report[:i] + report[i+1:])
    return subreports

def part1(file):
    with open(file, 'r') as fp:
        reports = [x for x in fp.read().split('\n')]
    
    total = 0

    for report in reports:
        if check_report([int(x) for x in report.split(' ')]):
            total += 1
        
    print(total)

def part2(file):
    with open(file, 'r') as fp:
        reports = [x for x in fp.read().split('\n')]
    
    total = 0
    
    for report in reports:
        if check_report([int(x) for x in report.split(' ')],damp=True):
            total += 1
    
    print(total)

part1('input')
part2('input')