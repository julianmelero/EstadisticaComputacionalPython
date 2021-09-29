from borracho import TraditionalBorracho
from field import Field
from coords import Coord

from bokeh.plotting import figure, show



def caminata(field, borracho, steps):
    start = field.get_coord(borracho)

    for _ in range(steps):
        field.move_borracho(borracho)

    return start.distance(field.get_coord(borracho))


def simulator(steps, n_try, BorrachoType):
    borracho = BorrachoType(name="Julián")
    origen = Coord(0, 0)
    distances = []

    for _ in range(n_try):
        field = Field()
        field.add_borracho(borracho, origen)
        simulator_walk = caminata(field, borracho, steps)
        distances.append(round(simulator_walk, 1))

    return distances



def graph(x, y):
    graphic = figure(title='Camino aleatorio',
                     x_axis_label='pasos', y_axis_label='distancia')
    graphic.line(x, y, legend='distancia media')

    show(graphic)


if __name__ == "__main__":
    walk_distance = [10000]
    n_try = 100

    def main(walk_distance, n_try, Borracho):
        half_distance_walk = []
        for steps in walk_distance:
            distances = simulator(steps, n_try, Borracho)
            half_distance = round(sum(distances) / len(distances), 4)
            max_distance = max(distances)
            min_distance = min(distances)
            half_distance_walk.append(half_distance)
            print(f'{Borracho.__name__} walks {steps}')
            print(f'Half distance is {half_distance}')
            print(f'Max distance is {max_distance}')
            print(f'Min distance is {min_distance}')
        
        graph(walk_distance, distances)
       

    main(walk_distance, n_try, TraditionalBorracho)