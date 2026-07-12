# Ask for expression
inp = input("Expression: ").split()

# Check symbol
if inp[1] == "+":
    print(float(inp[0]) + float(inp[2]))
elif inp[1] == "-":
    print(float(inp[0]) - float(inp[2]))
elif inp[1] == "*":
    print(float(inp[0]) * float(inp[2]))
elif inp[1] == "/":
    print(float(inp[0]) / float(inp[2]))