katz_deli = []

def line(current_line):
    if len(current_line) == 0:
        print("The line is currently empty.")
    else:
        counter = 1
        str = "The line is currently:"
        for customer in current_line:
            str += f" {counter}. {customer}"
            counter += 1
        print(str)

def take_a_number(current_line, new_name):
    current_line.append(new_name)
    print(f"Welcome, {new_name}. You are number {len(current_line)} in line.")

def now_serving(current_line):
    if len(current_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {current_line.pop(0)}.")