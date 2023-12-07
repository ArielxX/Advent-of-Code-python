time = input().split(':')[1]
time = int(time.replace(' ', ''))
distance = input().split(':')[1]
distance = int(distance.replace(' ', ''))

def func(holding, time):
    return (time - holding) * holding

# find when func(holding, time) > distance using discriminant

a = 1
b = -time
c = distance

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print(0)
elif discriminant == 0:
    print(1)
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(int(x2) - int(x1))
