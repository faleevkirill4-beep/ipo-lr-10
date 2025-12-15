    #FaleevKirill 
class RectCorrectError(Exception):

    pass

def isCorrectRest(coordinates):

    x1,y1 = coordinates[0] # левый нижний угол 
    x2,y2 = coordinates[1] # правый верхний угол 

    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        return False

    if x2 > x1 and y2 > y1:
        return True
    
    return False 



def isCollisionRect(rectangles):
    if not isinstance(rectangles, list) or len(rectangles) != 2:
        raise ValueError("Функция ожидает список из двух прямоугольников")
    
    # Проверяем корректность прямоугольников
    for i, rect in enumerate(rectangles, 1):
        if not isCorrectRest(rect):
            raise RectCorrectError(f"{i}й прямоугольник некорректный")
    
    # Извлекаем координаты первого прямоугольника
    (x1, y1), (x2, y2) = rectangles[0]
    
    # Извлекаем координаты второго прямоугольника
    (x3, y3), (x4, y4) = rectangles[1]
    
    intersect_x = not (x2 <= x3 or x4 <= x1)
    intersect_y = not (y2 <= y3 or y4 <= y1)
    
    return intersect_x and intersect_y


def intersectionAreaRect(rect1,rect2):

    if not isCorrectRest(rect1):
        raise ValueError("Первый прямоугольник некоректный")
    
    if not isCorrectRest(rect2):
        raise ValueError("Второй прямоугольник некоректный")
    
    (x1,y1), (x2,y2) = rect1

    (x3,y3), (x4,y4) = rect2

    # Находим координаты пересечения по оси X
    # Пересечение по X: максимальная из левых границ и минимальная из правых границ
    left_x = max(x1, x3)
    right_x = min(x2, x4)
    
    # Если пересечения по X нет (левая граница пересечения >= правой границы)
    if left_x >= right_x:
        return 0.0
    
    # Находим координаты пересечения по оси Y
    # Пересечение по Y: максимальная из нижних границ и минимальная из верхних границ
    bottom_y = max(y1, y3)
    top_y = min(y2, y4)
    
    # Если пересечения по Y нет
    if bottom_y >= top_y:
        return 0.0
    
    width = right_x - left_x
    height = top_y - bottom_y

    #площадь
    area = width * height

    return float(area)


def peresech(rect1,rect2):

    (x1,y1),(x2,y2) = rect1
    (x3,y3),(x4,y4) = rect2


    left_x = max(x1, x3)
    right_x = min(x2, x4)
    bottom_y = max(y1, y3)
    top_y = min(y2, y4)

    if left_x >=right_x or bottom_y >=top_y:
        return None

    return [(left_x, bottom_y), (right_x, top_y)]

def area(rect):

    (x1, y1), (x2, y2) = rect

    return (x2 - x1) * (y2 - y1)



def intersectionAreaMultiRect(rectangles):
    if not isinstance(rectangles,list):
        raise ValueError("Ожидается список списков")
    
    if len(rectangles) < 2:
        ValueError("надо 2 прямоугольника")

    for i,rect in enumerate(rectangles,1):
        if not isCorrectRest(rect):
            raise ValueError(f"{i}прямоугольник не коректный")
        
    if len(rectangles) == 2:
        peresechenie =peresech(rectangles[0],rectangles[1])
        return area(peresechenie) 
    
    