def reverse(input):
    current_count = -1
    if type(input) == str:
        reversed = ""
        for thing in input:
            reversed += input[current_count]
            current_count -= 1
    if type(input) == list:
        reversed = []
        for thing in input:
            reversed.append(input[current_count])
            current_count -= 1
    return reversed


if __name__ == '__main__':
    print(reverse(['hello', "man", "wassup"]))
