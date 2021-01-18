def find_first_index(arr, target, start_index = 0):
    if not arr[start_index:]:
        return -1
    if arr[start_index] == target:
        return start_index
    return find_first_index(arr, target, start_index + 1)


if __name__ == "__main__":
    arr = [0,6,3,7,7,10,7,4]
    print(f"Found first at index: {find_first_index(arr, 7)}")
