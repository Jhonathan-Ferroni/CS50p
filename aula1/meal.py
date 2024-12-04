def main():
    time = input("Enter time in 24-hour format (HH:MM): ")
    hours = convert(time)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    if 12.0<= hours <= 13.0:
        print("lunch time")
    if 18.0<= hours <= 19.0:
        print("dinner time")


def convert(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours + minutes / 60.0


if __name__ == "__main__":
    main()
