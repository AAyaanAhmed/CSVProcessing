import csv

t = c = h = 0
n = ""
d = {}

with open(C:/Users/Ayaan/Downloads/Book1.csv) as f:
    for r in csv.DictReader(f):
        try:
            s = float(r["Salary"])
        except:
            continue

        t += s
        c += 1

        if s > h:
            h, n = s, r["Name"]

        dept = r["Dept"]
        d[dept] = d.get(dept, 0) + 1

print("Records :", c)
print("Total   :", t)
print("Average :", round(t / c, 2) if c else 0)
print("Highest :", h, "-", n)

for k, v in d.items():
    print(k, ":", v)
