# Program-2.py
# Generate series of odd numbers up to n terms

n = int(input("Enter a number: "))
series = []

for i in range(n):
    series.append(2 * i + 1)

print("Series:", ", ".join(map(str, series)))
