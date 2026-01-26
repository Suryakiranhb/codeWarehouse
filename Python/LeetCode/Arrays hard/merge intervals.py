import sys

def merge_intervals(arr):
    if not arr:
        #if arr is empty:
        return []
    
    #sorted by start time:
    arr.sort(key = lambda x: x[0])

    merged = []
    merged.append(arr[0])

    for i in range(1,len(arr)):
        last = merged[-1]
        print(last)
        sys.exit()
        current = arr[i]

        #overlap cheking and merging if so
        if last[1] >= current[0]:
            last[1] = max(last[1],current[1])
        else:
            merged.append(current)
    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = merge_intervals(intervals)
print("The final merged list : ",ans)