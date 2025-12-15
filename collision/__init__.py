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
