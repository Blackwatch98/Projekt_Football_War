import pygame
from Network import Network
from Card import Card
import math
import random

#Colors
Red = (255, 0, 0)
Black = (0, 0, 0)
Gray = (128, 128, 128)

#Screen
width = 1000
height = 700

pygame.init()
win = pygame.display.set_mode((width,height))
screen = win.get_rect()

pygame.display.set_caption("Player")

#Globalki
playerNumber = 0
cards = []
const_cards = []

file = 'baby.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

def msg(txt, color, size, x, y):
    font = pygame.font.SysFont("bold", size)
    msgtxt = font.render(txt, True, color)
    msgrect = msgtxt.get_rect()
    msgrect.center = x, y
    win.blit(msgtxt, msgrect)

def rotatePivoted(im, angle, pivot):
    # rotate the leg image around the pivot
    image = pygame.transform.rotate(im, angle)
    rect = image.get_rect()
    rect.center = pivot
    return image, rect

def intro():
    BACKGROUND = pygame.image.load("playground2.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))
    wait = 1
    angle = 0
    radar = (500, 350)
    radar_len = 200

    fpsClock = pygame.time.Clock()
    img = pygame.image.load("ball.png")
    img_rect = img.get_rect()
    img_rect.center = screen.center

    logo = pygame.image.load("soccercard_lays.png")

    while wait:
        win.blit(BACKGROUND, (0, 0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        angle = (angle + 2) % 360

        x = radar[0] + math.cos(math.radians(angle)) * radar_len
        y = radar[1] + math.sin(math.radians(angle)) * radar_len

        pygame.draw.line(win, Red, radar, (x, y), 0)

        newimg, newimg_rect = rotatePivoted(img, angle, (x, y))

        logo_rect = logo.get_rect()
        logo_rect.center = (500, 50)

        win.blit(newimg, newimg_rect)
        win.blit(logo, logo_rect);
        fpsClock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if width/2 + 75 > cur[0] > width/2 -75 and height/2 + 25 > cur[1] > height/2 - 25:
            pygame.draw.rect(win, Gray, [width/2 - 75,height/2 - 30, 150, 50])
            if click[0] == 1:
                wait = 0
        else:
            pygame.draw.rect(win, Black, [width/2 - 75,height/2 - 30, 150, 50])

        msg("START", Red, 60, width / 2, height / 2)
        pygame.display.flip()


    print("Wyszedlem")

def load_players():
    players=[];
    id0=['Duczyminski',99,99,99,5,99,99];
    id1=['Adama',98,80,78,87,42,83];
    id2=['Aguero',88,92,79,90,35,82];
    id3=['Allan',78,76,81,86,87,86];
    id4=['Allison',64,66,65,62,36,65];
    id5=['Anderson',89,77,79,88,55,61];
    id6=['Ayew',82,82,78,85,51,78];
    id7=['Banega',66,76,87,84,80,72];
    id8=['Calvert-Lewin',88,80,68,81,40,83];
    id9=['Chevalier',85,80,76,80,42,79];
    id10=['De Bruyne',88,96,99,96,82,93];
    id11=['de Jong',88,87,93,95,88,90];
    id12=['de Ligt',68,59,67,70,84,85];
    id13=['Doherty',81,71,80,80,81,84];
    id14=['Eriksen',75,83,91,86,54,64];
    id15=['Firmino',80,84,82,89,80,85];
    id16=['Funes Mori',80,82,73,81,46,82];
    id17=['Gnabry',91,86,80,88,46,73];
    id18=['Gomis',74,88,70,81,38,77];
    id19=['Hamdallah',79,85,72,79,33,78];
    id20=['Heaton',83,82,77,88,59,85];
    id21=['Hutchinson',70,70,79,81,80,80];
    id22=['Ilicic',75,88,87,88,46,71];
    id23=['Kane',80,95,86,87,51,87];
    id24=['Kante',91,88,95,95,97,93];
    id25=['Kolarov',75,79,85,82,87,83];
    id26=['Kompany',53,55,68,67,86,82];
    id27=['Lewandowski',81,93,78,89,44,86];
    id28=['Lukaku',80,86,75,76,37,86];
    id29=['Maguire',52,54,69,75,84,86];
    id30=['Mane',99,95,92,97,57,88];
    id31=['Martial',91,85,77,89,42,73];
    id32=['Mbappe',99,96,93,98,55,90];
    id33=['Mendy',93,70,80,84,80,86];
    id34=['Messi',96,98,99,99,50,85];
    id35=['Meyer',81,77,86,88,76,82];
    id36=['Mooy',64,78,84,81,71,80];
    id37=['Neymar',92,87,89,96,33,59];
    id38=['Robertson',86,63,78,80,81,76];
    id39=['Samba',82,78,75,86,59,77];
    id40=['Suarez',79,92,83,87,54,86];
    id41=['Tomkins',45,36,61,61,88,80];
    id42=['van Dijk',78,61,71,73,91,87];
    id43=['Werner',95,87,75,86,38,73];
    id44=['Yedder',87,87,81,88,43,65];

    players.append(id0);
    players.append(id1);
    players.append(id2);
    players.append(id3);
    players.append(id4);
    players.append(id5);
    players.append(id6);
    players.append(id7);
    players.append(id8);
    players.append(id9);
    players.append(id10);
    players.append(id11);
    players.append(id12);
    players.append(id13);
    players.append(id14);
    players.append(id15);
    players.append(id16);
    players.append(id17);
    players.append(id18);
    players.append(id19);
    players.append(id20);
    players.append(id21);
    players.append(id22);
    players.append(id23);
    players.append(id24);
    players.append(id25);
    players.append(id26);
    players.append(id27);
    players.append(id28);
    players.append(id29);
    players.append(id30);
    players.append(id31);
    players.append(id32);
    players.append(id33);
    players.append(id34);
    players.append(id35);
    players.append(id36);
    players.append(id37);
    players.append(id38);
    players.append(id39);
    players.append(id40);
    players.append(id41);
    players.append(id42);
    players.append(id43);
    players.append(id44);

    return players;

'''
def withdraw_cards():
    
    x = 10
    y = 600
    for i in range(0, 8):
        surf = pygame.image.load("test.png")
        surf = pygame.transform.scale(surf, (100, 200))
        cards.append(Card(i, surf)) # pygame.draw.rect
        cards[i].power = x
        lista = ['Lewandowski',1,2,3,4,5,6];
        list[1];
        const_cards.append(cards[i])
        cards[i].surf_rect.midleft = (x, y)
        x += 120
    '''


def random_players(players):
    for i in range(0,43):
        img_url = str(players[i][0]) + ".png"
        surf = pygame.image.load(img_url)
        surf = pygame.transform.scale(surf, (150, 225))
        Cards = Card(i, surf, players[i][0], players[i][1], players[i][2], players[i][3],
                     players[i][4], players[i][5], players[i][6])
        const_cards.append(Cards)

    id = random.sample(range(0, 43), 16);
    id_test = 0

    x = 10;
    y = 600;

    print("Karty graczy wybrane z listy players zawierajacej cala pule dostepnym w grze zawodnikow")
    for i in range(0,43):
        for j in id:
            if i == j:
                cards.append(const_cards[i])
                id_test += 1
                break

    for card in cards:
        card.surf_rect.midleft = (x, y)
        x+=140;





def redrawWindow(game, p, cards,win_flag):
    #print(len(cards))

    if not (game.connected()):
        msg("Waiting for second player...", Red,60,width/2,height/2)
    else:
        if p == 1:
            msg("Your move:", Black, 40, 300, 50)
            msg("Opponents move:", Black, 40, 650, 50)
        else:
            msg("Your move:", Black, 40, 700, 50)
            msg("Opponents move:", Black, 40, 300, 50)



        pygame.draw.rect(win, Black, [200, 100, 200, 300])
        pygame.draw.rect(win, Black, [600, 100, 200, 300])

        pygame.draw.rect(win, Black, [400, 425, 200, 40])

        msg(("Wynik: "+str(game.points[0])+":"+str(game.points[1])), Red, 40, width/2, 445)

        if game.p1Went:
            msg("Locked In", Red, 40,310,250)
        else:
            msg("Waiting...", Red, 40,310,250)

        if game.p2Went:
            msg("Locked In", Red, 40,710,250)
        else:
            msg("Waiting...", Red, 40,710,250)

        moves = game.get_played_cards()

        name = ""
        if p == 2 and game.bothWent():
            for card in const_cards:
                if card.get_card_id() == int(moves[0]):
                    name = str(card.name) + ".png"
                    break
            opp_move = pygame.image.load(name)
            opp_move = pygame.transform.scale(opp_move, (200, 300))
            opp_move_rect = opp_move.get_rect()
            opp_move_rect.topleft = (200, 100)
            win.blit(opp_move,opp_move_rect)
            pygame.display.flip()
        elif p == 1 and game.bothWent():
            for card in const_cards:
                if card.get_card_id() == int(moves[1]):
                    name = str(card.name) + ".png"
                    break
            opp_move = pygame.image.load(name)
            opp_move = pygame.transform.scale(opp_move, (200, 300))
            opp_move_rect = opp_move.get_rect()
            opp_move_rect.topleft = (600, 100)
            win.blit(opp_move,opp_move_rect)
            pygame.display.flip()

        for card in cards:
            win.blit(card.surf,card.surf_rect)

    pygame.display.update()

def win_protocol(won,playerNumber):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    BACKGROUND = pygame.image.load("playground2.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))
    win.blit(BACKGROUND, (0, 0))

    pygame.draw.rect(win, Black, [150, 150, 700, 400])
    pygame.draw.rect(win, Gray, [200, 200, 600, 300])

    if won == -1:
        msg("DUNNO HOW BUT\n YOU BOTH WON", Red, 80, width / 2, height / 2)
    elif won == playerNumber:
        msg("YOU WON THE GAME", Red, 80,width/2,height/2)
    else:
        msg("YOU LOST :C", Red, 80, width / 2, height / 2)


    pygame.display.update()


def goal_animation(direction,win_flag):
    BACKGROUND = pygame.image.load("playground2.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))

    file2 = 'Omae.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file2)
    pygame.mixer.music.play()
    pygame.time.wait(500)

    x = 500
    y = 350

    socker = pygame.image.load("miszcz2.png")
    socker_rect = socker.get_rect()
    socker_rect.center = (x,y)

    x = 400
    y = 350

    socker2 = pygame.image.load("miszcz3.png")
    socker_rect2 = socker2.get_rect()
    socker_rect2.center = (x, y)


    ball = pygame.image.load("small_ball.png")
    ball_rect = ball.get_rect()
    ball_rect.center = (550,350)

    if win_flag == 0:
        msg("Tie Game!", Red, 40, 500, 350)
        pygame.display.flip()
        pygame.time.wait(1000)
        return

    if win_flag == 1:
        msg("You Won!", Red, 40, 500, 350)
        pygame.display.flip()
        pygame.time.wait(1000)
    if win_flag == 2:
        msg("You Lost!", Red, 40, 500, 350)
        pygame.display.flip()
        pygame.time.wait(1000)

    fpsClock = pygame.time.Clock()

    win.blit(ball,ball_rect)
    pygame.display.update()

    print("Direct ", direction)
    while True:
        if direction == 2:
            print("----------------------------------------------------")
            x = 700
            y = 350
            socker_rect.center = (x,y)
            win.blit(socker, socker_rect)
            pygame.display.flip()
            while x >= ball_rect.centerx:
                fpsClock.tick(60)
                win.blit(BACKGROUND, (0, 0))
                x -= 5
                socker_rect.center = (x,y)
                win.blit(socker, socker_rect)
                pygame.display.flip()


        else:
            x = 300
            y = 350
            socker_rect2.center = (x, y)
            win.blit(socker2, socker_rect2)
            pygame.display.flip()
            while x <= ball_rect.centerx:
                fpsClock.tick(60)
                win.blit(BACKGROUND, (0, 0))
                x += 5
                socker_rect2.center = (x,y)
                win.blit(socker2, socker_rect2)
                pygame.display.flip()

                print("xxxxxxxx",socker_rect.centerx)
                print(ball_rect.centerx)
                print(x)

        x = 550
        y = 350

        new_ball = ball
        new_ball_rect = ball_rect


        angle = 0
        angle2 = 0
        if direction == 2:
            while new_ball_rect.centerx > screen.left+20:
                win.blit(BACKGROUND, (0, 0))

                angle2 = (angle2 - 2) % 360
                new_ball, new_ball_rect = rotatePivoted(ball, angle2, (x,y))
                x -= 5
                win.blit(new_ball, new_ball_rect)
                pygame.display.flip()
                fpsClock.tick(60)
            break
        else:
            while new_ball_rect.centerx < screen.right - 20:
                win.blit(BACKGROUND, (0, 0))

                angle = (angle + 2) % 360
                new_ball, new_ball_rect = rotatePivoted(ball, angle, (x,y))
                x += 5
                win.blit(new_ball, new_ball_rect)
                pygame.display.flip()
                fpsClock.tick(60)
            break


    w = 50
    for i in range (0,5):
        win.blit(BACKGROUND, (0, 0))
        msg("GOAL!", Red, w, 500, 350)
        w += 50
        pygame.display.flip()
        fpsClock.tick(60)
    pygame.display.flip()

    pygame.mixer.stop()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.time.delay(500)



def main():
    run = True
    start = True
    havecards = False
    win_flag = -1

    #ustaw mape
    BACKGROUND = pygame.image.load("playground2.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (width, height))
    win.blit(BACKGROUND, (0, 0))

    pygame.display.flip()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if start:
            intro()
            start = False

            n = Network()
            playerNumber = int(n.getP())
            print("You are player ", playerNumber)



            while True:
                try:
                    game = n.send("get")

                except:
                    run = False
                    print("Dead")
                    break


                win.blit(BACKGROUND, (0, 0))

                if not havecards:
                    random_players(load_players());#withdraw_cards()
                    havecards = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for i in range(0,len(cards)):
                            if cards[i].clicked(pos):
                                if playerNumber == 1:
                                    if not game.p1Went:
                                        n.send(str(cards[i].id))
                                        cards[i].surf = pygame.image.load(cards[i].name + ".png")
                                        cards[i].surf = pygame.transform.scale(cards[i].surf, (200, 300))
                                        cards[i].surf_rect.topleft = (200, 100)
                                else:
                                    if not game.p2Went:
                                        n.send(str(cards[i].id))
                                        cards[i].surf = pygame.image.load(cards[i].name + ".png")
                                        cards[i].surf = pygame.transform.scale(cards[i].surf, (200, 300))
                                        cards[i].surf_rect.topleft = (600, 100)

                if game.bothWent():
                    redrawWindow(game, playerNumber, cards,win_flag)
                    pygame.time.delay(2000)
                    try:
                        game = n.send("next_round")
                    except:
                        run = False
                        print("Couldn't get game")
                        break

                    wynik = game.round_winner(const_cards, playerNumber)
                    to_remove = game.get_played_cards()

                    for card in cards:
                        if(playerNumber == 1):
                            if card.id == int(to_remove[0]):
                                cards.remove(card)
                        else:
                            if card.id == int(to_remove[1]):
                                cards.remove(card)

                    if ((wynik == 2 and playerNumber == 2) or (wynik == 1 and playerNumber == 1)):
                        win_flag = 1
                        try:
                            game = n.send("raise")
                        except:
                            run = False
                            print("Dead")
                            break
                    elif wynik == -1:
                        win_flag = 0
                    else:
                        win_flag = 2

                    print(wynik)
                    goal_animation(wynik, win_flag)

                    win_flag = -1

                    pygame.display.flip()

                if game.end == True:
                    break
                redrawWindow(game,playerNumber,cards,win_flag)


        while True:
            won = -1
            if game.points[0] > game.points[1]:
                won = 1
            else:
                won = 2

            win_protocol(won,playerNumber)

main()