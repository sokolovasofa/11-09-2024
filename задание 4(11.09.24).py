a=int(input("Введите время в часах:"))
if 4<a<12:
    print("Утро")
elif 11<a<18:
    print("День")
elif 17<a<23:
    print("Вечер")
elif -1<a<5 or 22<a<24:
    print("Ночь")
else:
    print("Ошибка")
