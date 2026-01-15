names = ["Brian", "Mary", "Charles"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]
b = []
for i in range(len(names)):
 a = sum(steps[i])
 print(names[i], ":", a)
 b.append(a)
c = max(b)
c1 = b.index(c)
print("The person with the highest amount of steps is", names[c1])
d = min(b)
e = c-d
print("The difference between the highest and lowest total steps is:", e)
