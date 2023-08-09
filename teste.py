def get_all_substrings(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substrings.append(input_string[i:j])
    return substrings

input_string = "abcd"
substrings = get_all_substrings(input_string)
print(substrings)