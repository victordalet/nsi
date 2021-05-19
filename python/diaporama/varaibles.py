import tkinter, pygame

def constantes():
    fps = 30  # number of frame per seconde
    root = tkinter.Tk()
    width = root.winfo_screenwidth() # width of the screen
    height = root.winfo_screenheight() # height of the screen
    key = pygame.key.get_pressed() # for keyboard
    reading_speed = 0.1 #time of reading
    bin_position = 999999, 55555
    speed_transition = 2
    centre = (width/2,height/2) # center position
    return fps, width, height, key,reading_speed,bin_position,speed_transition,centre

def colors():
    red = (255,0,0)
    black = (0,0,0)
    white = (255,255,255)
    return red,black,white

def variation():
    lecture = True
    slides = 0
    return lecture,slides