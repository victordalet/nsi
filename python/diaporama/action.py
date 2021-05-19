import pygame
def action_event(event,slides,list_rect,width,height,lecture,centre,bin_position):
    """
    for mousses click
    :param event:
    :param slides:
    :param list_rect:
    :param width:
    :param height:
    :param lecture:
    :return:
    """
    pygame.event.pump()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left = 1 right = 3 middle = 2 for mousse
        if slides == 0:
            slides = 1
        elif slides == 2:
            slides = 2.1
        elif slides == 2.2:
            slides = 3
        elif slides == 4:
            slides = 5

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # left = 1 right = 3 middle = 2 for mousse
        if slides == 1:
            slides = 2
        elif slides == 2.1:
            slides = 2.2
        elif slides == 3:
            slides = 4

    if event.type == pygame.MOUSEBUTTONUP:
        if slides == 1:
            if list_rect["trad_rectangle"].collidepoint(event.pos):
                list_rect["exemple1trad_rectangle"].center = centre
            else:
                list_rect["exemple1trad_rectangle"].center = (bin_position)
            if list_rect["glouton_rectangle"].collidepoint(event.pos):
                list_rect["exemple1glouton_rectangle"].center = centre
            else:
                list_rect["exemple1glouton_rectangle"].center = (bin_position)

        if slides == 3:
            if list_rect["trad_rectangle"].collidepoint(event.pos):
                list_rect["reseau_trad_rectangle"].center = centre
            else:
                list_rect["reseau_trad_rectangle"].center = (bin_position)
            if list_rect["glouton_rectangle"].collidepoint(event.pos):
                list_rect["reseau_glouton_rectangle"].center = centre
            else:
                list_rect["reseau_glouton_rectangle"].center = (bin_position)
            if list_rect["go_rectangle"].collidepoint(event.pos):
                list_rect["reseau_resultat_rectangle"].center=(width/2,height*3.5/4)
            else :
                list_rect["reseau_resultat_rectangle"].center = (bin_position)

        if slides == 5:
            if list_rect["trad_rectangle"].collidepoint(event.pos):
                list_rect["compression_trad_rectangle"].center = centre
            else:
                list_rect["compression_trad_rectangle"].center = (bin_position)
            if list_rect["glouton_rectangle"].collidepoint(event.pos):
                list_rect["compression_glouton_rectangle"].center = centre
            else:
                list_rect["compression_glouton_rectangle"].center = (bin_position)
            if list_rect["go_rectangle"].collidepoint(event.pos):
                list_rect["compression_resultat_rectangle"].center=(width/2,height*3.5/4)
            else :
                list_rect["compression_resultat_rectangle"].center = (bin_position)


    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pygame.event.pump()
        slides -= 1



    return slides,lecture

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
        if list_rect["trad_rectangle"].y < height/2:
            list_rect["trad_rectangle"].y += speed_transition
            list_rect["glouton_rectangle"].y += speed_transition
            lecture = True

    elif slides == 2:
        list_rect["trad_rectangle"].center = (width*1/5,-height)
        list_rect["glouton_rectangle"].center = (width*4/5,-height)
        list_rect["exemple2_rectangle"].center = (width/2,height/2)

    if slides == 2.1:
        list_rect["exemple2_rectangle"].center = (bin_position)
        list_rect["memoire_rectangle"].center = (width / 2, height / 2)

    if slides == 2.2:
        list_rect["reseau_dic_rectangle"].center = (width/2,height/2)
        list_rect["memoire_rectangle"].center = (bin_position)

    elif slides == 3 :
        if list_rect["trad_rectangle"].y < height/2:
            list_rect["trad_rectangle"].y += speed_transition
            list_rect["glouton_rectangle"].y += speed_transition
            list_rect["reseau_dic_rectangle"].center = (bin_position)
            list_rect["go_rectangle"].center = (10,10)


    elif slides == 4:
        list_rect["trad_rectangle"].center = (width*1/5,-height)
        list_rect["glouton_rectangle"].center = (width*4/5,-height)
        list_rect["reseau_resultat_rectangle"].center = (bin_position)
        list_rect["arbre_rectangle"].center = (width/2,height/2)

    elif slides == 5 :
        if list_rect["trad_rectangle"].y < height/2:
            list_rect["trad_rectangle"].y += speed_transition
            list_rect["arbre_rectangle"].center = (bin_position)
            list_rect["glouton_rectangle"].y += speed_transition
            list_rect["go_rectangle"].center = (10,10)

    return lecture