# = 19
prim = 91525
mult = 1
string = str(prim)
arr = []
while len(string) > 1:
    for i in string:
        mult *= int(i)
        string = str(mult)
        print(mult)


