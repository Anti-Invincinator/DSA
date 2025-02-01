'''
Linear Search; checks each element one by one until target value is found. (O(n) Complexity)
'''

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
        
    return -1

if __name__ == "__main__":
    data = [2, 3, 14, 23, 22, 18, 9] 

    if linear_search(data, target = 88) == -1:
        print("Target value doesn't exist in array!!")

    print(f"Target value exists at index : {linear_search(data, target = 9)}")