# CODE
123

[HW1](https://github.com/pupupeter/CODE/blob/main/%E6%88%91%E6%98%AF12345%E5%B0%8F%E6%9C%8B%E5%8F%8B.ipynb)
[HW1-2](https://github.com/pupupeter/CODE/blob/main/week3practice.ipynb)
[HW2](https://github.com/pupupeter/CODE/blob/main/little_pca%20(1).ipynb)
[HW3](https://github.com/pupupeter/CODE/blob/main/%E4%BD%9C%E6%A5%AD3.ipynb)
[HW4](https://github.com/pupupeter/CODE/blob/main/%E4%BD%9C%E6%A5%AD3.ipynb)
附註:HW4的資料並非使用老師YOUTUBE上的CSV(YOUTUBE上為去年)，而是來自於這學期老師開的課相見歡的CSV





---------------------------------------------
# Plant vs. Zombies Shooting Game


[korean](https://github.com/pupupeter/CODE/blob/main/readme(korea%3F).md)


## 1. Introduction
This is a simple 2D game developed using Pygame. The player controls a plant that can shoot bullets to fend off approaching zombies. The game includes background images, character sprites, collision detection, and a scoring system.

## 2. Key Components
### 2.1 Pygame Initialization
- Sets the game window size (800x600).
- Defines colors used in the game (white, green, red, black).

### 2.2 Image Resources
- **Background**: Fills the entire game screen (`background.jpg`).
- **Plant Character**:
  - Image resized to 50x50 (`123123.png`).
  - Can move up, down, left, and right.
  - Shoots bullets to attack zombies.
- **Bullets**:
  - Image resized to 5x10 (`55.jpg`).
  - Moves to the right and disappears upon hitting a zombie.
- **Zombies**:
  - Image resized to 50x50 (`zombie.jpg`).
  - Spawns randomly from the right and moves toward the left.

## 3. Game Flow
### 3.1 Game Initialization
- Loads image resources and sets character starting positions.

### 3.2 Gameplay
- The player moves the plant using the **↑ ↓ ← →** keys.
- The plant automatically shoots bullets every 500 milliseconds.
- Zombies spawn randomly every 2 seconds and move from right to left.

### 3.3 Collision Detection
- When a bullet hits a zombie, both disappear, and the score increases by 10.
- If a zombie touches the plant, the game ends.

### 3.4 Scoring System
- Displays the current score in the top-left corner.

## 4. Potential Enhancements
- Add more enemy types (e.g., zombies with different speeds).
- Introduce levels (e.g., time-based survival or fixed waves).
- Upgrade plant attacks (e.g., different bullet types).

## 5. Game Over
- If a zombie reaches the plant, **"Game Over"** is displayed along with the final score.
- The game closes after 3 seconds.

## 6. Requirements
### 6.1 environment
```bash
python -m venv example-venv 
```

```bash
example-venv\Scripts
```

```bash
example-venv\Scripts
```


```bash
.\Activate.ps1
```





### 6.2 Dependencies
Ensure you have the following installed before running the game:
```bash
pip install pygame
```

### 6.2 Running the Game in VS Code
1. Open the project folder in VS Code.
2. Ensure all required image files (`background.jpg`, `123123.png`, `55.jpg`, `zombie.jpg`) are in the same directory as the Python script.
3. Run the following command in the terminal:
```bash
python game.py
```
4. The game window should open, and you can start playing.

---
Developed using **Python** and **Pygame**.

