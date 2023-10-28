import numpy as np

class areas_calculator:

   def __init__(self):
      
      area = 0
   
   def circle_area(self):
      radio = float(input('\nIngrese radio: '))
      self.area = np.pi * radio ** 2
      print('\nEl área del círculo es: ', self.area)

class perimeters_calculator:
   
   def __init__(self):
      
      perimeter = 0
   
   def circle_perimeter(self):
      radio = float(input('\nIngrese radio: '))
      self.perimeter = 2 * np.pi * radio     
      print('\nEl perímetro del círculo es: ', self.perimeter)
