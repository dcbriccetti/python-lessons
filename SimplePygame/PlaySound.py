import pygame, time

pygame.init()
sound = pygame.mixer.Sound('powerup.wav')
sound.play(loops=0)
time.sleep(3) # Run long enough to hear the sound
