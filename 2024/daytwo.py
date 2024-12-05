import time

#Part 1
time1 = time.time()

reports = []
with open('daytwo.txt', 'r') as f:
    for line in f:
        # Split the line into two values
        reports.append(list(map(int, line.split())))


def increasing(report):
    for i, level in enumerate(report):
        if (i == len(report)-1):
            return 1
        elif (((report[i+1] - level) <= 3) and ((report[i+1] - level) >= 1)):
            continue
        else:
            return 0

def decreasing(report):
    for i, level in enumerate(report):
        if (i == len(report)-1):
            return 1
        elif ((level - (report[i+1]) <= 3) and ((level - report[i+1]) >= 1)):
            continue
        else:
            return 0
    
def part1(reports):
    count = 0
    
    for report in reports:
        if (report[0] < report[1]):
            count += increasing(report)
        else:
            count += decreasing(report)
    
    return count

time2 = time.time()

time12 = time.time()

print(part1(reports))
print('time: ', time2-time1)

# def increasing2(report, skipped):
#     if len(report) <= 1:
#         return 1

#     if skipped > 1:
#         return 0

#     if 1 <= (report[1] - report[0]) <= 3:
#         return increasing2(report[1:], skipped)

#     elif len(report) > 2 and 1 <= (report[2] - report[0]) <= 3:
#         return increasing2(report[2:], skipped + 1)

#     return 0


# def decreasing2(report, skipped):
#     if len(report) <= 1:
#         return 1

#     if skipped > 1:
#         return 0

#   
#     if 1 <= (report[0] - report[1]) <= 3:
#         return decreasing2(report[1:], skipped)

#     elif len(report) > 2 and 1 <= (report[0] - report[2]) <= 3:
#         return decreasing2(report[2:], skipped + 1)

#     return 0


# def part2(reports):
#     count2 = 0
#     for report in reports:
#         if report[0] < report[1]:
#             count2 += increasing2(report, 0)
#         else:
#             count2 += decreasing2(report, 0)

#     return count2

def is_increasing(arr):
    for i in range(1, len(arr)):
        if not (1 <= arr[i] - arr[i - 1] <= 3):
            return False
    return True


def is_decreasing(arr):
    for i in range(1, len(arr)):
        if not (1 <= arr[i - 1] - arr[i] <= 3):
            return False
    return True


def can_be_increasing(arr):

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]  
        if is_increasing(new_arr):
            return True
    return False


def can_be_decreasing(arr):
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        if is_decreasing(new_arr):
            return True
    return False


def part2(reports):
    count2 = 0
    for report in reports:
        if is_increasing(report) or is_decreasing(report) or can_be_increasing(report) or can_be_decreasing(report):
            count2 += 1
    return count2



time22 = time.time()
print(part2(reports))
print('time: ', time22-time12)

#Time to complete both 1:05:56