def binary_search(search_list, target):
    left_index = 0
    right_index = len(search_list) - 1
    
    while left_index <= right_index:
        
        middle_index = (right_index + left_index) // 2
        
        if target == search_list[middle_index]:
            return "Found at " + str(middle_index)
        elif target < search_list[middle_index]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
    return "Not Found"



def main():
    from random import sample
    
    search_list = sorted(sample([i for i in range(30)], 10))
    search_value = 10
    
    print(search_list, end = "\n\n")    
    print(binary_search(search_list, search_value))
    
main()
