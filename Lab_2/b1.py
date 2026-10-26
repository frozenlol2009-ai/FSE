print("Miroslav Smaliuk")
print("Simple Map Distance Computations")
print()

with open(r"C:\Study\FSE\Lab_2\inmap0.dat", "r") as file:
    content = file.read()
    
    numbers = [float(x) for x in content.split()]

count = int(numbers[0]) # колво дорог
scale = numbers[1] # масштаб (миль/дюйм)

print('Map Scale Factor: ', numbers[1], ' miles per inch')
print()
print('          Map         Mileage')
print('          Measure     Distance')
print('=' * 100)

distances = []

for i in range(count):
    row_num = i + 1
    measure = numbers[i + 2] #отрезок в дюймах
    distance = round(measure * scale + 0.00001,1) # считает пути в каждой дороге
    print('#  ',row_num,'     ',measure,'       ',distance)
    distances.append(distance) 

print('=' * 100)

total = sum(distances) #итоговый путь

print("Total Distance:      ", total)
