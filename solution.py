import sys
import heapq


def load_cities(
        path: str
) -> dict[str, int]:
    cities = {}
    with open(path, "r") as file:
        for line in file.readlines():
            city, energy = line.strip().split()
            cities[city] = int(energy)
    return cities


def load_graph(
        path: str
) -> dict[str, list[tuple[str, int]]]:
    graph = {}
    with open(path, "r") as file:
        for line in file.readlines():
            city1, city2, distance = line.strip().split()
            if city1 not in graph:
                graph[city1] = []
            if city2 not in graph:
                graph[city2] = []
            graph[city1].append((city2, int(distance)))
            graph[city2].append((city1, int(distance)))
    return graph


def memorize(f):
    memory = {}

    def remembered_f(*args, **kwargs):
        if str(args) + str(kwargs) not in memory:
            result = f(*args, **kwargs)
            memory[str(args) + str(kwargs)] = result
        return memory[str(args) + str(kwargs)]

    return remembered_f


@memorize
def dijkstra(
        graph: dict[str, list[tuple[str, int]]],
        start: str
) -> tuple[dict[str, int], dict[str, list[str, str]]]:
    priority_queue = [(0, start)]
    distances = {start: 0}
    paths = {start: []}

    while len(priority_queue) > 0:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance <= distances.get(current_node, float('inf')):
            for neighbor, distance in graph[current_node]:
                neighbor_distance = current_distance + distance
                if neighbor_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = neighbor_distance
                    paths[neighbor] = paths[current_node] + [neighbor]
                    heapq.heappush(priority_queue, (neighbor_distance, neighbor))

    return distances, paths


def calculate_min_cost(
        cities: dict[str, int],
        graph: dict[str, list[tuple[str, int]]]
) -> tuple[list[tuple[str, str, int, list[str]]], int]:
    total_cost = 0
    energy_flow = []
    while any([balance < 0 for balance in cities.values()]):
        consumers = [city for city, energy in cities.items() if energy < 0]
        producers = [city for city, energy in cities.items() if energy > 0]
        min_distance = float('inf')
        min_path = None
        best_consumer = None
        best_producer = None

        for consumer in consumers:
            distances, paths = dijkstra(graph, consumer)
            for producer in producers:
                if producer in distances and distances[producer] < min_distance:
                    min_distance = distances[producer]
                    min_path = paths[producer]
                    best_consumer = consumer
                    best_producer = producer

        if min_path is None:
            return [], -1

        energy_transferred = min(cities[best_producer], -cities[best_consumer])
        total_cost += min_distance * energy_transferred
        energy_flow.append((best_producer, best_consumer, energy_transferred, min_path))
        cities[best_consumer] += energy_transferred
        cities[best_producer] -= energy_transferred

    return energy_flow, total_cost


def run():
    if len(sys.argv) == 3:
        _, cities_path, distances_path = sys.argv
        cities = load_cities(cities_path)
        graph = load_graph(distances_path)

        if sum(cities.values()) < 0:
            print("Optimization impossible. Overall used energy bigger than overall produced energy.")
            return

        min_cost = calculate_min_cost(cities, graph)
        if min_cost == ([], -1):
            print("Optimization impossible."
                  " No possible routes arrangement resulting in meeting the energy needs of each city.")
            return

        print(f'Minimal cost: {min_cost[1]}')
        print(f'Routes arrangement:')
        for route in min_cost[0]:
            print(f'    From: {route[0]}'
                  f' To: {route[1]}'
                  f' Energy transferred: {route[2]}'
                  f' Through: {", ".join(reversed(route[3][:-1])) if len(route[3][:-1]) > 0 else "direct connection"}')
    else:
        print("Invalid program usage. Correct usage: solution.py cities_file_name distances_file_name")


if __name__ == "__main__":
    run()
