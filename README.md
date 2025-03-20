# CODE
123

[HW1](https://github.com/pupupeter/CODE/blob/main/%E6%88%91%E6%98%AF12345%E5%B0%8F%E6%9C%8B%E5%8F%8B.ipynb)


---------------------------------------------
# Plant vs. Zombies Shooting Game

## 1. Introduction
This is a simple 2D game developed using Pygame. The player controls a plant that can shoot bullets to fend off approaching zombies. The game includes background images, character sprites, collision detection, and a scoring system.

## 2. Key Components
### 2.1 Pygame Initialization
- Sets the game window size (`800x600`).
- Defines colors used in the game (white, green, red, black).

### 2.2 Image Resources
- **Background**: Fills the entire game screen (`background.jpg`).
- **Plant Character**:
  - Image resized to `50x50` (`123123.png`).
  - Can move up, down, left, and right.
  - Shoots bullets to attack zombies.
- **Bullets**:
  - Image resized to `5x10` (`55.jpg`).
  - Moves to the right and disappears upon hitting a zombie.
- **Zombies**:
  - Image resized to `50x50` (`zombie.jpg`).
  - Spawns randomly from the right and moves toward the left.

## 3. Game Flow
1. **Game Initialization**: Loads image resources and sets character starting positions.
2. **Gameplay**:
   - The player moves the plant using the `↑ ↓ ← →` keys.
   - The plant automatically shoots bullets every 500 milliseconds.
   - Zombies spawn randomly every 2 seconds and move from right to left.
3. **Collision Detection**:
   - When a bullet hits a zombie, both disappear, and the score increases by 10.
   - If a zombie touches the plant, the game ends.
4. **Scoring System**: Displays the current score in the top-left corner.

## 4. Potential Enhancements
- **Add More Enemy Types** (e.g., zombies with different speeds).
- **Introduce Levels** (e.g., time-based survival or fixed waves).
- **Upgrade Plant Attacks** (e.g., different bullet types).

## 5. Game Over
- If a zombie reaches the plant, "Game Over" is displayed along with the final score.
- The game closes after 3 seconds.

---
**Development Tools**: Python, Pygame
