# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def find_substrings(string):
    if string.count(" ") == 0:
        return [string]
    substrings = []
    depth = 0
    temp_substring = ""
    for char in string + " ":
        if char == '(':
            depth += 1
            if depth > 1:
                temp_substring += char
            continue
        if char == ')':
            depth -= 1
            if depth > 0:
                temp_substring += char
            continue
        if depth > 0:
            temp_substring += char
        if depth == 0 and len(temp_substring) > 0:
            substrings.append(temp_substring)
            temp_substring = ""
        if depth == 0 and char != " ":
            substrings.append(char)
    return substrings


def find_all_substrings(string):
    single_depth = find_substrings(string)
    final_output = []
    for substring in single_depth:
        if substring.count(" ") == 0:
            final_output.append(substring)
        else:
            final_output.append(find_all_substrings(substring))
    return final_output


def Calculate(string):
    formatted_string = find_all_substrings(string)
    print(formatted_string)
    calc = RunCalculation(formatted_string)
    return calc


def RunCalculation(formatted_string):
    if True not in [type(x) == list for x in formatted_string]:
        return RunFlatCalculation(formatted_string)
    else:
        return 9


def RunFlatCalculation(formatted_string):
    if len(formatted_string) == 3:
        calc = SingleCalc(formatted_string)

    elif len(formatted_string) > 3:
        calc = SingleCalc(formatted_string)
        print(calc)
        print(formatted_string[3:])
        new_list = [str(calc)]
        [new_list.append(x) for x in formatted_string[3:]]
        calc = RunFlatCalculation(new_list)

    else:
        calc = int(formatted_string[0])
    return calc


def SingleCalc(formatted_string):
    val1, op, val2, *_ = formatted_string
    if op == "+":
        calc = int(val1) + int(val2)
    elif op == "*":
        calc = int(val1) * int(val2)
    return calc


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
