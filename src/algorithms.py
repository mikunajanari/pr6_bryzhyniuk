import numpy as np
import random
from shapely.geometry import Point, Polygon

# Функція обчислення площі полігона методом Гауса (Shoelace formula)
def polygon_area_gauss(coords: Polygon):
    # Масив усіх X/Y-координат вершин
    x = np.array([p[0] for p in coords])
    y = np.array([p[1] for p in coords])

    # Обчислення суми за формулою Гауса
    area = np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)

    return abs(area) / 2

# Функція обчислення площі методом Монте-Карло
def monte_carlo_area(polygon: Polygon, num_points=10000):
    # Межі полігона
    min_x, min_y, max_x, max_y = polygon.bounds

    # Площа прямокутника, у який вписаний полігон
    box_area = (max_x - min_x) * (max_y - min_y)

    inside_count = 0

    # Генерація випадкових точок
    for _ in range(num_points):
        # Випадкові координати X/Y у межах прямокутника
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        if polygon.contains(Point(x, y)):
            inside_count += 1

    return box_area * inside_count / num_points