import pygame

import time

import random



pygame.init()



display_width=800

display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock=pygame.time.Clock()



black=(0,0,0)

white = (255,255,255)

red=(255,0,0)





plane_width = 73





clock=pygame.time.Clock()

crashed=False

planeImg=pygame.image.load('albatross.png')
 



def line(linex,liney,linew,lineh,color):

    pygame.draw.rect(gameDisplay,color,[linex,liney,linew,lineh])



def plane(x,y):

    gameDisplay.blit(planeImg,(x,y))



def text_objects(text,font):

    textSurface=font.render(text,True,black)

    return textSurface, textSurface.get_rect()



def message_display(text):

    largeText=pygame.font.Font('freesansbold.ttf',115)

    TextSurf,TextRect = text_objects(text, largeText)

    TextRect.center=((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf,TextRect)



    pygame.display.update()

    time.sleep(2)

    game_loop()



def crash():

    message_display('You Crashed')



def game_loop():

    x=(display_width * 0.45)

    y=(display_height * 0.8)

    x_change=0

    plane_speed=0


    line_starty=-600

    line_startx=400

    line_speed=10

    line_width=5

    line_height=100

    

    gameExit=False

    

    while not gameExit:



        for event in pygame.event.get():

            if event.type ==pygame.QUIT:

                gameExit=True



            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:

                    x_change = -5

                if event.key==pygame.K_RIGHT:

                    x_change = 5



            if event.type==pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:

                    x_change=0

        x+=x_change

                

        gameDisplay.fill(white)


        line(line_startx,line_starty,line_width,line_height,red)
        line_starty+=line_speed

        plane(x,y)



        if x>display_width - plane_width or x<0:

            crash()        

        if line_starty > display_height:

            line_starty= 0 - line_height

            line_startx=400

            

        pygame.display.update()

        clock.tick(60)

game_loop()

pygame.quit()

quit()
