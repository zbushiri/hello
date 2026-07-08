def main():
    x = input("What's the equation? ")
    #Adds spaces to the operator so the computer can read it properly
    x = x.replace("*", " * ")
    x = x.replace("-", " - ")
    x = x.replace("+", " + ")
    x = x.replace("/", " / ")

    #Splits the input
    x = x.split()
    #Mark the operator so you can tell which one the user uses
    operator = x[1]

    if(operator == "*"):
        print("The answer is ", mult(x[0], x[2]))
    elif(operator == "+"):
        print("The answer is", add(x[0], x[2]))
    elif(operator == "-"):
        print("The answer is", sub(x[0], x[2]))
    elif(operator == "/"):
        print("The answer is", div(x[0], x[2]))
    


def mult(a, b):
    return float(a) * float(b)

def add(a, b):
    return float(a) + float(b)

def sub(a, b):
    return float(a) - float(b)

def div(a, b):
    return float(a) / float(b)

main()