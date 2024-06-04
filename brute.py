from itertools import combinations


def gen_adjacency_dict(
        distances: list[tuple[str, str, int]]
) -> dict[str, list[tuple[str, int]]]:
    adjacency_dict = {}

    for distance in distances:
        start, goal, weight = distance
        if start not in adjacency_dict:
            adjacency_dict[start] = []
        if goal not in adjacency_dict:
            adjacency_dict[goal] = []
        adjacency_dict[start].append((goal, weight))
        adjacency_dict[goal].append((start, weight))

    return adjacency_dict


def validate_answer(
        cities: dict[str, int],
        distances: list[tuple[str, str, int]]
) -> bool | tuple[bool, int]:
    """
    :return: boolean indicating if the answer is valid + cost of the answer if valid
    """
    adjacency_dict = gen_adjacency_dict(distances)
    for city in cities:
        if city not in adjacency_dict:
            adjacency_dict[city] = []
    visited = set()
    stack = list()
    overall_cost = 0

    while visited != set(cities.keys()):
        stack.append([city for city in cities if city not in visited][0])
        visited.add([city for city in cities if city not in visited][0])
        line_energy = 0
        line_distance = 0
        energy_flowing = 0

        while len(stack) > 0:
            current_city = stack.pop()
            line_energy += cities[current_city]
            if cities[current_city] > 0:
                energy_flowing += cities[current_city]
            for city in adjacency_dict[current_city]:
                if city[0] not in visited:
                    stack.append(city[0])
                    visited.add(city[0])
                    line_distance += city[1]

        if line_energy < 0:
            return False

        overall_cost += line_distance * energy_flowing

    return True, overall_cost


def brute_generate(
        cities: dict[str, int],
        distances: list[tuple[str, str, int]],
) -> int:
    all_combinations = []
    for i in range(1, len(distances) + 1):
        all_combinations.extend([list(combination) for combination in combinations(distances, i)])

    valid_combinations = []
    for combination in all_combinations:
        validation = validate_answer(cities, combination)
        if validation:
            valid_combinations.append((combination, validation[1]))

    return min(*valid_combinations, key=lambda x: x[1]) if len(valid_combinations) > 0 else -1


if __name__ == "__main__":
    test_cities = {
        "A": 20,
        "B": 0,
        "C": -10,
        "D": -10
    }
    test_distances = [
        ("A", "B", 4),
        ("B", "C", 4),
        ("A", "C", 7),
        ("B", "D", 3)
    ]

    print(brute_generate(test_cities, test_distances))
