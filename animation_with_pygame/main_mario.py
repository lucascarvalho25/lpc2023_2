import pygame
import spritesheet

pygame.init()

#Para mover entre as animações, use as setas direcionais UP e DOWN.

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))     
pygame.display.set_caption("Animation with Pygame: Mario")

sprite_sheet_image = pygame.image.load("assets/small_mario_spritesheet.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

background_color = (50, 50, 50)
white_color = (255, 255, 255)

#Create animation list
animation_list = []
animation_steps = [4, 4, 7]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 110
frame = 0
step_counter = 0

for animation in animation_steps:
	temp_img_list = []
	for _ in range(animation):
		temp_img_list.append(sprite_sheet.get_image(step_counter, 23, 23, 6, white_color))
		step_counter += 1

	animation_list.append(temp_img_list)


run = True
while run:

	#Update background
	screen.fill(background_color)

	#Update animation
	current_time = pygame.time.get_ticks()
	if current_time - last_update >= animation_cooldown:
		frame += 1
		last_update = current_time

		if frame >= len(animation_list[action]):
			frame = 1


	#Show frame image
	screen.blit(animation_list[action][frame], (0, 0))
	
	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_DOWN and action > 0:
				animation_cooldown = 115
				action -= 1
				if action == 1:
					animation_cooldown = 55
				frame = 0

			if event.key == pygame.K_UP and action < len(animation_list) - 1:
				animation_cooldown = 55
				action += 1
				if action == 2:
					animation_cooldown = 115
				frame = 0

	pygame.display.update()