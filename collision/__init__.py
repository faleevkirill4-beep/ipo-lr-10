#FaleevKirill 

def isCorrectRest(coordinates):

    x1,y1 = coordinates[0] # левый нижний угол 
    x2,y2 = coordinates[1] # правый верхний угол 

    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        return False

    if x2 > x1 and y2 > y1:
        return True
    
    return False 