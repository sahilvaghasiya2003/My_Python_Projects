#Write a program to print third, fifth, seventh element from a list using 
#enumerator function

list1 = [12,43,495,33,45,323,435,654]
for index, list1 in enumerate(list1):
    if index==2 or index==4 or index==6:
        print(list1)