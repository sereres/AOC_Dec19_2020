# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def Calculate(string):
    formatted_string = string.split(" ")
    calc = RunCalcs(formatted_string)
    return calc


def RunCalcs(formatted_string):
    if len(formatted_string) == 3:
        calc = SingleCalc(formatted_string)

    elif len(formatted_string) > 3:
        calc = SingleCalc(formatted_string)
        print(calc)
        print(formatted_string[3:])
        new_list = [str(calc)]
        [new_list.append(x) for x in formatted_string[3:]]
        calc = RunCalcs(new_list)

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
