import pygame

# ingen ork till att lära mig något graphic lib pga sjukdom
# inspirerat av https://github.com/INDAPlus21/eliased-sorting-task-11/blob/master/notherviz.py


def initialize(lst):
    background = (0, 0, 0)
    staple = (255, 150, 45)
    w = 500
    h = 500
    screen = pygame.display.set_mode((w, h))
    screen.fill(background)
    pygame.display.flip()
    maxfraction = (h - 30)/max(lst)
    maxlengthfraction = (w)/len(lst)
    screen.fill(background)
    j = 0
    for i in lst:
        pygame.draw.rect(screen, staple, (j*maxlengthfraction,
                         (h-10)-i*maxfraction, maxlengthfraction/2, i*maxfraction))
        j += 1
        pygame.display.flip()
