import pygame
import griditems
from imageloader import ImageHandler
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

running = 1
score = 0
attempts = 0
timer = 0

reveal_list = list()

rect_dict = {'chicken': (128, 0, 64, 64), 'donut': (192, 0, 64, 64),
             'apple': (64, 0, 64, 64), 'banana': (64, 64, 64, 64),
             'strawberry': (64, 192, 64, 64), 'sushi': (128, 192, 64, 64),
             'watermelon': (64, 256, 64, 64), 'egg': (128, 256, 64, 64),
             'fries': (128, 320, 64, 64), 'hamburger': (128, 384, 64, 64),
             'background': (0, 256, 450, 128), 'cover': (0, 384, 256, 128)}

pygame.init()

game_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen_width = game_screen.get_width()
screen_height = game_screen.get_height()

text_font = pygame.font.SysFont('COMIC SANS MS', 100)

foods = pygame.image.load('.\Images\Food Pack.png')
foods = pygame.transform.scale(foods, (256, 640))
background_cloud = pygame.image.load('.\Images\cloudcover.png')
background_cloud = pygame.transform.scale(background_cloud, (512, 512))
background_cloud.fill((255, 255, 255, 220), None, pygame.BLEND_RGBA_MULT)
cloud_cover = pygame.image.load('.\Images\cloudcover.png')
cloud_cover = pygame.transform.scale(cloud_cover, (512, 512))

winner_image = ImageHandler('.\Images\Winner.png', 0, 100, game_screen)
winner_image.resize(screen_width, screen_height)
title_image = ImageHandler('.\Images\Title.png', 0, 0, game_screen)
title_image.resize(screen_width, screen_height)
play_button = ImageHandler('.\Images\Play1.png', 730, 900, game_screen)
play_button.resize(screen_width, screen_height)
play_button_over = ImageHandler('.\Images\Play2.png', 730, 900, game_screen)
play_button_over.resize(screen_width, screen_height)
play_button_click = ImageHandler('.\Images\Play3.png', 730, 900, game_screen)
play_button_click.resize(screen_width, screen_height)
play_again = ImageHandler('.\Images\playagain.png', 405, 900, game_screen)
play_again.resize(screen_width, screen_height)
play_again_over = ImageHandler('.\Images\playagain1.png', 405, 900, game_screen)
play_again_over.resize(screen_width, screen_height)
play_again_click = ImageHandler('.\Images\playagain2.png', 405, 900, game_screen)
play_again_click.resize(screen_width, screen_height)

play_rect = play_button.get_rect()
play_again_rect = play_again.get_rect()

food_col_1 = int(screen_height * .092)
food_col_2 = int(screen_height * .324)
food_col_3 = int(screen_height * .56)
food_col_4 = int(screen_height * .787)
food_row_1 = int(screen_width * .172)
food_row_2 = int(screen_width * .328)
food_row_3 = int(screen_width * .484)
food_row_4 = int(screen_width * .641)
food_row_5 = int(screen_width * .797)

grid1_1 = griditems.FoodCloud(food_row_1, food_col_1, foods, rect_dict['chicken'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid1_2 = griditems.FoodCloud(food_row_2, food_col_1, foods, rect_dict['donut'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid1_3 = griditems.FoodCloud(food_row_3, food_col_1, foods, rect_dict['apple'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid1_4 = griditems.FoodCloud(food_row_4, food_col_1, foods, rect_dict['banana'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid1_5 = griditems.FoodCloud(food_row_5, food_col_1, foods, rect_dict['strawberry'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid2_1 = griditems.FoodCloud(food_row_1, food_col_2, foods, rect_dict['sushi'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid2_2 = griditems.FoodCloud(food_row_2, food_col_2, foods, rect_dict['watermelon'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid2_3 = griditems.FoodCloud(food_row_3, food_col_2, foods, rect_dict['egg'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid2_4 = griditems.FoodCloud(food_row_4, food_col_2, foods, rect_dict['fries'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid2_5 = griditems.FoodCloud(food_row_5, food_col_2, foods, rect_dict['hamburger'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid3_1 = griditems.FoodCloud(food_row_1, food_col_3, foods, rect_dict['hamburger'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid3_2 = griditems.FoodCloud(food_row_2, food_col_3, foods, rect_dict['fries'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid3_3 = griditems.FoodCloud(food_row_3, food_col_3, foods, rect_dict['egg'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid3_4 = griditems.FoodCloud(food_row_4, food_col_3, foods, rect_dict['watermelon'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid3_5 = griditems.FoodCloud(food_row_5, food_col_3, foods, rect_dict['sushi'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid4_1 = griditems.FoodCloud(food_row_1, food_col_4, foods, rect_dict['strawberry'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid4_2 = griditems.FoodCloud(food_row_2, food_col_4, foods, rect_dict['banana'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid4_3 = griditems.FoodCloud(food_row_3, food_col_4, foods, rect_dict['apple'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid4_4 = griditems.FoodCloud(food_row_4, food_col_4, foods, rect_dict['donut'],
                              cloud_cover, rect_dict['cover'], game_screen)
grid4_5 = griditems.FoodCloud(food_row_5, food_col_4, foods, rect_dict['chicken'],
                              cloud_cover, rect_dict['cover'], game_screen)

cloud1 = griditems.CloudHandler(1, background_cloud, rect_dict['background'],
                                game_screen, screen_height, screen_width)
cloud2 = griditems.CloudHandler(1.1, background_cloud, rect_dict['background'],
                                game_screen, screen_height, screen_width)
cloud3 = griditems.CloudHandler(.5, background_cloud, rect_dict['background'],
                                game_screen, screen_height, screen_width)
cloud4 = griditems.CloudHandler(1.24, background_cloud, rect_dict['background'],
                                game_screen, screen_height, screen_width)
cloud5 = griditems.CloudHandler(.65, background_cloud, rect_dict['background'],
                                game_screen, screen_height, screen_width)

cloud_list = [cloud1, cloud2, cloud3, cloud4, cloud5]

food_list = [grid1_1, grid1_2, grid1_3, grid1_4, grid1_5, grid2_1,
             grid2_2, grid2_3, grid2_4, grid2_5, grid3_1, grid3_2,
             grid3_3, grid3_4, grid3_5, grid4_1, grid4_2, grid4_3,
             grid4_4, grid4_5]

cloud_cover_list = [grid1_1, grid1_2, grid1_3, grid1_4, grid1_5, grid2_1,
                    grid2_2, grid2_3, grid2_4, grid2_5, grid3_1, grid3_2,
                    grid3_3, grid3_4, grid3_5, grid4_1, grid4_2, grid4_3,
                    grid4_4, grid4_5]

while running > 0:
    scoreboard = text_font.render('Score: ' + str(score), 1, (0, 0, 0))
    track_attempts = text_font.render('Attempts: ' + str(attempts), 1, (0, 0, 0))

    game_screen.fill((51, 204, 255))

    for cloud in cloud_list:
        cloud.cloud_update()
        cloud.background_cloud_draw()

    if running == 1:
        title_image.draw()
        play_button.draw()

        if play_rect.collidepoint(pygame.mouse.get_pos()):
            play_button_over.draw()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

            elif event.type == QUIT:
                running = 0

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if play_rect.collidepoint(pos):
                        running = 2

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if play_rect.collidepoint(pos):
                        play_button_click.draw()

    if running == 2:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

            elif event.type == QUIT:
                running = 0

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and len(reveal_list) < 2:
                    pos = pygame.mouse.get_pos()
                    timer = 40
                    for cloud in cloud_cover_list:
                        if cloud.collision(pos):
                            reveal_list.append(cloud)
                            cloud_cover_list.remove(cloud)

        if timer > 0:
            timer -= 1

        if len(reveal_list) >= 2 and reveal_list[0].food_rect == reveal_list[1].food_rect:
            score += 1
            attempts += 1
            reveal_list.clear()
        elif len(reveal_list) >= 2 and reveal_list[0].food_rect != reveal_list[1].food_rect and timer == 0:
            attempts += 1
            for each in reveal_list:
                cloud_cover_list.append(each)
            reveal_list.clear()

        for food in food_list:
            food.draw_food()

        for cloud in cloud_cover_list:
            cloud.draw_cloud()

        game_screen.blit(scoreboard, (int(screen_width * .195), int(screen_height * .868)))
        game_screen.blit(track_attempts, (int(screen_width * .566), int(screen_height * .868)))

        if score == 10:
            running = 3

    if running == 3:
        scoreboard = text_font.render('Score: ' + str(score), 1, (0, 0, 0))
        track_attempts = text_font.render('Attempts: ' + str(attempts), 1, (0, 0, 0))

        play_again.draw()

        if play_again_rect.collidepoint(pygame.mouse.get_pos()):
            play_again_over.draw()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

            elif event.type == QUIT:
                running = 0

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if play_again_rect.collidepoint(pos):
                        cloud_cover_list = [grid1_1, grid1_2, grid1_3, grid1_4, grid1_5, grid2_1,
                                            grid2_2, grid2_3, grid2_4, grid2_5, grid3_1, grid3_2,
                                            grid3_3, grid3_4, grid3_5, grid4_1, grid4_2, grid4_3,
                                            grid4_4, grid4_5]
                        reveal_list.clear()
                        score = 0
                        attempts = 0
                        running = 2

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if play_again_rect.collidepoint(pos):
                        play_again_click.draw()

        winner_image.draw()
        game_screen.blit(scoreboard, (int(screen_width * .195), int(screen_height * .868)))
        game_screen.blit(track_attempts, (int(screen_width * .566), int(screen_height * .868)))

    pygame.display.flip()

pygame.quit()
