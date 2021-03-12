https://www.toptal.com/developers/sorting-algorithms

# 퀵정렬 quick sort

# 합병정렬  merge sort

def mergeSort(nums) :
    # 나누는
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    print(nums)
    print('divide!!!')
    left = mergeSort(nums[:mid]) # 정렬된 리스트들
    right = mergeSort(nums[mid:]) # 정렬된 리스트들
    print(left, right)
    # 합치자!
    sorted_list = merge(left, right) # 정렬된 리스트들을 합쳐준것
    print('sorted_list :',sorted_list)
    
    return sorted_list

def merge(left, right):
    l = 0
    r = 0
    sorted_list = []
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
    return sorted_list
    
            
# [8, 6, 4, 3, 2, 1]이 출력되어야 합니다.
print(mergeSort([1, 6, 3, 8, 2, 4, 5, 7]))

# [9, 7, 4, 3, 2, 1]가 출력되어야 합니다.
print(mergeSort([7, 2, 4, 1, 9, 3, 1, 3]))