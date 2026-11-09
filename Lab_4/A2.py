def draw_pryamougolnik(rows, columns, ch='#'):
    # прямоугольник
    print(f"\nПРЯМОУГОЛЬНИК {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()


def draw_treugolnik(rows, ch='#'):
    # треугольник
    print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
    for i in range(rows):
        for j in range(i + 1):
            print(ch, end='')
        print()
        

def draw_ramka(rows, columns, ch='#'):
    # рамка
    print(f"\nРАМКА {rows}*{columns}:")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()
        
        
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

draw_pryamougolnik(n, m)
draw_treugolnik(n)
draw_ramka(n, m)