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


  def calibrate(self):
    self.calibrateLight()
    self.calibrateDark()

    # if 'light' and 'dark' intensities are too close, recalibration is required
    if ((self.dark_mean + self.dark_std) > (self.light_mean - self.light_std)):
      print 'Insufficient Light Difference. Please recalibrate'


  def calibrateLight(self):
    lightData=[]
    raw_input('Press Enter to calibrate light')
    for i in range(0,100):
      print i
      lightData.append(RCtime.RCtime(self.pin))
    self.light_mean =numpy.mean(lightData)
    self.light_std = numpy.std(lightData)
    print 'Ok!'

  def calibrateDark(self):
    darkData =[]
    raw_input('Press Enter to Calibrate Dark')
    for i in range(0,100):
      print i
      darkData.append(RCtime.RCtime(self.pin))
    self.dark_mean=numpy.mean(darkData)
    self.dark_std=numpy.std(darkData)
    print 'Ok!'
