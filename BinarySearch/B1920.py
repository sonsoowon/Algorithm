import sys

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False


inp = sys.stdin.readline

n = int(input())
inp_arr = list(map(int, inp().rstrip().split()))
inp_arr.sort()

target_n = int(input())
target_arr = list(map(int, inp().rstrip().split()))

for target in target_arr:
    if binary_search(inp_arr, target):
        print(1)
    else: print(0)
