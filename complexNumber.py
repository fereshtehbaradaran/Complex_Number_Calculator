import math

class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img
    
  def rct(self):
      result = str(self.real)
      if self.img >= 0 :
          result += "+"
      result = result + str(self.img) + "i"
      return result
      
  def tri(self):
      r = math.sqrt(self.real**2 + self.img**2)
      teta = math.atan(self.img/self.real)
      return str(r)+"(cos("+str(teta)+") + isin("+str(teta)+"))"
      
  def exp(self):
      r = math.sqrt(self.real**2 + self.img**2)
      teta = math.atan(self.img/self.real)
      return str(r) + "e^i(" +str(teta) +")"
      
  def getR(self):
      return math.sqrt(self.real**2 + self.img**2)
    
  def getTeta(self):
      return math.atan(self.img/self.real)