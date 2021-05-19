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

    global exemple1glouton
    exemple1glouton  = pygame.image.load("./assets/picture/exemple1glouton.png")
    exemple1glouton = pygame.transform.smoothscale(exemple1glouton, (width, height))
    exemple1glouton = exemple1glouton.convert_alpha()
    global exemple1glouton_rectangle
    exemple1glouton_rectangle = exemple1glouton.get_rect()
    exemple1glouton_rectangle.center = (bin_position)

    global exemple1trad
    exemple1trad  = pygame.image.load("./assets/picture/exemple1trad.png")
    exemple1trad = pygame.transform.smoothscale(exemple1trad, (width, height))
    exemple1trad = exemple1trad.convert_alpha()
    global exemple1trad_rectangle
    exemple1trad_rectangle = exemple1trad.get_rect()
    exemple1trad_rectangle.center = (bin_position)

    global exemple2
    exemple2  = pygame.image.load("./assets/picture/exemple2.png")
    exemple2 = pygame.transform.smoothscale(exemple2, (width, height))
    exemple2 = exemple2.convert_alpha()
    global exemple2_rectangle
    exemple2_rectangle = exemple2.get_rect()
    exemple2_rectangle.center = (width/2,-2*height)

    global souris
    souris  = pygame.image.load("./assets/picture/souris.png")
    souris = pygame.transform.smoothscale(souris, (30,30))
    souris = souris.convert_alpha()
    global souris_rectangle
    souris_rectangle = souris.get_rect()
    souris_rectangle.center = (pygame.mouse.get_pos())

    global memoire
    memoire  = pygame.image.load("./assets/picture/memoire.png")
    memoire = pygame.transform.smoothscale(memoire, (int(width/2),int(height/2)))
    memoire = memoire.convert_alpha()
    global memoire_rectangle
    memoire_rectangle = memoire.get_rect()
    memoire_rectangle.center = (width/2,-height)

    global reseau_dic
    reseau_dic  = pygame.image.load("./assets/picture/reseau_dic.png")
    reseau_dic = pygame.transform.smoothscale(reseau_dic, (width,height))
    reseau_dic = reseau_dic.convert_alpha()
    global reseau_dic_rectangle
    reseau_dic_rectangle = reseau_dic.get_rect()
    reseau_dic_rectangle.center = (bin_position)

    global fin
    fin  = pygame.image.load("./assets/picture/fin.jpg")
    fin = pygame.transform.smoothscale(fin, (width, height))
    fin = fin.convert_alpha()
    global fin_rectangle
    fin_rectangle = fin.get_rect()
    fin_rectangle.center = (bin_position)

    global reseau_trad
    reseau_trad  = pygame.image.load("./assets/picture/reseau_trad.png")
    reseau_trad = pygame.transform.smoothscale(reseau_trad, (width, height))
    reseau_trad = reseau_trad.convert_alpha()
    global reseau_trad_rectangle
    reseau_trad_rectangle = reseau_trad.get_rect()
    reseau_trad_rectangle.center = (bin_position)

    global reseau_glouton
    reseau_glouton  = pygame.image.load("./assets/picture/reseau_glouton.png")
    reseau_glouton = pygame.transform.smoothscale(reseau_glouton, (width, height))
    reseau_glouton = reseau_glouton.convert_alpha()
    global reseau_glouton_rectangle
    reseau_glouton_rectangle = reseau_glouton.get_rect()
    reseau_glouton_rectangle.center = (bin_position)

    global reseau_resultat
    reseau_resultat  = pygame.image.load("./assets/picture/reseau_resultat.png")
    reseau_resultat = pygame.transform.smoothscale(reseau_resultat, (width, 200))
    reseau_resultat = reseau_resultat.convert_alpha()
    global reseau_resultat_rectangle
    reseau_resultat_rectangle = reseau_resultat.get_rect()
    reseau_resultat_rectangle.center = (bin_position)

    global arbre
    arbre = pygame.image.load("./assets/picture/arbre.png")
    arbre = pygame.transform.smoothscale(arbre, (int(width/2),int(height/2)))
    arbre = arbre.convert_alpha()
    global arbre_rectangle
    arbre_rectangle = arbre.get_rect()
    arbre_rectangle.center = (bin_position)

    global compression_trad
    compression_trad = pygame.image.load("./assets/picture/compression_trad.png")
    compression_trad = pygame.transform.smoothscale(compression_trad, (width, height))
    compression_trad = compression_trad.convert_alpha()
    global compression_trad_rectangle
    compression_trad_rectangle = compression_trad.get_rect()
    compression_trad_rectangle.center = (bin_position)

    global compression_glouton
    compression_glouton = pygame.image.load("./assets/picture/compression_glouton.png")
    compression_glouton = pygame.transform.smoothscale(compression_glouton, (width, height))
    compression_glouton = compression_glouton.convert_alpha()
    global compression_glouton_rectangle
    compression_glouton_rectangle = compression_glouton.get_rect()
    compression_glouton_rectangle.center = (bin_position)

    global compression_resultat
    compression_resultat = pygame.image.load("./assets/picture/compression_resultat.png")
    compression_resultat = pygame.transform.smoothscale(compression_resultat, (width, 200))
    compression_resultat = compression_resultat.convert_alpha()
    global compression_resultat_rectangle
    compression_resultat_rectangle = compression_resultat.get_rect()
    compression_resultat_rectangle.center = (bin_position)

    global go
    go = pygame.image.load("./assets/picture/go.png")
    go = pygame.transform.smoothscale(go, (30,30))
    go = go.convert_alpha()
    global go_rectangle
    go_rectangle = go.get_rect()
    go_rectangle.center = (bin_position)

    global trad
    trad = pygame.image.load("./assets/picture/trad.png")
    trad = trad.convert_alpha()
    global trad_rectangle
    trad_rectangle = trad.get_rect()
    trad_rectangle.center = (width*1/5,-height)

    global glouton
    glouton = pygame.image.load("./assets/picture/glouton.png")
    glouton = glouton.convert_alpha()
    global glouton_rectangle
    glouton_rectangle = glouton.get_rect()
    glouton_rectangle.center = (width*4/5,-height)

    dict_picture = {"first":first,"exemple1glouton":exemple1glouton,"exemple1trad":exemple1trad,"exemple2":exemple2,"souris":souris," memoire": memoire,"reseau_dic":reseau_dic,
                    "fin":fin,"reseau_trad":reseau_trad,"reseau_glouton":reseau_glouton,"reseau_resultat":reseau_resultat,"arbre":arbre,"compression_trad":compression_trad,
                    "compression_glouton":compression_glouton,"compression_resultat":compression_resultat,"go":go,"trad":trad,"glouton":glouton}

    dict_rect = {"first_rectangle":first_rectangle,"exemple1glouton_rectangle":exemple1glouton_rectangle,"exemple1trad_rectangle":exemple1trad_rectangle,
                 "exemple2_rectangle":exemple2_rectangle,"souris_rectangle":souris_rectangle,"memoire_rectangle": memoire_rectangle,"reseau_dic_rectangle":reseau_dic_rectangle,
                    "fin_rectangle":fin_rectangle,"reseau_trad_rectangle":reseau_trad_rectangle,"reseau_glouton_rectangle":reseau_glouton_rectangle,
                 "reseau_resultat_rectangle":reseau_resultat_rectangle,"arbre_rectangle":arbre_rectangle,"compression_trad_rectangle":compression_trad_rectangle,
                    "compression_glouton_rectangle":compression_glouton_rectangle,"compression_resultat_rectangle":compression_resultat_rectangle,"go_rectangle":go_rectangle,
                 "trad_rectangle":trad_rectangle,"glouton_rectangle":glouton_rectangle}

    return dict_picture,dict_rect

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
    screen.blit(trad,trad_rectangle)
    screen.blit(glouton,glouton_rectangle)
    screen.blit(exemple1glouton,exemple1glouton_rectangle)
    screen.blit(exemple1trad,exemple1trad_rectangle)
    screen.blit(exemple2,exemple2_rectangle)
    screen.blit(memoire,memoire_rectangle)
    screen.blit(reseau_dic,reseau_dic_rectangle)
    screen.blit(reseau_trad,reseau_trad_rectangle)
    screen.blit(reseau_glouton,reseau_glouton_rectangle)
    screen.blit(reseau_resultat,reseau_resultat_rectangle)
    screen.blit(arbre,arbre_rectangle)
    screen.blit(compression_trad,compression_trad_rectangle)
    screen.blit(compression_glouton,compression_glouton_rectangle)
    screen.blit(compression_resultat,compression_resultat_rectangle)
    screen.blit(souris, souris_rectangle)
    screen.blit(fin,fin_rectangle)
    screen.blit(go,go_rectangle)



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
        sentence_title = "Algorithme Glouton"
        if lecture == True:
            for i in range(len(sentence_title)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += sentence_title[i]
                label_title = title.render("{}".format(slow_sentence_title), 1, red)
                screen.blit(label_title, (400,20))
                time.sleep(reading_speed)
                label_name = little.render("Victor Dalet  /  Ambroise Jaquemet-Ramirez Vega  1e3", 1, white)
                screen.blit(label_name, (50, height - 100))
                pygame.display.flip()
            lecture = False
        else :
            label_title = title.render("{}".format(sentence_title), 1, red)
            screen.blit(label_title, (400, 20))
            label_name = little.render("Victor Dalet  /  Ambroise Jaquemet-Ramirez Vega  1e3", 1, white)
            screen.blit(label_name, (50, height - 100))

    if slides == 4:
        sentence_title = "Codage de Huffman"
        if lecture == True:
            for i in range(len(sentence_title)):
                souris_rectangle.center = (999999, 99999)
                slow_sentence_title += sentence_title[i]
                label_title = title.render("{}".format(slow_sentence_title), 1, red)
                screen.blit(label_title, (400,20))
                time.sleep(reading_speed)
                pygame.display.flip()
            lecture = False
        else :
            label_title = title.render("{}".format(sentence_title), 1, red)
            screen.blit(label_title, (400, 20))


    sentence_norme = "Dans la norme UTF-8, chancun de ses charactères est codé sur un octet, et le fichier pèse donc 16o ctets."

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

    pygame.display.flip()  #automatically update the screen

    return lecture