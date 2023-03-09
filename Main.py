msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0
x = ""
y = ""
oper = ""
result = ""


# take input and check to see whether to retrieve prior result
# return x, oper, y
def take_input():
    global memory
    global x
    global oper
    global y

    print(msg_0)
    x, oper, y = input().split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory


# determine whether v is single digit
def is_single_digit(v):
    if v > -10 and v < 10:  # simplify, how?
        if v.is_integer() is True:
            return True
        else:
            return False
    else:
        return False


# check complexity of user input
def check_complexity(v1, v2, v3):
    msg = ""
    if is_single_digit(v1) is True and is_single_digit(v2) is True:
        msg = msg + msg_6
    if v1 == 1 or v2 == 1:
        if v3 == "*":
            msg = msg + msg_7
    if v1 == 0 or v2 == 0:
        if v3 == "*" or v3 == "+" or v3 == "-":
            msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


# convert digits into floats, check operand, calculate result accordingly
# return value of result
def calculator():
    global x
    global oper
    global y
    global result

    while True:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            continue
        else:
            operators = ('+', '-', '*', '/')
            if oper not in operators:
                print(msg_2)
                continue
            else:
                check_complexity(x, y, oper)
                if oper == "+":
                    result = x + y
                    return result
                elif oper == "-":
                    result = x - y
                    return result
                elif oper == "*":
                    result = x * y
                    return result
                elif oper == "/":
                    try:
                        result = x / y
                        return result
                    except ZeroDivisionError:
                        print(msg_3)
                        take_input()


# offer to save results for use in further calculations
# return True if result is to be saved, else False
def save_result():
    global memory
    while True:
        print(msg_4)
        answer = input()
        if answer == "y":
            return True
        elif answer == "n":
            break
        else:
            continue


# a simple y/n function
# returns True if y, False if n
def yes_no():
    answer = input()
    if answer == "y":
        return True
    elif answer == "n":
        return False


# running through the algorithm
while True:
    take_input()
    result = calculator()
    print(result)
    if save_result() is True:
        if is_single_digit(result) is not True:
            memory = result
        else:
            print(msg_10)
            if yes_no() is True:
                print(msg_11)
                if yes_no() is True:
                    print(msg_12)
                    if yes_no() is True:
                        memory = result
    print(msg_5)
    if yes_no() is True:
        continue
    else:
        break
