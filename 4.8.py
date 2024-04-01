#print triangle pattern

print("Name: Ankit Singla")
print("Roll No: 2210997033")

n = int(input("Enter number of rows: "))
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
