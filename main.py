import math

x = float(input("Введите число:"))#ввод вещественного числа
result = math.floor(x) + math.ceil(x)#округление вниз до ближайшего целого + округление вверх до ближайшего целого
print(result)