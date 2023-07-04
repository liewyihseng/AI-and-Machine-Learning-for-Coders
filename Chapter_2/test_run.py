#!/usr/bin/python

#def displayPathtoPrincess(n,grid):
#print all the moves here
#for x in range(0, m):
#    for y in range(0, m):
#        if


m = 5
grid = ['-----', '--m--', '-----', '-----', '----p']

n_grid = []
for i in grid:
    n_grid.append([*i])

m_x = 0
m_y = 0
p_x = 0
p_y = 0
for x in range(0, m):
    for y in range(0, m):
        if n_grid[x][y] == 'm':
            m_x = y
            m_y = x
        if n_grid[x][y] == 'p':
            p_x = y
            p_y = x
diff_x = m_x - p_x
diff_y = m_y - p_y
print(n_grid)
print(diff_x)
print(diff_y)

if diff_x < 0:
    dir_x = 'RIGHT'
else:
    dir_x = 'LEFT'

if diff_y < 0:
    dir_y = 'DOWN'
else:
    dir_y = 'UP'
diff_x = abs(diff_x)
diff_y = abs(diff_y)
print(diff_x)
print(diff_y)

while diff_x > 0:
    print(dir_x)
    diff_x -= 1
while diff_y > 0:
    print(dir_y)
    diff_y -= 1

#displayPathtoPrincess(m,grid)