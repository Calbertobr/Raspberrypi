#!/usr/bin/python

import time
import random
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
led = [[0,4,7,3,0,5],[1,5,6,2,1,4],[2,6,5,1,2,3],[3,7,4,0,2,3],[4,0,3,7,3,2],[5,1,2,6,3,2],[6,2,1,5,4,1],[7,3,0,4,5,0]]
pixel = [[255,   0,  0], [255,   0,   0], [255,  87,   0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122], [255,  0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240], [255, 105,  0], [255, 214,   0], [187, 255,   0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255], [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255], [170, 255,  0], [ 61, 255,   0], [  0, 255,  48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255], [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255], [  0, 255, 66], [  0, 255, 174], [  0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192], [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]]
def aleatorio(x,y):
    pix=pixel[random.randrange( 0, 64, 4 )]
    r = pix[0]
    g = pix[1]
    b = pix[2]
    sense.set_pixel( x, y, r, g, b )
##########################################################
def cruz():
    w=0
    while ( w < 2 ):
        m=0
        for l in led:
            pix=pixel[m]
            r = pix[0]
            g = pix[1]
            b = pix[2]
            for cc in [0,1,2,3]:
                sense.set_pixel(   cc, l[0], r, g, b )
                sense.set_pixel( l[2],   cc, r, g, b )
                sense.set_pixel( 7-cc, l[2], r, g, b )
                sense.set_pixel( l[0], 7-cc, r, g, b )
            m+=4
            time.sleep(0.1)
            sense.clear()
        for l in led:
            pix=pixel[m]
            r = pix[0]
            g = pix[1]
            b = pix[2]
            for cc in [3,2,1,0]:
                sense.set_pixel(   cc, l[2], r, g, b )
                sense.set_pixel( l[0],   cc, r, g, b )
                sense.set_pixel( 7-cc, l[0], r, g, b )
                sense.set_pixel( l[2], 7-cc, r, g, b )
            m-=1
            time.sleep(0.1)
            sense.clear()
        w+=1
    return
##########################################################
def estrelas():
    l=0
    x=0
    y=0
    while( l < 40 ):
        n=0
        while(n < 3):
            x = random.randrange( 0, 8, 1 )
            y = random.randrange( 0, 8, 1 )
            aleatorio(x,y)
            n+=1
        time.sleep(0.05)
        sense.clear()
        l+=1
    return
##########################################################
def mozaico():
#    sense.clear()
    q=0
    while( q < 200 ):
        aleatorio(random.randrange( 0, 8, 1 ),random.randrange( 0, 8, 1 ))
        q+=1
        time.sleep(0.05)
    l=0
    return
##########################################################
def circle():
    m=0
    while ( m < 6):
        for k in led :
            aleatorio(k[0],k[4])
            aleatorio(7-k[0],7-k[4])
            aleatorio(k[4],k[2])
            aleatorio(7-k[4],7-k[2])
            time.sleep(0.1)
            sense.clear()
        m+=1
    return
##########################################################
def borda():
    sense.clear()
    m=0
    while ( m < 4):
        for k in led :
            aleatorio(k[0],7)
            aleatorio(0,k[0])
            aleatorio(k[2],0)
            aleatorio(7,k[2])
            time.sleep(0.1)
        m+=1
#        sense.clear()
        for k in led :
            if(k[0]>0 and k[0]<7 and k[2]>0 and k[2]<7):
                aleatorio(k[2],6)
                aleatorio(1,k[2])
                aleatorio(k[0],1)
                aleatorio(6,k[0])
            time.sleep(0.1)
        m+=1
#        sense.clear()
        for k in led :
            if(k[0]>1 and k[0]<6 and k[2]>1 and k[2]<6):
                aleatorio(k[0],5)
                aleatorio(2,k[0])
                aleatorio(k[2],2)
                aleatorio(5,k[2])
            time.sleep(0.1)
        m+=1
#        sense.clear()
        for k in led :
            if(k[0]>2 and k[0]<5 and k[2]>2 and k[2]<5):
                aleatorio(k[2],4)
                aleatorio(3,k[2])
                aleatorio(k[0],3)
                aleatorio(4,k[0])
            time.sleep(0.1)
        m+=1
        sense.clear()
    return
##########################################################
sense.clear()
while True:
    cruz()
    estrelas()
    mozaico()
    circle()
    borda()
##########################################################
