n = int(input("Enter Number of Lines: "))

prog = []
deftab = []
nametab = {}

inside = False
start = 0

print("Enter Program:")

for _ in range(n):
    prog.append(input())

for i,line in enumerate(prog):

    words = line.split()

    if "MACRO" in words:
        inside = True
        start = len(deftab)

    elif inside:

        deftab.append(line)

        if words[0] == "MEND":

            inside = False

            name = deftab[0].split()[0]

            nametab[name] = (start, len(deftab)-1)

# DEFTAB
print("\nDEFTAB")

for i,line in enumerate(deftab):
    print(i, line)

# NAMETAB
print("\nNAMETAB")
print("Name\tStart\tEnd")

for name,val in nametab.items():
    print(f"{name}\t{val[0]}\t{val[1]}")
    
