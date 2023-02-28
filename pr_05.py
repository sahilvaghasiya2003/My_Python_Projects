# store the multiplication table generated in
# problem 3  in a file name Table.txt


num = int(input("Enter a number :"))
table = [num*i for i in range(1,11)]
print(table)

with open("File.txt", "a")as f:
    f.write(str(table))
    f.write('\n')