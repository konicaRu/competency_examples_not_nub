import math


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


# конструктор создает прямоугольник
def make_rectangle(start_point, width, height):
    return ({'start_point': start_point, 'width': width, 'height': height})


# селектор извлекатель коорлинат левой-верхней точки
def get_start_point(constr):
    return constr['start_point']


# селектор извлекатель  ширины
def get_width(constr):
    return constr['width']


# селектор извлекатель высоты
def get_height(constr):
    return constr['height']


# фукция определит координаты точек для проверки принадлежит ли центр координат прямоугольнику
def get_quadrant(constr: dict):
    coordin_point = {'point_left_up': get_start_point(constr), 'point_right_up': {'x': get_x(point) + get_width(constr), 'y': get_y(point)},
                     'point_left_down': {'x': get_x(point), 'y': get_y(point) - get_height(constr)}, 'point_right_down': {'x': get_x(point) + get_width(const), 'y': get_y(point) - get_height(constr)}}

    if coordin_point['point_left_up']['x'] <= 0 and coordin_point['point_left_up']['y'] >= 0 and coordin_point['point_right_up']['x'] >= 0 and coordin_point['point_right_up']['y'] >= 0 and coordin_point['point_left_down']['x'] <= 0 and coordin_point['point_left_down']['y'] <= 0 and coordin_point['point_right_down']['x'] >= 0 and \
            coordin_point['point_right_down']['y'] <= 0:
        return True
    else:
        return False

    # проверяет, принадлежит ли центр координат прямоугольнику (не лежит на границе прямоугольника, а находится внутри)


def contains_origin(constr: dict):
    if get_quadrant(constr) == True:
        return True
    else:
        return False


# разрисовать на осях все варианты и подбить

point = make_decart_point(-3, 4)
const = make_rectangle(point, 5, 5)
# arr = {'start_point': {'x': 3, 'y': 4}, 'width': 5, 'height': 3}
# print(arr['start_point']['x'])
print(get_quadrant(const))
print(contains_origin(const))
