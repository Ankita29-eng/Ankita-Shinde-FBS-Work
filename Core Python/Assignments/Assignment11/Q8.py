# Print 1 to 100 in snakes and ladder pattern.
num = 1
for row in range(10):
    line = []

    for col in range(10):
        line.append(num)
        num += 1

    if row % 2 != 0:
        line.reverse()

    print(line)