a=int(input("Введите координату х1:"))
b=int(input("Введите координату y1:"))
c=int(input("Введите координату х2:"))
d=int(input("Введите координату y2:"))
if 0>=a>9 or 0>=b>9 or 0>=c>9 or 0>=d>9:
    print("Ошибка")
elif (a+2==c and b+1==d) or (a+2==c and b-1==d) or (a-2==c and b+1==d) or (a-2==c and b-1==d) or (a+1==c and b+2==d) or (a+1==c and b-2==d) or (a-1==c and b+2==d) or (a-1==c and b-2==d):
    print("yes")
else:
    print("no")