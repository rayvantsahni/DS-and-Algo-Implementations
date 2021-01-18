

def find_all_indices(arr, target, start_index = 0, indices = []):
    
    if not arr[start_index:]:
        return indices
    
    if arr[start_index] == target:
        indices.append(start_index)
    
    return find_all_indices(arr, target, start_index + 1, indices)


if __name__ == "__main__":
    arr = [9,2,2,6,9,2,7,9]
    target = 9
    
    print(f"All indices of {target}: {find_all_indices(arr, target)}")