


class Hysteresis:
    def __init__(self):
        self.visited = []
    
    def apply(self, magnitude, Th, Tl):
        height = len(magnitude)
        width = len(magnitude[0])
        edges = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            edges.append(row)
        
        self.visited = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(False)
            self.visited.append(row)
        
        for i in range(height):
            magnitude[i][0] = 0
            magnitude[i][width - 1] = 0
        for j in range(width):
            magnitude[0][j] = 0
            magnitude[height - 1][j] = 0
        
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if magnitude[i][j] >= Th and not self.visited[i][j]:
                    self.follow_edge(magnitude, edges, i, j, Tl)
        edges_output = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(edges[i][j] * 255)
            edges_output.append(row)
        
        return edges_output
    
    def follow_edge(self, magnitude, edges, start_i, start_j, Tl):
        height = len(magnitude)
        width = len(magnitude[0])
        stack = [(start_i, start_j)]
        while stack:
            i, j = stack.pop()
            if i < 0 or i >= height or j < 0 or j >= width:
                continue
            if self.visited[i][j]:
                continue
            if magnitude[i][j] < Tl:
                continue
            edges[i][j] = 1
            self.visited[i][j] = True
            neighbors = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)
            ]
            for di, dj in neighbors:
                ni, nj = i + di, j + dj
                if (0 <= ni < height and 0 <= nj < width and 
                    not self.visited[ni][nj] and magnitude[ni][nj] >= Tl):
                    stack.append((ni, nj))