def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace(" ", "")
    if is_correct(x):
        print("Yes")
    else:
        print("No")

def is_correct(n):
    match n:
        case "42" | "forty-two" | "fortytwo":
            return True
        case _:
            return False
        
main()