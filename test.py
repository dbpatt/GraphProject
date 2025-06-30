from main import Graph

# Test the implementation
if __name__ == "__main__":
    # Create a directed graph (like FNAF paths!)
    print("=== DIRECTED GRAPH TEST (FNAF Example) ===")
    fnaf_graph = Graph(is_directed=True)

    # Add Freddy's path
    fnaf_graph.add_edge("Show Stage", "Dining Area")
    fnaf_graph.add_edge("Dining Area", "Restrooms")
    fnaf_graph.add_edge("Restrooms", "Kitchen")
    fnaf_graph.add_edge("Kitchen", "East Hall")
    fnaf_graph.add_edge("East Hall", "East Corner")
    fnaf_graph.add_edge("East Corner", "Office")

    # Add Foxy's path
    fnaf_graph.add_edge("Pirate Cove", "West Hall")
    fnaf_graph.add_edge("West Hall", "West Corner")
    fnaf_graph.add_edge("West Corner", "Office")

    fnaf_graph.display()

    print("\nDFS from Show Stage:", fnaf_graph.dfs("Show Stage"))
    print("BFS from Show Stage:", fnaf_graph.bfs("Show Stage"))

    # Test edge removal
    print("\n=== REMOVING EDGE TEST ===")
    fnaf_graph.remove_edge("Kitchen", "East Hall")
    print("After removing Kitchen -> East Hall edge:")
    fnaf_graph.display()

    # Create an undirected graph (like Mario 64 castle!)
    print("\n=== UNDIRECTED GRAPH TEST (Mario 64 Example) ===")
    mario_graph = Graph(is_directed=False)

    # Add castle connections
    mario_graph.add_edge("Castle Hub", "Bob-omb Battlefield")
    mario_graph.add_edge("Castle Hub", "Whomp's Fortress")
    mario_graph.add_edge("Castle Hub", "Cool Cool Mountain")
    mario_graph.add_edge("Castle Hub", "Basement")
    mario_graph.add_edge("Basement", "Hazy Maze Cave")
    mario_graph.add_edge("Basement", "Lethal Lava Land")

    mario_graph.display()

    print("\nNeighbors of Castle Hub:", mario_graph.get_neighbors("Castle Hub"))
    print("DFS from Castle Hub:", mario_graph.dfs("Castle Hub"))
    print("BFS from Castle Hub:", mario_graph.bfs("Castle Hub"))

    # Test weighted edges
    print("\n=== WEIGHTED GRAPH TEST ===")
    weighted_graph = Graph(is_directed=True)

    # Add weighted edges (star requirements)
    weighted_graph.add_edge("Castle", "Bob-omb", 0)
    weighted_graph.add_edge("Castle", "Whomp's", 1)
    weighted_graph.add_edge("Castle", "Cool Mountain", 3)
    weighted_graph.add_edge("Castle", "Bowser Door", 8)

    weighted_graph.display()
