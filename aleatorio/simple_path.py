import random
from bokeh.plotting import figure, show





def graph(x, y):
    graphic = figure(title='Camino aleatorio')
    #graphic.line(x, y, legend='distancia media')

    show(graphic)


if __name__ == "__main__":
    walk_distance = 8000        
    graphic = figure(title='Camino aleatorio')
    x = 0
    y = 0
    x_new = 0
    y_new = 0
    new_cords_x = []    
    new_cords_y = []    
    for steps in range(walk_distance):
        x,y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x_new = x_new + x
        y_new = y_new + y
        new_cords_x.append(x_new)
        new_cords_y.append(y_new)
        graphic.line(new_cords_x, new_cords_y)            
    
    show(graphic)


   