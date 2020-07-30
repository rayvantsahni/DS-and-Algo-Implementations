def exponential_search(search_list, left, right, target):
    if search_list[0] == target:
        return "Found at 0"
    
    i = 1
    while i < len(search_list) and search_list[i] <= target:
        i *= 2
        
    index = binary_search(search_list, i//2, min(i, len(search_list)-1), target) 
    return index
    

def binary_search(search_list, left, right, target):
    if left > right:
        return "Not Found!"

    middle = (left + right) // 2

    if search_list[middle] == target:
        return "Found at " + str(middle)
    elif search_list[middle] > target:
        return binary_search(search_list, left, middle - 1, target)
    else:
        return binary_search(search_list, middle + 1, right, target)
    
    


def main():
    from random import sample
    
    search_list = sorted(sample([i for i in range(30)], 10))
    search_value = 10
    
    print(search_list, end = "\n\n")
    print(exponential_search(search_list, 0, len(search_list)-1, search_value))
    
    
main()    