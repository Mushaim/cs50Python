def main():
    time = input("What time is it? ")
    formatted_time = convert(time)

    if 7 <= formatted_time <= 8:
        print("breakfast time",end="")
    elif 12 <= formatted_time <= 13:
        print("lunch time",end="")
    elif 18 <= formatted_time <= 19:
        print("dinner time",end="")

def convert(time):
    if time.endswith("a.m.") or time.endswith("p.m."):
        time, time_format = time.split(" ")
        hour, min = time.split(":")
        if time_format == "p.m." and hour != "12":
            hour = (float(hour))+12
        return float(hour)+(float(min))/60
    else:
        hour, min = time.split(":")
        hour = float(hour)
        min = (float(min))/60
        return hour+min


if __name__ == "__main__":
    main()