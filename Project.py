import datetime
cdt = datetime.datetime.now()
currentTime = cdt.strftime("%H:%M")
import pygame

pygame.init()
window = pygame.display.set_mode((750,1334))
while True:
    pygame.display.set_caption(currentTime)
for event in pygame.event.get():
    
