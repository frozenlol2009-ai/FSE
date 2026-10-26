x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))
if (x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0):
    if (x1>0 and y1>0 and x2>0 and y2>0):
        print("Yes, I") # точки в первой координатной четверти
    elif (x1<0 and y1<0 and x2<0 and y2<0):
        print("Yes, III ") # точки в третьей координатной четверти 
    elif (x1>0 and y1<0 and x2>0 and y2<0):
        print("Yes, IV") # точки в четвертой координатной четверти
    elif (x1<0 and y1>0 and x2<0 and y2>0):
        print("Yes, II") # точки во второй координатной четверти
    else:
        print ("No") # точки не лежат в одной координатной четверти 
else:
    print ("Error") # введена координата равная 0

