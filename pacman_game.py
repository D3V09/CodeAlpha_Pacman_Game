import random

# Initialize game variables
rows = 5
cols = 10
pacman_row = 3
pacman_col = 5
ghost_row = random.randint(0, rows - 1)
ghost_col = random.randint(0, cols - 1)
food_row = random.randint(0, rows - 1)
food_col = random.randint(0, cols - 1)
score = 0

# Main game loop
n=0
while n < 10:
    # Display game board
    for i in range(rows):
        for j in range(cols):
            if i == pacman_row and j == pacman_col:
                print("P", end="")
            elif i == ghost_row and j == ghost_col:
                print("G", end="")
            elif i == food_row and j == food_col:
                print("F", end="")
            else:
                print(".", end="")
        print()
    n=n-1

    # Get user input
    direction = input("Enter direction (w/a/s/d): ")

    # Move Pacman
    if direction == "w":
        pacman_row -= 1
    elif direction == "s":
        pacman_row += 1
    elif direction == "a":
        pacman_col -= 1
    elif direction == "d":
        pacman_col += 1

    # Move Ghost
    ghost_row += random.choice([-1, 0, 1])
    ghost_col += random.choice([-1, 0, 1])

    # Check for collisions
    if pacman_row == ghost_row and pacman_col == ghost_col:
        print("Game Over!")
        break

    if pacman_row == food_row and pacman_col == food_col:
        score += 10
        food_row = random.randint(0, rows - 1)
        food_col = random.randint(0, cols - 1)

    # Check win condition
    if score >= 100:
        print("You Win!")
        break
