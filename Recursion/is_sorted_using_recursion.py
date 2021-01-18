def is_sorted_using_recursion1(arr):  # compares the first 2 elements recursively
    if not arr or len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted_using_recursion(arr[1:])


def is_sorted_using_recursion2(arr):  # compares the last 2 elements recursively
    if not arr or len(arr) == 1:
        return True
    if arr[-1] < arr[-2]:
        return False
    return is_sorted_using_recursion2(arr[:-1])


if __name__ == "__main__":
    arr = [8,6,3,1,5,10,7,3]
    # arr.sort()
    print(is_sorted_using_recursion1(arr))