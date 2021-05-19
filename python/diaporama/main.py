import pygame
from varaibles import constantes, colors , variation
from assets import pictures, screen_update,font
from action import action_event, result

def initialize(fps,width,height):
    """
    initialize pygame
    :param fps:
    :param width:
    :param height:
    :return:
    """
    screen = pygame.display.set_mode((width,height ), pygame.FULLSCREEN)  # dimension of screen
    pygame.display.set_caption('exposer Algo glouton')  # name of program
    icon_32x32 = pygame.image.load("./assets/picture/souris.png").convert_alpha()  # source of icon
    pygame.display.set_icon(icon_32x32)  # dimension of icon
    clock = pygame.time.Clock()  # for fps
    ms = clock.tick(fps)  # for fps

    return screen,clock

def main():
    pygame.init()
    fps,width,height,key,reading_speed,bin_position,speed_transition,centre = constantes()
    lecture,slides = variation()
    red,black,white = colors()
    screen,clock = initialize(fps,width,height)
    list_picture,list_rect = pictures(width, height,bin_position)
    font()
    while 42: # infinite loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (key[pygame.K_LALT] or key[pygame.K_LALT])):  # red cross or alt f4
                pygame.quit()  # closing
        pygame.init()
        pygame.mouse.set_visible(False)
        lecture = screen_update(screen,red,lecture,reading_speed,slides,height,black,white,width,list_picture)
        slides,lecture = action_event(event,slides,list_rect,width,height,lecture,centre,bin_position)
        lecture = result(slides, bin_position, width, height,list_rect,lecture,speed_transition,list_picture)

main() # main function
