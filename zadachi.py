# Расчет количества книг на дискете
byte_one_symbol = 4
volume = 1.44
pages = 100
lines = 50
symbol = 25
total_symbol = pages * lines * symbol
volume_book = total_symbol * byte_one_symbol

disk_size = volume * 1024 * 1024
num_books = disk_size // volume_book
print("Количество книг:", num_books)

# Расчет периметра и площади геометрических фигур
pi = 3.1415
radius = 5
perimeter = 4 * radius
side = 5
area = pi * radius
area = round(area , 2)
circumference = 2*pi*radius
circumference = round(circumference , 2)
perimeter_square = 4*side
square_area = side ^ 2
print("Площадь круга" , area)
print("Длина окружности" , circumference)
print("Площадь квадрата" , square_area)
print("Периметр квадрата" , perimeter_square)

# Формирование строки из повторяющихся чисел
str_numbers = {}