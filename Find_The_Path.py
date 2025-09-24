from collections import deque

def canExit(maze):
    if not maze or not maze[0]:
        return False
    
    rows, cols = len(maze), len(maze[0])
    
    # If start or end is blocked, return False immediately
    if maze[0][0] == 1 or maze[rows - 1][cols - 1] == 1:
        return False
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Down, Up, Right, Left
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        r, c = queue.popleft()
        
        # If we reach the bottom-right corner then we have found a path
        if (r, c) == (rows - 1, cols - 1):
            return True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols 
                and maze[nr][nc] == 0 
                and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))
    
    return False
