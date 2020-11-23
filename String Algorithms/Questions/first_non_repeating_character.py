def get_character_index(s):
    d = {}  # will hold values in the format[fist_index, count]

    for i in range(len(s)):
        if d.get(s[i]):
            d[s[i]][1] += 1
        else:
            d[s[i]] = [i, 1]

    min_index = len(s) + 1  # will hold the index of the first character with frequency 1
    
    for i in d:
        if d[i][1] == 1 and min_index > d[i][0]:
            min_index = d[i][0]

    return min_index


if __name__ == "__main__":
    string = input("Enter string\n")
    index = get_character_index(string)

    try:
        print("First Non-repeating character is {} at index {}".format(string[index], index))
    except:
        print("No Non-repeating character")
