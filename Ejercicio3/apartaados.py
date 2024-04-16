import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'Rivendell': {'Minas Tirith': 5, 'Moria': 10},
    'Minas Tirith': {'Rivendell': 5, 'Moria': 2, 'Gondor': 3},
    'Moria': {'Rivendell': 10, 'Minas Tirith': 2, 'Gondor': 4},
    'Gondor': {'Minas Tirith': 3, 'Moria': 4}
}

start_city = input("Enter the start city: ")
end_city = input("Enter the end city: ")

distances = dijkstra(graph, start_city)
shortest_distance = distances[end_city]

print(f"The shortest distance between {start_city} and {end_city} is {shortest_distance}")