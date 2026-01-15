names = ["Brian", "Mary", "Charles"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]
days = len(steps[0])
y = []
a = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(days):
    z = 0
    for j in range(len(names)):
        z = z + steps[j][i]
    print(a[i], ":", z, "steps")
    y.append(z)
x = max(y)
w = (y.index(x))
print("The most active day is on", a[w])