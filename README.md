# Minesweeper Game

## Introduction
This simple Minesweeper game is designed for beginner programmers to understand basic concepts of 2D arrays, loops, functions, and input handling in Python. Minesweeper is a classic single-player puzzle game where the player must uncover cells on a grid containing hidden mines without triggering them.

## Usage
The program takes input for the dimensions of the game board (`n` rows and `m` columns), the number of bombs (`k`), and the locations of these bombs. It then generates a Minesweeper board, marking bomb locations with '*' and filling other cells with the count of adjacent bombs. Finally, it prints the resulting Minesweeper board.

## How to Play
1. Input the dimensions of the board (`n` rows and `m` columns).
2. Input the number of bombs (`k`).
3. Enter the locations of the bombs, providing the row and column for each bomb.
4. The program will generate the Minesweeper board, revealing the count of adjacent bombs in each cell.
5. Players can analyze the board to identify safe cells and avoid bombs.

## Code Explanation
The code consists of a function `count_adjacent_bombs` to calculate the number of bombs around a given cell. It utilizes a 2D list (`game_map`) to represent the Minesweeper board. Bomb locations are marked with '*', and other cells contain the count of adjacent bombs. The program uses nested loops for input, board generation, and bomb counting.

## Example
For a 3x3 board with 2 bombs at locations (1, 1) and (2, 2), the program output might look like this:

## Purpose
This project is intended for beginner programmers to practice basic Python programming concepts such as loops, functions, input handling, and 2D arrays. It provides a practical example of solving a simple problem in a step-by-step manner.

Feel free to explore and modify the code to enhance your understanding of Python programming and game development!
