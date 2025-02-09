w=float(input("Select Width: "))
l=float(input("Select Length: "))
p=2*(w+l)
rp = round(p)
rp = int(rp)
if rp == 0:
    print("Invalid Number")
else:
    print(rp)
