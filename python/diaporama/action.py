import pygame
def action_event(event,slides,list_rect,width,height):
    """
    for mouse click
    :param event:
    :param slides:
    :param list_rect:
    :param width:
    :param height:
    :return:
    """
    pygame.event.pump()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[0].collidepoint(event.pos):
            if slides == 0:
                list_rect[1].center = (1 / 4 * width, -height)
                list_rect[2].center = (3 / 4 * width, -height)
                slides = 1

    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[1].collidepoint(event.pos):
            if slides == 1:
                slides = 2
            elif slides == 2:
                slides = 3

    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[2].collidepoint(event.pos):
            if slides == 1:
                slides = 2
            elif slides == 3:
                slides = 4

    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[3].collidepoint(event.pos):
             slides = 5

    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[6].collidepoint(event.pos):
             slides = 6

    if event.type == pygame.MOUSEBUTTONDOWN:
        if list_rect[8].collidepoint(event.pos):
             slides = 7

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # left = 1 right = 3 middle = 2 for mousse
        slides -= 1
    return slides

def result(slides,bin_position,width,height,list_rect,lecture,speed_transition,list_picture):
    """
    change slideshows
    :param slides:
    :param bin_position:
    :param width:
    :param height:
    :param list_rect:
    :param lecture:
    :param speed_transition:
    :param list_picture:
    :return:
    """
    if slides == 1:
        if list_rect[1].center != (1 / 4 * width, height/2):
            list_rect[1].y += speed_transition
            list_rect[2].y += speed_transition
        else:
            list_rect[1].center = (1 / 4 * width, height/2)
            list_rect[2].center = (3 / 4 * width, height/2)

    elif slides == 2:
        if list_rect[1].center != (width/2,height/2):
            list_rect[1].x += speed_transition
            list_rect[2].x += speed_transition+2
            lecture = True

    elif slides == 3 :
        if list_rect[2].center != (width/2,height/2):
            list_rect[1].x -= speed_transition
            list_rect[2].x -= speed_transition
            lecture = True

    elif slides == 4:
        list_rect[1].center = (bin_position)
        list_rect[2].center = (bin_position)
        list_rect[3].center = (width/2,height/2)

    elif slides == 5:
        list_rect[5].center = (width*1/3 -180,100)
        list_rect[6].center = (width * 2 / 3 +150,100)
        list_rect[9].center = (width*2/3 +120 , height/2+100)
        list_rect[10].center = (width * 1 / 3 -250 + 150, height / 2+100)

    elif slides == 6:
        list_rect[5].center = (bin_position)
        list_rect[6].center = (bin_position)
        list_rect[9].center = (bin_position)
        list_rect[10].center = (bin_position)
        list_rect[8].center = (width/2,height/2)

    elif slides == 7:
        list_rect[3].center = (width / 2, height / 2)
        list_rect[7].center = (width / 2, height / 2)
    return lecture

