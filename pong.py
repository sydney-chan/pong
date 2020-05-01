import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

teal = (10,118,135)                                     #picking colors
white = (255,255,255)

size = (700,500)                                        #creating screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("boink")

time = pygame.time.Clock()


half_lscreen = 349
half_hscreen = 249

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(teal)
        font = pygame.font.SysFont('Courier', 70)
        titletext = font.render('Pong', 1, white)
        screen.blit(titletext, (half_lscreen-200, half_hscreen))

        font = pygame.font.SysFont('Courier', 30)
        instruct = font.render('press space to start', 1, white)
        screen.blit(instruct, (300, 400))
        keys = pygame.key.get_pressed()                             #GAME CODE
        if keys[pygame.K_SPACE]:
            intro = False
        pygame.display.update()
        time.tick(60)


# def player_name():
#     screen.fill(teal)
#     font = pygame.font.SysFont('Courier', 30)
#     prompttext = font.render('input Player 1 Name', 1, white)
#     screen.blit(prompttext, (half_lscreen-200, half_hscreen))
#     pygame.display.update()
#
#     playerinput = ''
#     name = True
#
#     while name:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_BACKSPACE:
#                     playerinput = playerinput[:-1]
#                 elif event.type == pygame.K_RETURN:
#                     playerinput = ''
#                 else:
#                     playerinput += event.unicode


                #elif event.key == pygame.K_LSHIFT



paddleR = Paddle(white, 10,100)                         #create right paddle
paddleR.rect.x = 670
paddleR.rect.y = 200
#
paddleL = Paddle(white, 10,100)                         #create left paddle
paddleL.rect.x = 20
paddleL.rect.y = 200

ball = Ball(white, 30, 30)                             #create ball
ball.rect.x = half_lscreen
ball.rect.y = half_hscreen


# ball2 = Ball(white, 30, 30)                             #create ball
# ball2.rect.x = half_lscreen
# ball2.rect.y = half_hscreen

sprites = pygame.sprite.Group()                         #create sprite group
sprites.add(paddleR)
sprites.add(paddleL)
sprites.add(ball)
# sprites.add(ball2)
#
#




def countdown(t, restart, player1, player2):
    while t >= 0:
        screen.fill(teal)
        font = pygame.font.Font(None, 74)                           #print player scores
        text = font.render(str(player1),1,white)
        screen.blit(text, (250,10))
        text = font.render(str(player2),1,white)
        screen.blit(text, (420,10))

        sprites.draw(screen)                                         #draw sprites

        pygame.draw.line(screen, teal, [349,0],[349,500],70)            #cover up line
        font = pygame.font.Font(None, 100)
        text = font.render(str(t),1,white)
        screen.blit(text, (half_lscreen-10,half_hscreen-10))            #countdown numbers
        pygame.display.flip()



        # if restart == True:
        #     font = pygame.font.Font(None, 74)
        #     text = font.render("Player   wins!",1,white)
        #     screen.blit(text, (200,50))
        #     font = pygame.font.Font(None, 40)
        #     text = font.render("Press space to play again",1,white)
        #     screen.blit(text, (200,200))
        #     keys = pygame.key.get_pressed()                             #GAME CODE
        #     if keys[pygame.K_SPACE]:
        #         playing = True
        #         break
        #     pygame.display.update()


        t -= 1
        time.tick(60)
        pygame.time.wait(1000)                                              #slow down
        if t==0:

            ball.rect.x = half_lscreen
            ball.rect.y = half_hscreen


            #ball.velocity[0] = -ball.velocity[0]
            #ball2.rect.x = half_lscreen
            #ball2.rect.y = half_hscreen
            #ball2.velocity[0] = -ball.velocity[0]
        #pygame.display.flip()



game_intro()

def playgame():
    go = True                                               #start game

    player1 = 0
    player2 = 0
    while go:                                               #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
                break
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    go = False
                    break
                    pygame.quit()

        sprites.update()


        keys = pygame.key.get_pressed()                             #GAME CODE
        if keys[pygame.K_UP]:
            paddleR.moveup(5)
        if keys[pygame.K_DOWN]:
            paddleR.movedown(5)
        if keys[pygame.K_w]:
            paddleL.moveup(5)
        if keys[pygame.K_s]:
            paddleL.movedown(5)






        if ball.rect.x>=675: #or ball2.rect.x>=675:                                        #if ball hits back wall, opposite player scores
            player1+=1
            if player1==4:
                go=False
                screen.fill(teal)                                           #show screen
                pygame.draw.line(screen, white, [349,0],[349,500],5)
                sprites.draw(screen)

                font = pygame.font.Font(None, 74)
                text = font.render(str(player1),1,white)
                screen.blit(text, (250,10))
                text = font.render(str(player2),1,white)
                screen.blit(text, (420,10))
                pygame.draw.line(screen, teal, [349,0],[349,500],50)
                font = pygame.font.Font(None, 74)
                text = font.render("Player 1 wins!",1,white)
                screen.blit(text, (200,200))
                font = pygame.font.Font(None, 40)
                # text = font.render("Press space to play again",1,white)


                # countdown(9, True)
                pygame.display.flip()
                pygame.time.wait(5000)
                break

            countdown(3, False, player1, player2)
            ball.bounce()
            sprites.update()


        if ball.rect.x<=0:# or ball2.rect.x<=0:
            player2+=1
            if player2==4:
                go=False
                screen.fill(teal)
                                                           #show screen
                pygame.draw.line(screen, white, [349,0],[349,500],5)
                sprites.draw(screen)

                font = pygame.font.Font(None, 74)
                text = font.render(str(player1),1,white)
                screen.blit(text, (250,10))
                text = font.render(str(player2),1,white)
                screen.blit(text, (420,10))
                pygame.draw.line(screen, teal, [349,0],[349,500],50)
                font = pygame.font.Font(None, 74)
                text = font.render("Player 2 wins!",1,white)
                screen.blit(text, (200,200))
                font = pygame.font.Font(None, 40)
                # text = font.render("Press space to play again",1,white)

                # countdown(9, True)

                pygame.display.flip()
                pygame.time.wait(5000)

                break
            countdown(3, False, player1, player2)
            ball.bounce()
            sprites.update()


        if ball.rect.y>475:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]




        # if ball2.rect.y>475:                                              were going to try 2 balls
        #     ball2.velocity[1] = -ball2.velocity[1]
        # if ball2.rect.y<0:
        #     ball2.velocity[1] = -ball2.velocity[1]

        #
        # if ball2.rect.x>=675:                                        #if ball hits back wall, opposite player scores
        #     player1+=1
        #     ball2.rect.x = half_lscreen
        #     ball2.rect.y = half_hscreen
        #     ball2.velocity[0] = -ball.velocity[0]
        #
        # if ball2.rect.x<=0:
        #     player2+=1
        #     ball2.rect.x = half_lscreen
        #     ball2.rect.y = half_hscreen
        #     ball2.velocity[0] = -ball2.velocity[0]



        if pygame.sprite.collide_mask(ball, paddleR) or pygame.sprite.collide_mask(ball, paddleL):
            ball.bounce()

        # if pygame.sprite.collide_mask(ball2, paddleR) or pygame.sprite.collide_mask(ball2, paddleL):
        #     ball2.bounce()

        # if pygame.sprite.collide_mask(ball, ball2):
        #     ball.bounce()
            # ball2.bounce()

        screen.fill(teal)                                           #show screen
        pygame.draw.line(screen, white, [349,0],[349,500],5)
        sprites.draw(screen)

        font = pygame.font.Font(None, 74)
        text = font.render(str(player1),1,white)
        screen.blit(text, (250,10))
        text = font.render(str(player2),1,white)
        screen.blit(text, (420,10))

        pygame.display.flip()
        time.tick(60)



# playing = True
# while playing:
#     playgame()
#     countdown(9, True)
playgame()
pygame.quit()
