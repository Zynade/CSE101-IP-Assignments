n = int(input("Number of students: "))

# Note: I have assumed pi to equal 3.14
pi = 3.14

for i in range(n):
    dimension = input("2D or 3D?: ")
    if dimension == "2D":
        print("Choose a shape from the ones below (Enter the serial number): ")
        choice = int(input("""
        #1: Square
        #2: Rectangle
        #3: Rhombus
        #4: Parallelogram
        #5: Circle
        """))

        if choice == 1:
            s = float(input("Side s: "))
            peri = s * 4
            area = s * s
            print("Perimeter:", peri)
            print("Area:", area)

        elif choice == 2:
            l = float(input("length: "))
            b = float(input("breadth: "))
            peri = 2 * (l + b)
            area = l * b
            print("Perimeter:", peri)
            print("Area:", area)

        elif choice == 3:
            a = float(input("side length: "))
            d1 = float(input("diagonal 1: "))
            d2 = float(input("diagonal 2: "))
            peri = 4 * a
            area = d1 * d2 / 2
            print("Perimeter:", peri)
            print("Area:", area)

        elif choice == 4:
            # Note: I'm assuming the given height to be with respect to the base (here, base === breadth)
            l = float(input("length: "))
            b = float(input("base: "))
            h = float(input("height: "))
            peri = 2 * (l + b)
            area = b * h
            print("Perimeter:", peri)
            print("Area:", area)

        elif choice == 5:
            r = float(input("radius: "))
            peri = 2 * pi * r
            area = pi * r * r
            print("Circumference:", peri)
            print("Area:", area)

    elif dimension == "3D":
        print("Choose a shape from the ones below (Enter the serial number): ")
        choice = int(input("""
            #6: Cube
            #7: Cuboid
            #8: Right circular cone
            #9: Hemisphere
            #10: Sphere
            #11: Solid cylinder
            #12: Hollow cylinder
            """))
        # pi = 3.14

        if choice == 6:
            s = float(input("side s: "))
            csa = 4 * s * s
            tsa = 6 * s * s
            volume = s * s * s
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 7:
            l = float(input("length: "))
            b = float(input("breadth: "))
            h = float(input("height: "))
            csa = 2 * h * (l + b)
            tsa = 2 * ((l * b) + (b * h) + (h * l))
            volume = l * b * h
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 8:
            slant = float(input("slant height: "))
            r = float(input("radius: "))
            h = float(input("height: "))
            csa = pi * r * slant
            tsa = pi * r * (r + slant)
            volume = 1/3 * pi * h * r * r
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 9:
            r = float(input("radius: "))
            csa = 2 * pi * r * r
            tsa = 3 * pi * r * r
            volume = 2/3 * pi * r * r * r
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 10:
            r = float(input("radius: "))
            csa = 4 * pi * r * r
            tsa = 4 * pi * r * r
            volume = 4/3 * pi * r * r * r
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 11:
            r = float(input("radius: "))
            h = float(input("height: "))
            csa = 2 * pi * r * h
            tsa = 2 * pi * r * (h + r)
            volume = pi * r * r * h
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

        elif choice == 12:
            r1 = float(input("radius 1: "))
            r2 = float(input("radius 2: "))
            h = float(input("height: "))
            csa = 2 * pi * h * (r1 + r2)
            tsa = 2 * pi * abs((r1 * r1 - r2 * r2)) + csa
            volume = pi * h * abs((r1 * r1 - r2 * r2))
            print("CSA:", csa)
            print("TSA:", tsa)
            print("Volume:", volume)

    print()
