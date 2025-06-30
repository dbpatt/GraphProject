class Graph:
    def __init__(self, is_directed=True):
        """
        Initialize an empty graph.

        Args:
            is_directed (bool): True for directed graph, False for undirected
        """
        self.adjacency_list = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph if it doesn't exist.

        Args:
            vertex: The vertex to add
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination, weight=None):
        """
        Add an edge between two vertices.

        Args:
            source: The starting vertex
            destination: The ending vertex
            weight: Optional weight for the edge
        """
        # Make sure both vertices exist
        if source not in self.adjacency_list:
            self.add_vertex(source)
        if destination not in self.adjacency_list:
            self.add_vertex(destination)

        # Add the edge
        if weight is None:
            self.adjacency_list[source].append(destination)
        else:
            self.adjacency_list[source].append((destination, weight))

        # If undirected, add edge in both directions
        if not self.is_directed:
            if weight is None:
                self.adjacency_list[destination].append(source)
            else:
                self.adjacency_list[destination].append((source, weight))

    def remove_edge(self, source, destination):
        """
        Remove an edge between two vertices.

        Args:
            source: The starting vertex
            destination: The ending vertex
        """
        if source in self.adjacency_list:
            # Handle both weighted and unweighted edges
            neighbors = self.adjacency_list[source]
            self.adjacency_list[source] = []

            for neighbor in neighbors:
                # Check if it's a tuple (weighted) or just a vertex
                if isinstance(neighbor, tuple):
                    if neighbor[0] != destination:
                        self.adjacency_list[source].append(neighbor)
                else:
                    if neighbor != destination:
                        self.adjacency_list[source].append(neighbor)

        # If undirected, remove edge in both directions
        if not self.is_directed and destination in self.adjacency_list:
            neighbors = self.adjacency_list[destination]
            self.adjacency_list[destination] = []

            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    if neighbor[0] != source:
                        self.adjacency_list[destination].append(neighbor)
                else:
                    if neighbor != source:
                        self.adjacency_list[destination].append(neighbor)

    def get_neighbors(self, vertex):
        """
        Get all neighbors of a given vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            List of neighbors (or empty list if vertex doesn't exist)
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        return []

    def dfs(self, start_vertex):
        """
        Perform Depth-First Search starting from a given vertex.

        Args:
            start_vertex: The vertex to start from

        Returns:
            List of vertices in DFS order
        """
        if start_vertex not in self.adjacency_list:
            return []

        visited = set()
        result = []

        # Stack for DFS
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # Add neighbors to stack
                neighbors = self.get_neighbors(vertex)
                for neighbor in reversed(neighbors):
                    # Handle weighted edges
                    if isinstance(neighbor, tuple):
                        neighbor_vertex = neighbor[0]
                    else:
                        neighbor_vertex = neighbor

                    if neighbor_vertex not in visited:
                        stack.append(neighbor_vertex)

        return result

    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search starting from a given vertex.

        Args:
            start_vertex: The vertex to start from

        Returns:
            List of vertices in BFS order
        """
        if start_vertex not in self.adjacency_list:
            return []

        visited = set()
        result = []

        # Queue for BFS (using list, append to add, pop(0) to remove)
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            # Add neighbors to queue
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                # Handle weighted edges
                if isinstance(neighbor, tuple):
                    neighbor_vertex = neighbor[0]
                else:
                    neighbor_vertex = neighbor

                if neighbor_vertex not in visited:
                    visited.add(neighbor_vertex)
                    queue.append(neighbor_vertex)

        return result

    def display(self):
        """
        Display the graph structure.
        """
        print("Graph structure:")
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")

"""
REFLECTIONS ON CHALLENGES FACED:

1. What parts of the project did you get stuck on?
   - Handling both weighted and unweighted edges in the same graph
   - Making remove_edge work correctly for undirected graphs
   - Ensuring DFS and BFS worked with the mixed edge types

2. Why were you stuck?
   - The data structure changes when you mix weighted/unweighted edges
   - Weighted edges are stored as tuples (vertex, weight) while unweighted are just vertices
   - Had to check types throughout the code to handle both cases

3. What information did you need to get unblocked?
   - How to check if something is a tuple in Python (isinstance function)
   - Understanding that I needed to maintain consistency in how edges are stored
   - Realizing that undirected graphs need special handling for edge removal

4. How did you know you needed that information?
   - Got TypeError when trying to compare tuples with strings
   - Tests were failing when mixing weighted and unweighted edges
   - Remove operation wasn't working symmetrically for undirected graphs

5. How did you find that information?
   - Python documentation for isinstance() and type checking
   - Testing with print statements to see data structure
   - Drawing out the graph operations on paper to visualize the problem
   - Thinking through the edge cases systematically
"""
