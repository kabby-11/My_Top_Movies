from collections import deque

def breadth_first_search(graph, start, goal):
    """
    Finds the shortest path between two rooms in a graph using BFS.
    Args:
    graph: A dictionary that maps each room to a set of its neighboring
    rooms.
    start: The name of the starting room.
    goal: The name of the destination room.
    Returns:
    A list of rooms that form the shortest path from the start room to the
    destination room, or None if no path exists.
    """
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)
        print("Visiting:", current_node)
        if current_node == goal:
            return path
        for neighbor in graph[current_node] - visited:
            queue.append((neighbor, path + [neighbor]))
    return None

def main():
    num_of_rooms = int(input("Enter the no. of rooms: "))
    graph = {}
    # Gather room connections
    for _ in range(num_of_rooms):
        room_name = input("Enter the room name: ")
        connections = input(f"Enter connections for room {room_name} (eg: A,B): ").split(',')
        graph[room_name] = set(connections)

    start_room = input("Enter the starting room: ")
    goal_room = input("Enter the goal room: ")
    path = breadth_first_search(graph, start_room, goal_room)

    if path:
        print("Path found:", ' -> '.join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
