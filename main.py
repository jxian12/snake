import pygame
import random

# 設定遊戲視窗大小和背景顏色
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BG_COLOR = (255, 255, 255)

# 設定貪吃蛇的初始位置、長度和速度
SNAKE_SIZE = 10
SNAKE_COLOR = (0, 0, 0)
SNAKE_SPEED = 10
INITIAL_SNAKE_LENGTH = 5

# 設定食物的大小和顏色
FOOD_SIZE = 10
FOOD_COLOR = (255, 0, 0)

# 初始化 pygame
pygame.init()

# 創建遊戲視窗
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# 設定字體和字體大小
font = pygame.font.Font(None, 30)

# 創建一條貪吃蛇
snake = []
for i in range(INITIAL_SNAKE_LENGTH):
    snake.append(pygame.Rect(320, 240 + i * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE))

# 創建一個食物
food = pygame.Rect(random.randint(0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)

# 設定初始移動方向
direction = 'up'

# 遊戲主迴圈
while True:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'

    # 移動貪吃蛇的頭部
    if direction == 'up':
        snake_head = pygame.Rect(snake[0].left, snake[0].top - SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'down':
        snake_head = pygame.Rect(snake[0].left, snake[0].top + SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'left':
        snake_head = pygame.Rect(snake[0].left - SNAKE_SIZE, snake[0].top, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'right':
        snake_head = pygame.Rect(snake[0].left + SNAKE_SIZE, snake[0].top, SNAKE_SIZE, SNAKE_SIZE)

    # 插入貪吃蛇的頭部到列表中
    snake.insert(0, snake_head)

    # 判斷貪吃蛇是否吃到食物
    if snake_head.colliderect(food):
        food = pygame.Rect(random.randint(0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE),
                           FOOD_SIZE, FOOD_SIZE)
    else:
        snake.pop()

    # 檢查貪吃蛇是否碰到邊界或自己，如果是遊戲結束
    if snake_head.left < 0 or snake_head.right > SCREEN_WIDTH or snake_head.top < 0 or snake_head.bottom > SCREEN_HEIGHT:
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (
        SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        quit()
    for i in range(1, len(snake)):
        if snake_head.colliderect(snake[i]):
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (
            SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            quit()

    # 繪製遊戲視窗
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, FOOD_COLOR, food)
    for rect in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, rect)
    pygame.display.update()

    # 控制遊戲速度
    pygame.time.delay(1000 // SNAKE_SPEED)


