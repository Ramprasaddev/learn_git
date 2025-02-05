def reverse_a_string(string):
    string_list = list(string)
    left, right = 0, len(string_list) - 1
    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1
    reversed_string = ''.join(string_list)
    print(reversed_string)
    return reversed_string

string = "Ramprasad is a good boy"
reverse_a_string(string)