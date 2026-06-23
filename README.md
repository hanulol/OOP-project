# Two-Player Shooting Game

A two-player local multiplayer shooting game built with **Python** and **Pygame**. Two players battle on a split-screen arena using different bullet types and strategic reloading.

## Gameplay

- Each player has **100 HP** and **15 bullets** per magazine.
- Reduce your opponent's HP to 0 to win.
- Use different bullet types: **Normal**, **Red** (high damage, limited supply), and **Yellow** (very fast, low damage).
- Reload your ammo (a long cooldown is applied after reloading).

## Controls

### Player 1 (Blue)
| Action         | Key       |
|----------------|-----------|
| Move Up        | W         |
| Move Down      | S         |
| Move Left      | A         |
| Move Right     | D         |
| Shoot          | F         |
| Reload         | R         |
| Red Bullet     | C         |
| Yellow Bullet  | Q         |

### Player 2 (Red)
| Action         | Key           |
|----------------|---------------|
| Move Up        | ↑ (Up Arrow)  |
| Move Down      | ↓ (Down Arrow)|
| Move Left      | ← (Left Arrow)|
| Move Right     | → (Right Arrow)|
| Shoot          | / (Slash)     |
| Reload         | Right Alt     |
| Red Bullet     | , (Comma)     |
| Yellow Bullet  | . (Period)    |

## Bullet Types

| Bullet Type | Color   | Damage | Speed | Notes                        |
|-------------|---------|--------|-------|------------------------------|
| Normal      | Gold    | 10     | 8     | Standard bullet, consumes ammo |
| Red         | Red     | 20     | 8     | High damage, 10 total shared across both players |
| Yellow      | Yellow  | 5      | 25    | Very fast, low damage, consumes ammo |

> **Note:** Red Bullets are tracked by a class-level variable (`__num_red_bullets_left`) shared across all `Red_Bullet` instances, meaning both players consume from the same total pool of 10 red bullets.

## Installation

1. Make sure you have Python 3 installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## How to Play

1. The **instruction page** explains the controls. Press **SPACE** to start.
2. During the game, move, shoot, and reload to defeat your opponent.
3. When a player's HP reaches 0, the game ends.
   - Press **R** to restart.
   - Press **ESC** to quit.

## Project Structure

```
├── main.py           # Main game loop, rendering, game state management
├── player.py         # Player class (movement, shooting, reload, HP)
├── bullet.py         # Base Bullet class
├── red_bullet.py     # Red_Bullet subclass (high damage, limited supply)
└── yellow_bullet.py  # Yellow_Bullet subclass (fast, low damage)
```

## Class Hierarchy (OOP)

```
Bullet (base)
├── Red_Bullet (damage=20, class-level bullet count)
└── Yellow_Bullet (damage=5, speed=25)

Player (movement, shooting, HP, ammo management)
```

- **Inheritance**: `Red_Bullet` and `Yellow_Bullet` inherit from `Bullet`, overriding `color`, `speed`, and `damage`.
- **Encapsulation**: The `Red_Bullet` class uses a name-mangled class attribute (`__num_red_bullets_left`) to track the shared red bullet count.
- **Composition**: The `main.py` creates `Player` objects and manages a list of `Bullet` instances.