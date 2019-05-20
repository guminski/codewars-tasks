
def tower_builder(n_floors):  
    tower = []  
    for i in range(1, n_floors + 1):
        spaces = ''.join(' ') * (n_floors - i)
        stars = ''.join('*') * ((i * 2) - 1)
        floor = spaces + stars + spaces
        tower.append(floor)
    return tower

for e in tower_builder(6):
    print(e)
