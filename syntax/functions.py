def sum(*args):
    sum = 0
    for i, num in enumerate(args):
        print("Argument number {0} is {1}".format(i, num))
        sum = sum + num

    print("Sum is {0}".format(sum))


sum(1, 2, 3, 4, 5)
# sum(1, 2, 3, "a", 4, 5)
