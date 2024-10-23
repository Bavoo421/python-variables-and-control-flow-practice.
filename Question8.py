# Asking for a number (1-7)
day_num = int(input("Enter a number (1-7): "))

# Matching the number to a day of the week
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# Printing the corresponding day or an invalid input message
print(days.get(day_num, "Invalid input"))
