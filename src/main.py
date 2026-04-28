import time

import matplotlib.pyplot as plt
from generators import generate_polygon
from algorithms import polygon_area_gauss, monte_carlo_area

# Генерація полігону
polygon = generate_polygon(num_points=50, radius=50)

# Еталонна площа
shapely_area = polygon.area

def task_2_test():
    # Метод Гауса
    coords = list(polygon.exterior.coords)[:-1]   # координати вершин
    gauss_area = polygon_area_gauss(coords)

    # Метод Монте-Карло
    mc_area = monte_carlo_area(polygon, 10000)

    print("Перевірка площі")
    print("Shapely:", shapely_area)
    print("Gauss:", gauss_area)
    print("Monte Carlo:", mc_area)

def task_3_error():
    # Кількість точок для експерименту
    points_list = [100, 1000, 10000, 100000]

    errors = []

    print("\nДослідження точності Монте-Карло")

    for n in points_list:
        mc = monte_carlo_area(polygon, n)

        # відносна похибка у %
        error = abs(mc - shapely_area) / shapely_area * 100

        errors.append(error)

        print(f"Точки: {n:6} | Площа: {mc:.4f} | Похибка: {error:.4f}%")

    plt.figure(figsize=(8,5))
    plt.plot(points_list, errors, marker="o")
    
    plt.xlabel("Кількість точок")
    plt.ylabel("Відносна похибка (%)")
    plt.title("Залежність похибки від кількості точок")
    plt.grid(True)
    plt.show()

def task_4_benchmark():
    vertex_counts = [10, 50, 100, 1000]

    print("\nАналіз продуктивності")
    print("-" * 65)
    print(f"{'Вершини':<10}{'Shapely':<15}{'Гаус':<15}{'Monte Carlo':<15}")
    print("-" * 65)

    for n in vertex_counts:
        polygon = generate_polygon(num_points=n, radius=50)
        coords = list(polygon.exterior.coords)[:-1]

        # Shapely
        start = time.perf_counter()
        area1 = polygon.area
        shapely_time = time.perf_counter() - start

        # Гаус
        start = time.perf_counter()
        area2 = polygon_area_gauss(coords)
        gauss_time = time.perf_counter() - start

        # Monte Carlo (10000 точок)
        start = time.perf_counter()
        area3 = monte_carlo_area(polygon, 10000)
        mc_time = time.perf_counter() - start

        print(f"{n:<10}{shapely_time:<15.6f}{gauss_time:<15.6f}{mc_time:<15.6f}")

def main():
    task_2_test()
    task_3_error()
    task_4_benchmark()

if __name__ == "__main__":
    main()