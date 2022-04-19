while True:
    pattern_type = input("""\nWhat pattern would you like?: 
	-Right-angled triangle
	-Isosceles triangle
	-Kite
	-Half Kite
	-X
	-quit
    """)
    print()

    # EXIT CONDITION
    if pattern_type == "quit":
        break

    n = int(input("Size: "))

    if pattern_type == "Right-angled triangle":
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    if pattern_type == "Isosceles triangle":
        for i in range(1, n + 1):
            for j in range(n - i):
                # print (n - i) blank spaces
                print(" ", end="")
            for k in range(1, 2 * i):
                # print numbers from 1 to 2i - 1
                print(k, end="")
            print()

    if pattern_type == "Kite":
        # repeat the top part of isosceles triangle
        for i in range(1, n + 1):
            for k in range(n - i):
                # print (n - i) blank spaces
                print(" ", end="")
            for l in range(1, 2 * i):
                # print numbers from 1 to 2n - 1
                print(l, end="")
            print()

        for i in range(1, n):
            for j in range(i):
                # print i number of spaces
                print(" ", end="")
            for k in range(1, 2 * (n - i)):
                # print the numbers from 1 to 2n - 2i - 1. Because in say line 2, we want 2(4) - 2(2) - 1 = 3 numbers
                print(k, end="")
            print()

    if pattern_type == "Half Kite":
        # print top half
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

        # print bottom half
        for i in range(1, n):
            for j in range(1, n - i + 1):
                print(j, end=" ")
            print()

    if pattern_type == "X":
        # top half
        for i in range(0, n - 1):
            for j in range(i):
                # print i number of blank spaces
                print(" ", end="")
            for k in range(1, 2 * (n - i)):
                print(k, end="")
            print()

        # bottom half
        for i in range(1, n + 1):
            for j in range(n - i):
                print(" ", end="")
            for k in range(1, 2 * i):
                print(k, end="")
            print()
