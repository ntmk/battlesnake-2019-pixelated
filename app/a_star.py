from utils import distance, reconstruct_path, neighbours
from gameboard import GameBoard


def a_star(start, goal, grid, tail, ignore_list):
    """
    A-Star algorithm for pathfinding\n
    
    
    @param start -> Starting point\n
    @param goal -> End point\n
    @param grid -> Updated grid\n
    @param tail -> Tail of snake / additional coords to ignore\n
    @param ignore_list -> Grid locations to avoid
    """
    start = tuple(start)
    goal = tuple(goal)
    closed_set = []
    open_set   = [start]
    came_from = {} 
    
    g_score = GameBoard(grid.height, grid.width, 10)
    g_score.set_cell(start, 0)
    
    f_score = GameBoard(grid.height, grid.width, 10)
    f_score.set_cell(start, distance(start,goal))

    while(len(open_set) > 0):
        current = min(open_set, key=lambda p: f_score.get_cell(p))

        if (current == goal):
            return reconstruct_path(came_from, goal)
        open_set.remove(current)

        closed_set.append(current)
        
        for neighbour in neighbours(current, grid, int(g_score.get_cell(current)), tail, ignore_list):
            if neighbour in closed_set:
                continue
            tentative_g_score = g_score.get_cell(current) + distance(current,neighbour)
            if neighbour not in open_set:
                open_set.append(neighbour)
            elif tentative_g_score == g_score.get_cell(neighbour):
                dx1 = current[0] - goal[0]
                dy1 = current[1] - goal[1]
                dx2 = start[0] - goal[0]
                dy2 = start[1] - goal[1]
                cross = abs(dx1*dy2 - dx2*dy1)
                tentative_g_score += cross*0.001
            elif tentative_g_score > g_score.get_cell(neighbour):
                continue
            came_from[neighbour] = current
            g_score.set_cell(neighbour, tentative_g_score)
            f_score.set_cell(neighbour, tentative_g_score + distance(neighbour,goal))
    return None