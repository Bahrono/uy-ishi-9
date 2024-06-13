def CloneRange(start, stop=None, step=1.0):
    if stop is None:
        stop = start
        start = 0.0

    current = float(start)
    while current < stop:
        yield current
        current += step


for num in CloneRange(1, 5, 0.5):
    print(num)
#1
# for num in CloneRange(0, 10, 2):
#     print(num)
#2
# for num in CloneRange(5, 10):
#     print(num)
#3
# for num in CloneRange(5):
#     print(num)
#4
# for num in CloneRange(1.5, 5, 0.75):
#     print(num)


