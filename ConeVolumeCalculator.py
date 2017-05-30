# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

# Define Function below
# be sure to return an integer
import math

def calculateConeVolume(r, h):
     volume = (1.0/3)*math.pi*r**2*h
     volume = round(volume, 2)
     return volume

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
   answer = calculateConeVolume(10, 2)
   print(asnwer)
