x=0
y=0
value = 0
av = 0
while x < 3:
    name = input()
    while y < 3:
        num = int(input())
        value += num
        y += 1
    av = value / 3
    print("Name: ", name)
    print("Average: ", "{:.2f}".format(av))
    x += 1