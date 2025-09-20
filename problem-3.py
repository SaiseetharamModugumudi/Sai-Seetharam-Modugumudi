# Program-3.py
# Generate series (pattern depends on input)

n = int(input("Enter a number: "))
series = []

# logic: odd numbers up to n (if n is odd), else up to n-1
if n % 2 == 0:
    limit = n - 1
else:
    limit = n

for i in range(limit):
    series.append(2 * i + 1)

print("Series:", ", ".join(map(str, series)))
