import os
import random
import time

width = 40
height = 20
player1_symbol = '1'
player2_symbol = '2'
empty_symbol = ' '
wall_symbol = '#'
bullet_symbol = '*'
player1_start_pos = (2, 2)
player2_start_pos = (width - 3, height - 3)
bullet_speed = 0.1  


class Tank:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def move(self, dx, dy, walls):
        if 0 <= self.x + dx < width and 0 <= self.y + dy < height and (self.x + dx, self.y + dy) not in walls:
            self.x += dx
            self.y += dy

    def shoot(self):
        return Bullet(self.x, self.y, self.symbol)


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == player1_symbol:
            self.x += 1
        elif self.direction == player2_symbol:
            self.x -= 1

    def is_out_of_bounds(self):
        return self.x < 0 or self.x >= width

    def is_collision(self, x, y):
        return self.x == x and self.y == y


def draw_game(player1, player2, bullets, walls):
    os.system('cls' if os.name == 'nt' else 'clear')  

    field = [[empty_symbol] * width for _ in range(height)]
    for x, y in walls:
        field[y][x] = wall_symbol
    field[player1.y][player1.x] = player1.symbol
    field[player2.y][player2.x] = player2.symbol
    for bullet in bullets:
        field[bullet.y][bullet.x] = bullet_symbol

    print('+---' * width + '+')
    for row in field:
        print('|' + ' '.join(row) + '|')

    print('+---' * width + '+')


def check_collision(player1, player2, bullets, walls):
    for bullet in bullets:

        if (player1.x == bullet.x and player1.y == bullet.y):
            return True, "Player 2"

        elif (player2.x == bullet.x and player2.y == bullet.y):
            return True, "Player 1"
    return False, None


def main():
    player1 = Tank(*player1_start_pos, player1_symbol)
    player2 = Tank(*player2_start_pos, player2_symbol)
    bullets = []
    player1_score = 0
    player2_score = 0

    walls = [(5, 5), (5, 6), (5, 7), (35, 15), (35, 16), (35, 17)]

    while True:
        draw_game(player1, player2, bullets, walls)
        time.sleep(bullet_speed)

        for bullet in bullets:
            bullet.move()

        bullets = [bullet for bullet in bullets if not bullet.is_out_of_bounds()]

        if random.random() < 0.1:
            bullets.append(player1.shoot())
        if random.random() < 0.1:
            bullets.append(player2.shoot())

        collision, winner = check_collision(player1, player2, bullets, walls)
        if collision:
            if winner == "Player 1":
                player1_score += 1
            elif winner == "Player 2":
                player2_score += 1
            print("\nPlayer 1 Score:", player1_score)
            print("Player 2 Score:", player2_score)
            time.sleep(2)
            bullets = []
            player1.x, player1.y = player1_start_pos
            player2.x, player2.y = player2_start_pos

        if player1_score >= 3:
            print("\nPlayer 1 venceu!")
            break
        elif player2_score >= 3:
            print("\nPlayer 2 venceu!")
            break


if __name__ == "__main__":
    main()
