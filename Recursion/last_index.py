def find_last_index(arr, end_index, target):
    if not arr[:end_index + 1]:
        return -1
    if arr[end_index] == target:
        return end_index
    return find_last_index(arr, end_index - 1, target)


if __name__ == "__main__":
    arr = [7,5,5,6,9,8,2,8,8,5,2]
    print(f"Found last at index: {find_last_index(arr, len(arr) - 1, 9)}")