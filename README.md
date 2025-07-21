# Simple First Game (Invasion)

This is a simple 2D game built with Python and the Pygame library. It's my first GitHub project designed as a practice exercise to understand basic game mechanics.

## Gameplay
- **Objective:** Control a robot character, collect coins, and avoid monsters.
- **Controls:** Use arrow keys (`↑`, `↓`, `←`, `→`) to move your character.
- **End Condition:** The game ends immediately if your robot collides with a monster.

## Features
- **Dynamic Spawning:** Coins and monsters appear randomly at intervals.
- **Simple Collision Detection:** The game uses masks to precisely detect collisions between the robot, coins, and monsters.
- **Score Tracking:** Your current points are shown on the screen.

## Project Structure
- `Invasion` class handles the core game mechanics:
    - `spawn_coin()` and `spawn_monster()` for random generation of game objects.
    - `update_robot()`, `update_coin()`, and `update_monster()` methods to update the positions and interactions of the objects.
    - Collision detection handled by `check_collision_coin()` and `check_collision_monster()`.
    - Simple UI managed by `intro()` and `draw_screen()` methods.


## Contributions
This project is for educational purposes, and contributions or improvements are always welcome. Feel free to fork, open issues, or submit pull requests!
