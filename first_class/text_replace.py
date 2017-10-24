
with open("boris.txt") as infile:
    lines = infile.read()

find = "art"
replacement = "death"
lines = lines.split(".")

lines = [line.replace(find, replacement) for line in lines if find in line]
print("\n".join(lines))
