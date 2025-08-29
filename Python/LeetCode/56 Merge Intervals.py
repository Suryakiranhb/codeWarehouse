#56. Merge intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    # Sorting intervals based on each 2d element's 0th position (sorting based on start time)
    intervals.sort(key = lambda x:x[0])
    merged_list = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= merged_list[-1][1]:
            merged_list[-1][1] = max(merged_list[-1][1], intervals[i][1])
            #merged_list.append([intervals[i][0],intervals[i+1][1]])
        else:
            merged_list.append(intervals[i])
    return merged_list


intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = merge_intervals(intervals)
print(f"The merged list would be: {ans}")