from collision import (
    isCorrectRest,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
)

coordinats = [
    [(1,1),(5,5)],
    [(2,2),(6,6)],
    [(3,3),(7,7)]
]
coord = [coordinats[0],coordinats[1]]
#1
for i,rect in enumerate(coordinats,1):
    print(f"прямоугольник {i}: {rect}")
    print(f"подходит: {isCorrectRest(rect)}")

#2

print(f" Пересечение прямоугольников: {isCollisionRect(coord)}")

#3
print(f"Площадь переечения: {intersectionAreaRect(coordinats[0],coordinats[1])}")

#4
print(f"Площадь пересечения n-го колличества прямоугольников:{intersectionAreaMultiRect(coordinats)} ")
