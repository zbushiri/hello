# Input the greeting
greeting = input("Greeting: ").strip().lower()
# Greeting starts with hello
if greeting.startswith("hello"):
    print("$0")
# Greeting starts with the letter h
elif greeting.startswith("h"):
    print("$20")
# Greeting starts with anything else 
else:
    print("$100")