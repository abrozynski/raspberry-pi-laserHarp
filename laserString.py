from calibration import *
import RCtime, time
import pygame


class laserString:
  
  note = 'notes/ukeA.mp3'

  def __init__(self, pin):
    self.pin = pin
    self.calibration = Calibration(pin)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(self.note)

  def play(self):
    max_RC_time = self.calibration.light_mean
    while True:
      reading =RCtime.RCtime(self.pin, max_reading=max_RC_time) 
      if reading < (self.calibration.dark_mean + 2.0*self.calibration.dark_std):
        pygame.mixer.music.play()
