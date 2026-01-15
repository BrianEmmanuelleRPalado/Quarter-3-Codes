cities = ["London", "New York City"]

temperature = [

  [8, 8.5, 8.5, 8, 8.5, 9, 7],

  [0, 0, 2, -2, -4, -8.5, 0.5]
]
#rows are temperature
#columns are days
#the unit is celsius
a = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("New York's temperature on", a[2], ":", temperature[1][2])
print("London's temperature daily...", temperature[0])
print("Updating London's temperature on", a[3], "to 6.")
temperature[0][3] = 6
print("Updated temperature:", temperature[0])