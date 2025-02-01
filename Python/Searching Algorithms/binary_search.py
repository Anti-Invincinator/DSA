'''
Binary Search; searches for a target value in a sorted list by repeadetly diving the search range in half. (O(log n))
'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 #midpoint

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target: # if target is greater than the midpoint, left half is dropped
            low = mid + 1

        else:                   # vice-versa if targer is smaller
            high = mid - 1  

    return -1


if __name__ == "__main__":
    data = sorted([5, 3, 7, 1, 9])  # list is sorted.
    target = 7
    result = binary_search(data, target)
    if result != -1:
        print(f"Target {target} found at index: {result}")
    else:
        print("Target not found.")