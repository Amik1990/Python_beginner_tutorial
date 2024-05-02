# Tří seznamy v seznamu
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# 1. Vypíše hodnotu ve 3 řádku na 2 místě
print(number_grid[2][1])

# 2. For loop. Vypíše obsah seznamu. Tzn. vypíše pod sebou seznamy  [1, 2, 3],  [4, 5, 6], [7, 8, 9], [0]
for row in number_grid:
    print(row)

# 3. For loop (složený). Vypíše pod sebou jednotlivé hodnoty seznamů v seznamu. 1,2,3,4,5,6,7,8,9,0
for row in number_grid:
    for col in row:
        print(col)


# Můj příklad se slovníkem
number_grid2 = {
    1: "Adam",
    2: "Pepa",
    3: "John",
    4: "Roland"
}

print(number_grid2[2])

for key in number_grid2:
    print(key)
