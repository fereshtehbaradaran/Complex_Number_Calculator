from complexNumber import Complex
import math

def summation(c1, c2):
    return Complex(c1.real + c2.real , c1.img + c2.img)

def subtraction(c1, c2):
    return Complex(c1.real - c2.real , c1.img - c2.img)

def multiplication(c1, c2):
    return Complex(c1.real*c2.real - c1.img*c2.img, c1.real*c2.img + c2.real*c1.img)

def division(c1,c2):
    return Complex((c1.real*c2.real+c1.img*c2.img)/(c2.real**2+c2.img**2), (c1.img*c2.real - c1.real*c2.img)/(c2.real**2+c2.img**2)) 

def power(c,n):
    r = c.getR()
    teta = c.getTeta()
    return Complex((r**n)*math.cos(n*teta),(r**n)*math.sin(n*teta))