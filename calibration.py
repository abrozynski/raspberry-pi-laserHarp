import RCtime
import numpy

class Calibration:

  def __init__(self, pin):
    self.pin = pin
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
