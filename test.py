import sys
import pygame
import math

def rotatePivoted(im, angle, pivot):
    # rotate the leg image around the pivot
    image = pygame.transform.rotate(im, angle)
    rect = image.get_rect()
    rect.center = pivot
    return image, rect

pygame.init()
green = (0, 255, 0)
size = width, height = (1000,700)
speed = [2, -2]

screen = pygame.display.set_mode(size)
win = screen.get_rect()


img = pygame.image.load("ball.png")
img_rect = img.get_rect()
img_rect.center = win.center

fpsClock = pygame.time.Clock()

# newimg = img
Red = pygame.Color("red")
angle = 0
startpoint = pygame.math.Vector2(500, 350)
endpoint = pygame.math.Vector2(500, 500)

radar = (100,100)
radar_len = 200


# then render the line radar->(x,y)
#pygame.draw.line(screen, Color("black"), radar, (x,y), 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(green)
    #newimg = pygame.transform.rotate(img, angle)
    # newimg = pygame.transform.rotate(newimg, angle)
    #newimg_rect = newimg.get_rect()
    #print(newimg_rect.center)
    #newimg_rect.center = img_rect.center

    angle = (angle + 2) % 360

    x = radar[0] + math.cos(math.radians(angle)) * radar_len
    y = radar[1] + math.sin(math.radians(angle)) * radar_len


    #print(endpoint.rotate(angle).x + startpoint.x)
   #print(endpoint.x)
    #print(endpoint.y)

    #current_endpoint = endpoint.rotate(angle)
    pygame.draw.line(screen, Red, radar, (x, y), 1)
    #pygame.draw.line(screen, Red, startpoint, current_endpoint, 2)



    newimg, newimg_rect = rotatePivoted(img,angle,(x,y))

    screen.blit(newimg, newimg_rect)
    pygame.display.flip()
    fpsClock.tick(30)