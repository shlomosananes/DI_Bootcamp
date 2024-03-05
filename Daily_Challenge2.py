
birthday = input("Please enter your birthday in format DD/MM/YY separated by s simple '/': ")
date_list = birthday.split("/")
print(date_list)
day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])
print(day)
print(month)
print(year)
day_last = day % 10

print(day_last)

print("    ")