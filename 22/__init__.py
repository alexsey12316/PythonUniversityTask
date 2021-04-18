from enum import Enum

maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]


def custom_input():
    try:
        a = [int(i) for i in input().split(' ')]
        if a[0] < 0 or a[1] < 0 or a[0] > len(maze) or a[1] > len(maze[0]) or maze[a[0]][a[1]] == '#':
            raise Exception
        return a[0], a[1]
    except:
        print('Неверные координаты')
        print('Попробуйте снова')
        return custom_input()


list_of_exits = []
result = []


def step(i: int, j: int):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
        if maze[i][j] == ' ':
            maze[i][j] = '*'
            path(i, j)
        elif maze[i][j].isalpha():
            result.append(maze[i][j])
            maze[i][j] = '*'


def path(i: int, j: int):
    step(i - 1, j)
    step(i, j + 1)
    step(i, j - 1)
    step(i + 1, j)


for i in range(0, len(maze)):
    maze[i] = list(maze[i])

x, y = custom_input()
maze[x][y] = '*'
path(x, y)
result.sort()
print(result)
for s in maze:
    print(s)
