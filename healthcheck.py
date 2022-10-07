#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:18:30 2022

@author: clockshield
"""


from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("600x450")

class Doctor():
    
    def __init__(self):
        print("this is class Doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi))
        
    def heart_rate(heart_rate):
        if(heart_rate > 60 and heart_rate < 100):
            print("Great your heart rate is normal") 
        else:
            print("Your heart rate does not appear to be normal, please visit the clinic")
    
class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rates):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Patient name: ", self.patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
        
        
patient1 = Patient("Michael", 30, 0.9144, 80)
patient1.healthCheck()

patient2 = Patient("Jessica", 40, 1, 120)
patient2.healthCheck()
root.mainloop()
