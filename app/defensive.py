from a_star import a_star
from utils import neighbours, distance, check_ahead


SNAKE = 1
DANGER = 5


def find_my_tail(charlie, grid):
    """
    Find path to onw tail\n
    @param charlie -> Own snake information\n
    @param grid -> Updated grid\n
    @return temp_path -> Path to your own tail
    """ 
    my_tail_path = a_star(charlie.head, charlie.tail, grid, charlie.coords, [SNAKE, DANGER])
    return my_tail_path


def find_my_tail_emergency(charlie, grid):
    """
    Find path to onw tail\n
    @param charlie -> Own snake information\n
    @param grid -> Updated grid\n
    @return temp_path -> Path to your own tail
    """ 
    my_tail_path = a_star(charlie.head, charlie.tail, grid, charlie.coords, [SNAKE])
    return my_tail_path


def find_enemy_tail(charlie, enemies, grid):
    """
    Find path to available enemy tail\n
    @param charlie -> Own snake information\n
    @param enemies -> Array of enemy snakes\n
    @param grid -> Updated grid\n
    @return temp_path -> Path to enemy tail
    """
    for enemy in enemies:
        if distance(charlie.head, enemy.tail) > 3:
            continue
        enemy_tail_path = a_star(charlie.head, enemy.tail, grid, charlie.coords, [SNAKE, DANGER])
        if(enemy_tail_path):
            return enemy_tail_path


def trouble(charlie, grid):
    """
    Select a random available move\n
    @param charlie -> Own snake information\n
    @param grid -> Updated grid\n
    @return temp_path -> Random safe spot to move
    """
    for neighbour in neighbours(charlie.head, grid, 0, charlie.tail, [SNAKE]):
        trouble_path = a_star(charlie.head, neighbour, grid, charlie.coords, [SNAKE])
        return trouble_path


def eat_food(charlie, grid, foods, check_grid):
    """
    Finds a path to food\n

    @param Charlie -> Own snake information\n
    @param grid -> Updated grid\n
    @param foods -> List of food on the board\n
    @param check_grid -> Grid to update for food\n
    @return path -> Ideal path to eat food
    """
    for food in foods:
        tentative_path = a_star(charlie.head, food, grid, charlie.coords, [SNAKE, DANGER])
        if not tentative_path:
            continue
        return check_ahead(tentative_path, charlie, food, grid, check_grid)