def find_shortest_path(graph, start, end):
    visited = set()
    path = []

    def dfs(current):
        if current == end:
            return path
        visited.add(current)
        path.append(current)
        for neighbor in graph[current] - visited:
            new_path = dfs(neighbor)
            if new_path is not None:
                return new_path
        return None

    return dfs(start)

def main():
    num_of_rooms = int(input("Enter the no. of rooms: "))
    graph = {}

    # Gather room connections
    for _ in range(num_of_rooms):
        room = input("Enter the room name: ")
        gates = input(f"Enter connections for room {room} (eg:A,B): ").split(',')
        graph[room] = set(gates)

    initial_room = input("Enter the starting room: ")
    dest_room = input("Enter the destination room: ")
    shortest_path = find_shortest_path(graph, initial_room, dest_room)

    if shortest_path:
        print("Shortest path:", " -> ".join(shortest_path))
    else:
        print("No path found")

if __name__ == "__main__":
    main()
