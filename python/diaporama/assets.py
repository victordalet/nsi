import pygame,time

def pictures(width,height,bin_position):
    """
    load pictures
    :param width:
    :param height:
    :param bin_position:
    :return:
    """
    global first
    first  = pygame.image.load("./assets/picture/first.jpg")
    first = pygame.transform.smoothscale(first, (width, height))
    first = first.convert_alpha()
    global first_rectangle
    first_rectangle = first.get_rect()

    global book1
    book1  = pygame.image.load("./assets/picture/book1.jpg")
    book1 = pygame.transform.smoothscale(book1, (int(width/2),height))
    book1 = book1.convert_alpha()
    global book1_rectangle
    book1_rectangle = book1.get_rect()
    book1_rectangle.center = (bin_position)

    global book2
    book2  = pygame.image.load("./assets/picture/book2.jpg")
    book2 = pygame.transform.smoothscale(book2, (int(width/2),height))
    book2 = book2.convert_alpha()
    global book2_rectangle
    book2_rectangle = book2.get_rect()
    book2_rectangle.center = (bin_position)

    global question
    question  = pygame.image.load("./assets/picture/question.jpg")
    question = pygame.transform.smoothscale(question, (int(width),height))
    question = question.convert_alpha()
    global question_rectangle
    question_rectangle = question.get_rect()
    question_rectangle.center = (bin_position)

    global souris
    souris  = pygame.image.load("./assets/picture/souris.png")
    souris = pygame.transform.smoothscale(souris, (30,30))
    souris = souris.convert_alpha()
    global souris_rectangle
    souris_rectangle = souris.get_rect()
    souris_rectangle.center = (pygame.mouse.get_pos())

    global perso1
    perso1  = pygame.image.load("./assets/picture/perso1.png")
    perso1 = pygame.transform.smoothscale(perso1, (200,200))
    perso1 = perso1.convert_alpha()
    global perso1_rectangle
    perso1_rectangle = perso1.get_rect()
    perso1_rectangle.center = (bin_position)

    global perso2
    perso2  = pygame.image.load("./assets/picture/perso2.png")
    perso2 = pygame.transform.smoothscale(perso2, (200, 200))
    perso2 = perso2.convert_alpha()
    global perso2_rectangle
    perso2_rectangle = perso2.get_rect()
    perso2_rectangle.center = (bin_position)

    global fin
    fin  = pygame.image.load("./assets/picture/fin.jpg")
    fin = pygame.transform.smoothscale(fin, (width, height))
    fin = fin.convert_alpha()
    global fin_rectangle
    fin_rectangle = fin.get_rect()
    fin_rectangle.center = (bin_position)

    global livre
    livre = pygame.image.load("./assets/picture/livre.jpg")
    livre = pygame.transform.smoothscale(livre, (int(width/2), int(height)))
    livre= livre.convert_alpha()
    global livre_rectangle
    livre_rectangle = livre.get_rect()
    livre_rectangle.center = (bin_position)

    global text2
    text2 = pygame.image.load("./assets/picture/text2.png")
    text2 = pygame.transform.smoothscale(text2, (700, int(height/2+100)))
    text2= text2.convert_alpha()
    global text2_rectangle
    text2_rectangle = text2.get_rect()
    text2_rectangle.center = (bin_position)

    global text1
    text1 = pygame.image.load("./assets/picture/text1.png")
    text1 = pygame.transform.smoothscale(text1, (700, int(height/2+100)))
    text1= text1.convert_alpha()
    global text1_rectangle
    text1_rectangle = text1.get_rect()
    text1_rectangle.center = (bin_position)

    list_picture = [first,book1,book2,question,souris,perso1,perso2,fin,livre,text2,text1]
    list_rect = [first_rectangle,book1_rectangle,book2_rectangle,question_rectangle,souris_rectangle,perso1_rectangle,perso2_rectangle,fin_rectangle,livre_rectangle,
                 text2_rectangle,text1_rectangle]
    return list_picture,list_rect

def font():
    """
    load fonts
    :return:
    """
    global title
    title = pygame.font.Font("./assets/font/title.ttf", 100)

    global norm
    norm = pygame.font.Font("./assets/font/norm.ttf",35)

    global little
    little = pygame.font.Font("./assets/font/norm.ttf",30)

def screen_update_picture(screen):
    """
    display pictures
    :param screen:
    :return:
    """
    screen.blit(first, first_rectangle)
    screen.blit(book1,book1_rectangle)
    screen.blit(book2,book2_rectangle)
    screen.blit(question,question_rectangle)
    screen.blit(perso1,perso1_rectangle)
    screen.blit(perso2,perso2_rectangle)
    screen.blit(livre,livre_rectangle)
    screen.blit(text2,text2_rectangle)
    screen.blit(text1,text1_rectangle)
    screen.blit(souris, souris_rectangle)
    screen.blit(fin,fin_rectangle)


def screen_update_label(screen,red,lecture,reading_speed,slides,height,black,white,width):
    """
    display sentences
    :param screen:
    :param red:
    :param lecture:
    :param reading_speed:
    :param slides:
    :param height:
    :param black:
    :param white:
    :param width:
    :return:
    """
    slow_sentence_title = ""
    if slides == 0:
        sentence_title = "Parcours : Imagination et Pensée"
        if lecture == True:
            for i in range(len(sentence_title)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += sentence_title[i]
                label_title = title.render( "{}".format(slow_sentence_title), 1, red)
                screen.blit(label_title, (250,20))
                time.sleep(reading_speed)
                label_name = little.render("Victor Dalet 1e3".format(sentence_title), 1, white)
                screen.blit(label_name, (50, height - 100))
                pygame.display.flip()
            lecture = False
        else :
            label_title = title.render("{}".format(sentence_title), 1, red)
            screen.blit(label_title, (250, 20))
            label_name = little.render("Victor Dalet 1e3".format(sentence_title), 1, white)
            screen.blit(label_name, (50, height - 100))

    elif slides == 4:
        problematic1 = "Quelle (s) figure(s) du sauvage nous est présentée dans ces textes ?"
        problematic2 = "Comment la solitude est-elle mise en avant dans ces textes ? "
        problematic3 = "Quel regard sur l’autre et sur l’ailleurs ces auteurs mettent-ils en avant ? "
        if lecture == True:
            label_pb = title.render("Problématiques:",1, white)
            screen.blit(label_pb, (width*1/3, 100))
            for i in range(len(problematic1)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += problematic1[i]
                label_pb1 = norm.render( "{}".format(slow_sentence_title), 1, black)
                screen.blit(label_pb1, (250,height*1/3))
                time.sleep(reading_speed)
                pygame.display.flip()
            slow_sentence_title = ""
            for i in range(len(problematic2)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += problematic2[i]
                label_pb2 = norm.render( "{}".format(slow_sentence_title), 1, black)
                screen.blit(label_pb2, (250,height/2))
                label_pb1 = norm.render("{}".format(problematic1), 1, black)
                screen.blit(label_pb1, (250, height*1/3))
                time.sleep(reading_speed)
                pygame.display.flip()
            slow_sentence_title = ""
            for i in range(len(problematic3)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += problematic3[i]
                label_pb3 = norm.render( "{}".format(slow_sentence_title), 1, black)
                screen.blit(label_pb3, (250,height*2/3))
                label_pb1 = norm.render("{}".format(problematic1), 1, black)
                screen.blit(label_pb1, (250, height*1/3))
                label_pb2 = norm.render("{}".format(problematic2), 1, black)
                screen.blit(label_pb2, (250, height/2))
                time.sleep(reading_speed)
                pygame.display.flip()
            lecture = False
        else :
            label_pb1 = norm.render("{}".format(problematic1), 1, black)
            screen.blit(label_pb1, (250, height*1/3))
            label_pb2 = norm.render("{}".format(problematic2), 1, black)
            screen.blit(label_pb2, (250, height/2))
            label_pb3 = norm.render("{}".format(problematic3), 1, black)
            screen.blit(label_pb3, (250, height*2/3))
            souris_rectangle.center = (pygame.mouse.get_pos())

    return lecture

def screen_update(screen,red,lecture,reading_speed,slides,height,black,white,width,list_picture):
    """
    call the other functions to display
    :param screen:
    :param red:
    :param lecture:
    :param reading_speed:
    :param slides:
    :param height:
    :param black:
    :param white:
    :param width:
    :param list_picture:
    :return:
    """
    screen_update_picture(screen)
    lecture = screen_update_label(screen,red,lecture,reading_speed,slides,height,black,white,width)
    souris_rectangle.center = (pygame.mouse.get_pos())
    if slides == 5:
        pygame.draw.rect(screen, white, (width/2, 0, 10, height))
    pygame.display.flip()  #automatically update the screen

    return lecture