def get_Input():
    input = 'Day_02_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        reports = []
        for report_Str in raw_Input:
            report_Split = report_Str.split()
            report = []
            for num in report_Split:
                report.append(int(num))
            reports.append(report)
        return reports

def check_Reports(reports):
    safe_Count = 0
    unsafe = False
    for report in reports:
        if sorted(report) == report:
            for index in range(len(report)):
                if index != len(report) - 1:
                    if report[index + 1] - report[index] > 3 or report[index] == report[index + 1]:
                        unsafe = True
            if not unsafe:
                safe_Count += 1
        elif sorted(report, reverse=True) == report:
            for index in range(len(report)):
                if index != len(report) - 1:
                    if report[index] - report[index + 1] > 3 or report[index] == report[index + 1]:
                        unsafe = True
            if not unsafe:
                safe_Count += 1
        unsafe = False
    return safe_Count

def report_Splitter(report):
    new_Reports = []
    for skip in range(len(report)):
        new_Reports.append([])
        for num in range(len(report)):
            if num != skip:
                new_Reports[skip].append(report[num])
    is_Safe = report_Checker(new_Reports)
    return is_Safe

def report_Checker(reports):
    is_Safe = False
    unsafe = False
    for report in reports:
        if sorted(report) == report:
            for index in range(len(report)):
                if index != len(report) - 1:
                    if report[index + 1] - report[index] > 3 or report[index] == report[index + 1]:
                        unsafe = True
            if not unsafe:
                is_Safe = True
        elif sorted(report, reverse=True) == report:
            for index in range(len(report)):
                if index != len(report) - 1:
                    if report[index] - report[index + 1] > 3 or report[index] == report[index + 1]:
                        unsafe = True
            if not unsafe:
                is_Safe = True
        unsafe = False
    return is_Safe

def main():
    reports = get_Input()
    print(check_Reports(reports))
    safe_Count = 0
    for report in reports:
        if report_Splitter(report):
            safe_Count += 1
    print(safe_Count)

if __name__ == '__main__':
    main()