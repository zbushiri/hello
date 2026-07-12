def main():
# Asks for time
    inp = input("What time is it? ").split()

    hour, minute = inp[0].split(":")
    hour = float(hour)
    minute = float(minute)

# Assistance for a.m. / p.m.
    if len(inp) == 2 and inp[1] == "p.m.":
        hour = hour + 12
    else:
        pass
        
# Breakfast time 7-8
    if 7 <= convert(hour, minute) <= 8:
        print("breakfast time")

# Lunch time 12-13
    elif 12 <= convert(hour, minute) <= 13:
        print("lunch time")

# Dinner time 18-19
    elif 18 <= convert(hour, minute) <= 19:
        print("dinner time")

def convert(hour, minute):

# Translates minutes 
    minute = minute/ 60
# Puts together
    time = hour + minute
# Returns the time
    return(time)
    

if __name__ == "__main__":
    main()