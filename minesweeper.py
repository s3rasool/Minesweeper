n , m = map(int , input().split())
k = int(input())
game_map = []
location_of_bombs = []

def count_adjacent_bombs(board, x, y, m, n):
    count = 0
    directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == '*':
            count += 1

    return count

# n = row 
# m = column
# k = number of bobm

for i in range( n ) :
    game_map.append([])
    for y in range( m ) :
        game_map[i].append(0)

for i in range(k) :
    bomb_location = input()
    x, y = map(int, bomb_location.split())
    location_of_bombs.append((x, y))

for x , y in location_of_bombs :
    game_map[x-1][y-1] = '*'

# پر کردن اطلاعات خانه‌های حاوی بمب نیستند
for i in range(n):
    for j in range(m):
        if game_map[i][j] != '*':
            bomb_count = count_adjacent_bombs(game_map, i, j, n, m)
            game_map[i][j] = str(bomb_count)

for row in game_map:
    print(' '.join(map(str, row)))

