#program to remove duplicates from a string
'''a=str(input("enter a str:"))
empty=""
for i in a:
    if i in empty:
        continue
    else:
        empty+=i
print(empty)'''


a=str(input("enter a str:"))
empty=""
for i in range(len(a)):
    ch=a[i]
    while ch not in i:
        i+=ch
    print(e)
