def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    num = float(d.replace("$", ""))
    return(num)


def percent_to_float(p):
    num = float(p.replace("%", "")) / 100
    return(num)

main()