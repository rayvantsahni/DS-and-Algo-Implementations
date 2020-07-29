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
    print(binary_search(search_list, 0, len(search_list)-1, search_value))
    
main()
