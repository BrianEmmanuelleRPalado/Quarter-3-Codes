cities = ["London", "New York City"]

temperature = [

  [8, 8.5, 8.5, 8, 8.5, 9, 7],

  [0, 0, 2, -2, -4, -8.5, 0.5]
]
#rows are temperature
#columns are days
#the unit is celsius
a = sum(temperature[0])/7
b = sum(temperature[1])/7
print("The average weekly temperature for", cities[0], "is", round(a, 2), "and the average weekly temperature for", cities[1], "is", round(b, 2))

for i in range(len(cities)):
  total = sum(temperature[i])
  average = total / len(temperature[i])
  print("The added up temperature for", cities[i], "is", round(total, 2))
