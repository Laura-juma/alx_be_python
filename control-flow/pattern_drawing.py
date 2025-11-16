
rows = int(input("Enter the size of the pattern:"))
max_rows = 1

if rows < 0:
  print("Please input a positive integer")
else:
  while max_rows <= rows:
    for i in range(1, rows+1):
      print("*", end="")
    print()
    max_rows +=1

